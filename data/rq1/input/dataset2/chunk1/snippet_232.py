#Source: https://stackoverflow.com/questions/54053256/pytorch-attributeerror-cannot-assign-module-before-module-init-call-even
class ResNetGenerator(nn.Module):
    def __init__(self, input_nc=3, output_nc=3, n_residual_blocks=9, use_dropout=False):
        # super(ResNetGenerator, self).__init__()
        super().__init__()