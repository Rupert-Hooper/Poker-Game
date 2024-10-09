import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as function
from torch.utils.data import Dataset, DataLoader

training_input="inputTrainingData.txt"
training_output="outputTraining.txt"
testing_input="extraInput.txt"
testing_output="extraOutput.txt"
selfinput1= "SelfInputBatch1.txt"
selfoutput1= "SelfOutputBatch1.txt"
selfinput2= ("SelfInputBatch2.txt")
selfoutput2= ("SelfOutputBatch2.txt")


class PokerDataset(Dataset):
    
    def __init__(self,input_file, label_file):
            #Load the data from the file
            self.inputs= []
            with open(input_file, "r") as file:
                 for line in file:
                      values= list(map(float, line.strip().split(",")))# split data by commas and convert into a float
                      self.inputs.append(torch.tensor(values)) # Store each line as a tensor 

            self.labels=[]
            with open(label_file,"r") as file:
                 for line in file:
                      label = int(line.strip()) #convert labels to integers
                      self.labels.append(torch.tensor(label, dtype=torch.long)) #store as a tensor of type long
                     
    
    def __len__(self):#returns number of samples
         return len(self.inputs)
    
    def __getitem__(self, index): #returns the input features and labels at a given index
         return self.inputs[index], self.labels[index]


class PokerBotNN(nn.Module): # Defines the neural network for the poker bot 

    def __init__(self,inputSize,layerSize,outputSize):
        super(PokerBotNN,self).__init__()
        self.l1 = nn.Linear(inputSize,layerSize) # first layer of nn
        self.l2 = nn.Linear(layerSize,layerSize) # second layer of nn
        self.l3 = nn.Linear(layerSize,outputSize) # third layer of nn

    def forward(self,out): #passes data through the neural network to get an output 
        out = function.relu(self.l1(out)) #relu activation function on first layer
        out = function.relu(self.l2(out)) #relu activation function on second layer
        out = self.l3(out) #output layer
        return out
    
input_size = 17
layer_size = 128
output_size = 3

dataset= PokerDataset(selfinput2, selfoutput2) #creates dataset to input into neural network

#Uses DataLoader to handle batching and shuffling
batch_size=input_size
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

model= PokerBotNN(input_size,layer_size,output_size) #instantiates the PokerBot nn
criterion= nn.CrossEntropyLoss() # loss function
optimizer=optim.Adam(model.parameters(), lr=0.001) #optimizer to update weights of the neural network
 
# Load the saved weights into the model
model.load_state_dict(torch.load('poker_bot_model.pth'))
 
epochs=100
for epoch in range(epochs):
    for inputs,labels in dataloader: #iterates through inputs
        outputs = model(inputs) # completes a forward pass on the data
        loss = criterion(outputs,labels) #calculates the loss of the data

    #carries out a backward pass on the data 
    optimizer.zero_grad() 
    loss.backward()
    optimizer.step()

    #prints the loss for every epoch
    if epoch % 10 ==0:
        print(f'Epoch [{epoch}/{epochs}], Loss: {loss.item():.4f}')

    torch.save(model.state_dict(), 'poker_bot_model.pth') 

#stores weights for the neural network
torch.save(model.state_dict(), 'poker_bot_model.pth')  


    