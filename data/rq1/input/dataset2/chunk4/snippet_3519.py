#Source: https://stackoverflow.com/questions/75842262/i-am-getting-an-attribute-error-when-creating-a-pytorch-model
from torch import nn
import segmentation_models_pytorch as smp
from segmentation_models_pytorch.losses import DiceLoss 
class segmentationmodels():
  def __init__(self):
    super(segmentationmodels,self).__init__()
    self.arc=smp.Unet(
        encoder_name=ENCODER,
        encoder_weights=weights,
        in_channels=3,
        classes=1,
        activation=None
    )
  def forward(self,images,mask=None):
    logits=self.arc(images)
    if mask != None:
      loss1=DiceLoss(mode='binary')(logits,mask)
      loss2=nn.BCEWithLogitsLoss()(logits,mask)
      return logits,loss1+loss2
    return logits
model=segmentationmodels()
model.to(DEVICE)