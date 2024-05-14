#Source: https://stackoverflow.com/questions/74859282/got-typeerror-when-adding-return-indices-true-to-nn-maxpool2d-in-pytorch
# B = Batch size
# decoder (B, 8) => (B, 3, 224, 224)
class Decoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.decoder_fc = nn.Sequential(
            nn.Linear(8, 1024),
            nn.ReLU(True),
            nn.Linear(1024, 64*7*7),
            nn.ReLU(True)
        )
        self.unflat = nn.Unflatten(dim=1, unflattened_size=(64, 7, 7))
        self.decoder_cnn = nn.Sequential(
            nn.MaxUnpool2d(2),
            nn.BatchNorm2d(64),
            nn.ConvTranspose2d(64, 32, kernel_size=3, stride=2, padding=1),
            nn.ReLU(True),
            nn.ConvTranspose2d(32, 16, kernel_size=3, stride=2, padding=1),
            nn.MaxUnpool2d(2),
            nn.BatchNorm2d(16),
            nn.ReLU(True),
            nn.ConvTranspose2d(16, 8, kernel_size=3, stride=2, padding=0),
            nn.ReLU(True),
            nn.ConvTranspose2d(8, 3, kernel_size=3, stride=1, padding=0)
        )
    def forward(self, x):
        x = self.decoder_fc(x)
        x = self.unflat(x)
        x = self.decoder_cnn(x)
        return x