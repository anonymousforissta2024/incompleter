#Source: https://stackoverflow.com/questions/76224141/what-does-it-mean-by-typeerror-argument-of-type-adam-is-not-iterable
import os
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import Model
from ISR.models import RRDN, Discriminator
from ISR.models import Cut_VGG19
from ISR.train import Trainer

# Define paths for HR and LR input images
lr_train_dir = 'C:/data/lr_train_150/',
hr_train_dir = 'C:/data/hr_train_150/',
lr_valid_dir = 'C:/data/lr_test_150/',
hr_valid_dir = 'C:/data/hr_test_150/',

lr_train_patch_size = 22 #size of my LR image
layers_to_extract = [5, 9]
scale = 10
hr_train_patch_size = lr_train_patch_size * scale # 220 Size of my HR image


# Instantiate models
rrdn = RRDN(arch_params={'C':4, 'D':3, 'G':64, 'G0':64, 'T':10, 'x':scale}, patch_size=lr_train_patch_size)
discriminator = Cut_VGG19(patch_size=hr_train_patch_size, layers_to_extract=layers_to_extract)
feature_extractor = Discriminator(patch_size=hr_train_patch_size, kernel_size=3)


# Define optimizer and loss function
optimizer = Adam(1e-4, beta_1=0.9, beta_2=0.999)
#loss = 'mse'
loss_weights = {
  'generator': 0.0,
  'feature_extractor': 0.0833,
  'discriminator': 0.01
}
losses = {
  'generator': 'mae',
  'feature_extractor': 'mse',
  'discriminator': 'binary_crossentropy'
} 
learning_rate = {'initial_value': 0.0004, 'decay_factor': 0.5, 'decay_frequency': 30}
log_dirs = {'logs': './logs', 'weights': './weights'}
flatness = {'min': 0.0, 'max': 0.15, 'increase': 0.01, 'increase_frequency': 5}


# Define trainer
trainer = Trainer(generator=rrdn, 
                  discriminator=discriminator,
                  feature_extractor=feature_extractor, 
                  #name='srgan', 
                  log_dirs=log_dirs,
                  #checkpoint_dir='./models', 
                  learning_rate=learning_rate, 
                  losses=losses, 
                  flatness = flatness,
                  loss_weights = loss_weights,
                  adam_optimizer=optimizer,
                  lr_train_dir = 'C:/data/lr_train_150/',
                  hr_train_dir = 'C:/data/hr_train_150/',
                  lr_valid_dir = 'C:/data/lr_test_150/',
                  hr_valid_dir = 'C:/data/hr_test_150/'
                 )

# Train the model
trainer.train(batch_size=16, 
              steps_per_epoch=20, 
              #validation_steps=10, 
              epochs=1, 
              #print_frequency=100
              monitored_metrics={'val_generator_PSNR_Y': 'max'}
             )