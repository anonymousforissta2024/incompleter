#Source: https://stackoverflow.com/questions/75581482/how-to-resolve-batchlabel-name-torch-tensorbatchlabel-name-dtype-torch-i
class BERT_CRF(nn.Module):
    

    def __init__(self, bert_model, num_labels):
       
        super(BERT_CRF, self).__init__()
        self.bert = bert_model
        self.config = self.bert.config
        self.dropout = nn.Dropout(0.25)     
        self.classifier = nn.Linear(768, num_labels)
        self.crf = CRF(num_labels, batch_first=True)

    def forward(self, input_ids, attention_mask, labels=None, token_type_ids=None):
        outputs = self.bert(input_ids, attention_mask=attention_mask)
       

        sequence_output = torch.stack((outputs[1][-1], outputs[1][-2], outputs[1][-3], outputs[1][-4])).mean(dim=0)
        
        sequence_output = self.dropout(sequence_output)
      
        emission = self.classifier(sequence_output)  # [32,256,17]

        labels = labels.reshape(attention_mask.size()[0], attention_mask.size()[1])
      

        if labels is not None:
        
            loss = -self.crf(log_soft(emission, 2), labels, mask=attention_mask.type(torch.uint8), reduction='mean')
       
            prediction = self.crf.decode(emission, mask=attention_mask.type(torch.uint8))
          
            print([loss, prediction])
            return [loss, prediction]

        else:
      
            prediction = self.crf.decode(emission, mask=attention_mask.type(torch.uint8))
            return prediction