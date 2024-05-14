#Source: https://stackoverflow.com/questions/64429461/typeerror-iteration-over-a-0-d-tensor
print(len(train_ds)) # 44
print(len(valid_ds)) # 22


class LSTMClassifier(nn.Module):

    def __init__(self, embed_size, hidden_size, vocab_size, num_layers, num_classes, batch_size):
        super(LSTMClassifier, self).__init__()

        self.embed_size = embed_size
        self.hidden_size = hidden_size
        self.batch_size = batch_size
        self.num_layers = num_layers
        self.embedding = nn.Embedding(vocab_size, embed_size) # a lookup table

        self.lstm = nn.LSTM(embed_size, hidden_size, num_layers, dropout=0.3, bidirectional=True)

        self.fc = nn.Sequential(
            nn.Linear(2*hidden_size, 100),
            nn.ReLU(),
            nn.Dropout(p=0.2),
            nn.Linear(100, num_classes)
        )

        self.hidden = self.init_hidden()

    def init_hidden(self):
        h = to_var(torch.zeros((2*self.num_layers, self.batch_size, self.hidden_size)))
        c = to_var(torch.zeros((2*self.num_layers, self.batch_size, self.hidden_size)))
        return h, c

    def forward(self, x):
        x = self.embedding(x)
        x, self.hidden = self.lstm(x, self.hidden)
        x = self.fc(x[-1]) # select the last output
        return x