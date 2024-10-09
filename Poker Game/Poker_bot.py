import torch
from Ai_bot import PokerBotNN

input_size = 17
layer_size = 128
output_size = 3

# Instantiate the model again
model = PokerBotNN(input_size, layer_size, output_size)

# Load the saved weights into the model
model.load_state_dict(torch.load('poker_bot_model.pth'))

# Set the model to evaluation mode if you're making predictions
model.eval()

def PokerBot(input): #runs the bot to make a decision in the game
     #Converts input to tensor and adds batch dimension
     input_tensor = torch.tensor(input, dtype=torch.float32).unsqueeze(0)
     
     #set the model to evaluation mode
     model.eval()

     #disables gradient calculation
     with torch.no_grad(): 
          output=model(input_tensor)#completes a forward pass to get an output

     
     decision = torch.argmax(output, dim=1) #gets the output  

     return decision