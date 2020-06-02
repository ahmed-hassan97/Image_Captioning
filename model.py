import torch
import torch.nn as nn
import torchvision.models as models


class EncoderCNN(nn.Module):
    def __init__(self, embed_size):
        super(EncoderCNN, self).__init__()
        resnet = models.resnet50(pretrained=True)
        for param in resnet.parameters():
            param.requires_grad_(False)
        
        modules = list(resnet.children())[:-1]
        self.resnet = nn.Sequential(*modules)
        self.embed = nn.Linear(resnet.fc.in_features, embed_size)

    def forward(self, images):
        #pretrained mode resnet
        features = self.resnet(images)
        features = features.view(features.size(0), -1)
        features = self.embed(features)
        return features
    

class DecoderRNN(nn.Module):
    def __init__(self, embed_size, hidden_size, vocab_size, num_layers=1):
        super(DecoderRNN, self).__init__()
        ## decode data
#         embed_size  = 512
#         hidden_size = 512

#         num_layers  =512
        self.embed_size = embed_size
        self.hidden_size = hidden_size
        self.vocab_size = vocab_size
        self.num_layers = num_layers
        
        self.embedding = nn.Embedding(vocab_size, embed_size)
        
        self.lstm = nn.LSTM(input_size=embed_size, hidden_size=hidden_size, num_layers=num_layers,                         batch_first=True)
        
        self.fc = nn.Linear(hidden_size, vocab_size)
        
        self.dropout = nn.Dropout(0.25)
       
    
    def forward(self, features, captions):
        
        #to embedding data into numeric
        
        captions = captions[:, :-1]
        
        

        captions = self.embedding(captions)
        
       

        features = features.unsqueeze(1)
        
        
        output, hidden = self.lstm(torch.cat((features, captions), dim=1))
        
        output = self.dropout(output)
        
        output = self.fc(output)
        
        return output
        

    def sample(self, inputs, states=None, max_len=25):
        
        " accepts pre-processed image tensor (inputs) and returns predicted sentence (list of tensor ids of length max_len) "
        
        sentence = []
        i = 0
        word_item = None
        
        while i < max_len:            
            # reached the <end> word
            if word_item == 1:
                break
            
            output, states = self.lstm(inputs, states)
            output = self.fc(output)
            
            _, word = output.max(2)
            
            word_item = word.item()
            sentence.append(word_item)
            
            inputs = self.embedding(word)
            
            i+=1
        
        return sentence
        