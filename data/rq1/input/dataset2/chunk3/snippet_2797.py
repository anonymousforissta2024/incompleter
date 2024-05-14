#Source: https://stackoverflow.com/questions/67504836/pythonpytorch-typeerror-string-indices-must-be-integers
TRANSFORMERS = {
    "bert-multi-cased": (BertModel, BertTokenizer, "bert-base-uncased"),
}

class Transformer(nn.Module):
    def __init__(self, model, num_classes=1):
        """
        Constructor
    
    Arguments:
        model {string} -- Transformer to build the model on. Expects "camembert-base".
        num_classes {int} -- Number of classes (default: {1})
    """
    super().__init__()
    self.name = model

    model_class, tokenizer_class, pretrained_weights = TRANSFORMERS[model]

    bert_config = BertConfig.from_json_file(MODEL_PATHS[model] + 'bert_config.json')
    bert_config.output_hidden_states = True
    
    self.transformer = BertModel(bert_config)

    self.nb_features = self.transformer.pooler.dense.out_features

    self.pooler = nn.Sequential(
        nn.Linear(self.nb_features, self.nb_features), 
        nn.Tanh(),
    )

    self.logit = nn.Linear(self.nb_features, num_classes)

def forward(self, tokens):
    """
    Usual torch forward function
    
    Arguments:
        tokens {torch tensor} -- Sentence tokens
    
    Returns:
        torch tensor -- Class logits
    """
    _, _, hidden_states = self.transformer(
        tokens, attention_mask=(tokens > 0).long()
    )

    hidden_states = hidden_states[-1][:, 0] # Use the representation of the first token of the last layer

    ft = self.pooler(hidden_states)

    return self.logit(ft)