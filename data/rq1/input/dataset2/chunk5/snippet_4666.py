#Source: https://stackoverflow.com/questions/66545871/attributeerror-dict-object-has-no-attribute-step
import os
import ast
import torch
import torchaudio
import torch.nn as nn
from torch.nn import functional as F
import torch.optim as optim
from torch.utils.data import DataLoader
from pytorch_lightning.core.lightning import LightningModule
from pytorch_lightning import Trainer
from argparse import ArgumentParser
from model import SpeechRecognition
from dataset import Data, collate_fn_padd
from pytorch_lightning.callbacks import ModelCheckpoint

nodes = int(1)
gpus = int(1)
data_workers = int(0)
train_file  = 'path/to/your/train.json'
valid_file = 'path/to/your/test.json'
valid_every = int(1000)
save_model_path = 'path/where/you/want/to/save/your/model'
logdir = 'path/where/you/want/to/save/your/logs'
epochs = int(10)
batch_size = int(64)
pct_start = float(0.3)
div_factor = int(100)
dparams_override = str("{}")
hparams_override = str("{}")
load_model_from = None
resume_from_checkpoint = None

class SpeechModule(LightningModule):
    def __init__(self, model, args):
        super(SpeechModule, self).__init__()
        self.model = model
        self.criterion = nn.CTCLoss(blank=28, zero_infinity=True)
        self.args = args

    def forward(self, x, hidden):
        return self.model(x, hidden)

    def configure_optimizers(self):
        self.optimizer = optim.AdamW(self.model.parameters(), self.args.learning_rate)
        lr_scheduler = optim.lr_scheduler.ReduceLROnPlateau(
            self.optimizer, mode='min',
            factor=0.50, patience=6
        )
        self.scheduler = {
            'scheduler': lr_scheduler,
            'reduce_on_plateau': True,
            'monitor': 'val_checkpoint_on'
        }

        return [self.optimizer], [self.scheduler]

    def step(self, batch):
        spectrograms, labels, input_lengths, label_lengths = batch 
        bs = spectrograms.shape[0]
        hidden = self.model._init_hidden(bs)
        hn, c0 = hidden[0].to(self.device), hidden[1].to(self.device)
        output, _ = self(spectrograms, (hn, c0))
        output = F.log_softmax(output, dim=2)
        loss = self.criterion(output, labels, input_lengths, label_lengths)
        return loss

    def training_step(self, batch, batch_idx):
        loss = self.step(batch)
        logs = {'loss': loss, 'lr': self.optimizer.param_groups[0]['lr'] }
        return {'loss': loss, 'log': logs}

    def train_dataloader(self):
        d_params = Data.parameters
        d_params.update(dparams_override)
        train_dataset = Data(json_path=self.train_file, **d_params)
        return DataLoader(dataset=train_dataset,
                            batch_size= batch_size,
                            num_workers= data_workers,
                            pin_memory=True,
                            collate_fn=collate_fn_padd)

    def validation_step(self, batch, batch_idx):
        loss = self.step(batch)
        return {'val_loss': loss}

    def validation_epoch_end(self, outputs):
        avg_loss = torch.stack([x['val_loss'] for x in outputs]).mean()
        self.scheduler.step(avg_loss)
        tensorboard_logs = {'val_loss': avg_loss}
        return {'val_loss': avg_loss, 'log': tensorboard_logs}

    def val_dataloader(self):
        d_params = Data.parameters
        d_params.update(dparams_override)
        test_dataset = Data(json_path=valid_file, **d_params, valid=True)
        return DataLoader(dataset=test_dataset,
                            batch_size= batch_size,
                            num_workers= data_workers,
                            collate_fn=collate_fn_padd,
                            pin_memory=True)


def checkpoint_callback():
    return ModelCheckpoint(
        filepath= save_model_path,
        save_top_k=True,
        verbose=True,
        monitor='val_loss',
        mode='min',
        prefix=''
    )

def main(args):
    h_params = SpeechRecognition.hyper_parameters
    h_params.update(hparams_override)
    model = SpeechRecognition(**h_params)
    if load_model_from:
        speech_module = SpeechModule.load_from_checkpoint(load_model_from, model=model)
    else:
        speech_module = SpeechModule(model, args)
    trainer = Trainer()

    trainer = Trainer(                
        max_epochs= epochs, gpus= gpus,
        num_nodes= nodes, distributed_backend=None,
        gradient_clip_val=1.0,                     
        val_check_interval= valid_every,
        checkpoint_callback=checkpoint_callback,
        resume_from_checkpoint= resume_from_checkpoint
    )
    trainer.fit(speech_module)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--learning_rate', default=1e-3, type=float, help='learning rate')

    args = parser.parse_args()
    hparams_override = ast.literal_eval(hparams_override)
    dparams_override = ast.literal_eval(dparams_override)
    if save_model_path:
        if not os.path.isdir(os.path.dirname(save_model_path)):
            raise Exception("the directory for path {} does not exist".format(save_model_path))

    main(args)