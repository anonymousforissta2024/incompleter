#Source: https://stackoverflow.com/questions/49332694/attributeerror-grammatrix-object-has-no-attribute-gradinput
# Define an nn Module to compute content loss in-place
class ContentLoss(object):

    def __init__(self, strength):
      super(ContentLoss, self).__init__()
      self.strength = strength
      self.target = 0
      self.loss = 0
      self.mode = None

    def forward(self, input):
      print("ContentLoss - Forward")
      if self.mode == 'loss':
        print("ContentLoss - Forward - Loss")
        self.loss = (input * self.target) * self.strength #Forward
      elif self.mode == 'capture':
        print("ContentLoss - Forward - Capture")
        self.target = input
      self.output = input 
      return self.output

    def backward(self, input, gradOutput): 
      print("ContentLoss - Backward") 
      if self.mode == 'loss':
        print("ContentLoss - Backward - Loss")
        self.gradInput = input * self.target # Backward
        self.gradInput = self.gradInput * self.strength
        self.gradInput = self.gradInput + gradOutput
      else:
        print("ContentLoss - Backward - Capture")
        self.target = gradOutput
      return self.gradInput


class GramMatrix(object):
   def __init__(self):
     super(GramMatrix, self).__init__()

   def forward(self, input):
     self.output = input
     return self.output

   def backward(self, input, gradOutput):
     self.gradInput = self.gradInput + gradOutput + input
     return self.gradInput

class StyleLoss(object):

    def __init__(self, strength):
      super(StyleLoss, self).__init__()
      self.strength = strength
      self.target = 0
      self.mode = None
      self.loss = 0
      self.gram = GramMatrix()
      self.blend_weight = None
      self.G = None

    def forward(self, input):
      print("StyleLoss - Forward")
      self.G = self.gram.forward(input)
      if self.mode == 'capture':
        print("StyleLoss - Forward - Capture")
        if self.blend_weight == None:
          self.target = self.G
        else:
          self.target = self.target + (self.blend_weight * self.G)
      elif self.mode == 'loss':
        print("StyleLoss - Forward - Loss")
        self.loss = self.strength * (self.G * self.target) #Forward
      self.output = input
      return self.output

    def backward(self, input, gradOutput):
      print("StyleLoss - Backward")
      if self.mode == 'loss':
        dG = self.gram.backward(self.G, self.target)
        self.gradInput = input * dG
        self.gradInput = self.gradInput * self.strength
        self.gradInput = self.gradOutput
      else: 
        print("StyleLoss - Backward - Capture")
        self.gradInput = gradOutput
      return self.gradInput



input_value = 1
gradOut_value = 0
weight = 5
CL = ContentLoss(weight)
SL = StyleLoss(weight)

CL.mode = 'capture'
CL.forward(input_value)

CL.mode = None
SL.mode = 'capture'
SL.forward(input_value)

CL.mode = 'loss'
SL.mode = 'loss'

CL.forward(input_value)
SL.forward(input_value)

CL.backward(input_value, gradOut_value)
SL.backward(input_value, gradOut_value)