from deck import Deck
from checker import WinChecker
import random

# input data = [suit,val,suit,val,tableSuit,tableVal,tableSuit,tableVal,tableSuit,tableVal,potodds,Position on table]
# output data = [0/1/2] (fold/check/raise)

training_input="inputTrainingData.txt"
training_output="outputTraining.txt"
testing_input="extraInput.txt"
testing_output="extraOutput.txt"

class Player():  #creating the class player 
    def __init__(self):
        self.hand=[]
        self.BestHand=[]
        self.BestHandValue=0
       
                 
def numConverter(list):#converts letters into numbers 
    new_list=[]
    for i in list:
        if i == "C":
            new_list.append(1)
        elif i == "D":
            new_list.append(2)
        elif i == "H":
            new_list.append(3)
        elif i == "S":
            new_list.append(4)
        else:
            new_list.append(i)
    return new_list


def round0data(): #generates training data for the first round of betting 
    input_data=[]
    output_data=0

    #randomly generates the players position
    place= random.randint(1,7) 
    position= (place+1)/8

    #randomly generates the pot odds 
    bet= 400 
    pot= random.randint(6,8)*400 
    potOdds=bet/pot
    
    #generates the deck and players 
    player = [Player()]
    deck= Deck()
    deck.ShuffleDeck()

    #allocates one player a fixed hand 
    deck.DealCardsToPlayers(player)

    winNumber=0
    loops=100

    for i in range (loops): #simulates a round 100 times to see how many times the fixed hand player would win

        players = [Player(),Player(),Player(),Player(),Player()]
        deck.DealCardsToPlayers(players)
        allPlayers=[]

        #creates a list of all the players
        for i in players:
            allPlayers.append(i)
        allPlayers.append(player[0])
        
        deck.DealCardsToTable(5) #deals all the cards to the table 

        winner=WinChecker(deck.Table,allPlayers) #checks which player wins 
        for i in winner:
            if i == 5:
                winNumber=winNumber+1

        for i in deck.Table: #returns table cards to the deck
          deck.ShuffledDeck.append(i)

        for i in players: #returns players cards to the deck
           deck.ShuffledDeck.append(i.hand[0])
           deck.ShuffledDeck.append(i.hand[1])
        
        deck.ResetTable()
        deck.ResetPlayerCards(players)
        allPlayers=[]

    #enters the input data into the array for input data
    input_data.append(player[0].hand[0][0])
    input_data.append(player[0].hand[0][1])
    input_data.append(player[0].hand[1][0])
    input_data.append(player[0].hand[1][1])
    for i in range(10):
        input_data.append(0)
    input_data.append(potOdds)
    input_data.append(position)

    #calculates whether the player should check, raise or fold for the output data 
    print(winNumber)
    if winNumber/loops < potOdds: 
        output_data=0
    elif position <= 3/8: 
        if winNumber/loops-potOdds>0.1:
            output_data=2
        else:
            output_data=1

    elif 3/8 < position and position <=5/8:
      if winNumber/loops-potOdds>0.05:
            output_data=2
      else:
            output_data=1

    elif 5/8 < position and position <=1:
        if winNumber/loops-potOdds>0.025:
            output_data=2
        else:
            output_data=1

    input_data=numConverter(input_data)

    return input_data, output_data


def round1data(): #generates training data for the second round of betting 
    input_data=[]
    output_data=0

    #randomly generates the players position
    place= random.randint(1,7) 
    position= (place+1)/random.randint(place+1,8)

    #randomly generates the pot odds 
    bet= 400 
    pot= random.randint(8,20)*400 
    potOdds=bet/pot
    
    #generates the deck and players 
    player = [Player()]
    deck= Deck()
    deck.ShuffleDeck()

    #allocates one player a fixed hand 
    deck.DealCardsToPlayers(player)
    deck.DealCardsToTable(3)

    winNumber=0
    loops=100

    for i in range (loops): #simulates a round 100 times to see how many times the fixed hand player would win

        players = [Player(),Player(),Player(),Player(),Player(),Player(),Player()]
        deck.DealCardsToPlayers(players)
        allPlayers=[]

        #creates a list of all the players 
        for i in players: 
            allPlayers.append(i)
        allPlayers.append(player[0])
        
        deck.DealCardsToTable(2) #deals the rest of the cards to the table 

        winner=WinChecker(deck.Table,allPlayers)#checks which player wins 
        for i in winner:
            if i == 7:
                winNumber=winNumber+1

        for i in range(3,5): #returns table cards to the deck
          deck.ShuffledDeck.append(deck.Table[i])

        for i in players: #returns players cards to the deck
           deck.ShuffledDeck.append(i.hand[0])
           deck.ShuffledDeck.append(i.hand[1])
        
        deck.Table.pop(3)
        deck.Table.pop(3)
        deck.ResetPlayerCards(players)
        allPlayers=[]

    #enters the input data into the array for input data
    input_data.append(player[0].hand[0][0])
    input_data.append(player[0].hand[0][1])
    input_data.append(player[0].hand[1][0])
    input_data.append(player[0].hand[1][1])
    for i in deck.Table:
        input_data.append(i[0])
        input_data.append(i[1])

    for i in range(4):
        input_data.append(0)
    input_data.append(potOdds)
    input_data.append(position)

    #calculates whether the player should check, raise or fold for the output data 
    if winNumber/loops < potOdds: 
        output_data=0
    elif position <= 3/8: 
        if winNumber/loops-potOdds>0.1:
            output_data=2
        else:
            output_data=1

    elif 3/8 < position and position <=5/8:
      if winNumber/loops-potOdds>0.05:
            output_data=2
      else:
            output_data=1

    elif 5/8 < position and position <=1:
        if winNumber/loops-potOdds>0.025:
            output_data=2
        else:
            output_data=1

    input_data=numConverter(input_data)

    return input_data, output_data

def round2data(): #generates training data for the third round of betting 
    input_data=[]
    output_data=0

    #randomly generates the players position
    place= random.randint(1,7) 
    position= (place+1)/random.randint(place+1,8)

    #randomly generates the pot odds 
    bet= 400 
    pot= random.randint(8,25)*400 
    potOdds=bet/pot
    
    #generates the deck and players 
    player = [Player()]
    deck= Deck()
    deck.ShuffleDeck()

    #allocates one player a fixed hand 
    deck.DealCardsToPlayers(player)
    deck.DealCardsToTable(4)

    winNumber=0
    loops=100

    for i in range (loops): #simulates a round 100 times to see how many times the fixed hand player would win

        players = [Player(),Player(),Player(),Player(),Player(),Player(),Player()]
        deck.DealCardsToPlayers(players)
        allPlayers=[]

        #creates a list of all the players 
        for i in players:
            allPlayers.append(i)
        allPlayers.append(player[0])
        
        deck.DealCardsToTable(1) #deals the rest of the cards to the table 

        winner=WinChecker(deck.Table,allPlayers) #checks which player wins 
        for i in winner:
            if i == 7:
                winNumber=winNumber+1

        for i in range(4,5): #returns table cards to the deck
          deck.ShuffledDeck.append(deck.Table[i])

        for i in players: #returns players cards to the deck
           deck.ShuffledDeck.append(i.hand[0])
           deck.ShuffledDeck.append(i.hand[1])
        
        deck.Table.pop(4)
        deck.ResetPlayerCards(players)
        allPlayers=[]

    #enters the input data into the array for input data
    input_data.append(player[0].hand[0][0])
    input_data.append(player[0].hand[0][1])
    input_data.append(player[0].hand[1][0])
    input_data.append(player[0].hand[1][1])
    for i in deck.Table:
        input_data.append(i[0])
        input_data.append(i[1])

    for i in range(2):
        input_data.append(0)
    input_data.append(potOdds)
    input_data.append(position)

    #calculates whether the player should check, raise or fold for the output data 
    print(winNumber)
    if winNumber/loops < potOdds: 
        output_data=0
    elif position <= 3/8: 
        if winNumber/loops-potOdds>0.1:
            output_data=2
        else:
            output_data=1

    elif 3/8 < position and position <=5/8:
      if winNumber/loops-potOdds>0.05:
            output_data=2
      else:
            output_data=1

    elif 5/8 < position and position <=1:
        if winNumber/loops-potOdds>0.025:
            output_data=2
        else:
            output_data=1

    input_data=numConverter(input_data)

    return input_data, output_data

def round3data(): #generates training data for the fourth round of betting 
    input_data=[]
    output_data=0

    #randomly generates the players position
    place= random.randint(1,7) 
    position= (place+1)/random.randint(place+1,8)

    #randomly generates the pot odds 
    bet= 400 
    pot= random.randint(8,27)*400 
    potOdds=bet/pot
    
    #generates the deck and players 
    player = [Player()]
    deck= Deck()
    deck.ShuffleDeck()

    #allocates one player a fixed hand 
    deck.DealCardsToPlayers(player)
    deck.DealCardsToTable(5)

    winNumber=0
    loops=100

    for i in range (loops): #simulates a round 100 times to see how many times the fixed hand player would win

        players = [Player(),Player(),Player(),Player(),Player(),Player(),Player()]
        deck.DealCardsToPlayers(players)
        allPlayers=[]

        #creates a list of the rest of the players
        for i in players:
            allPlayers.append(i)
        allPlayers.append(player[0])

        winner=WinChecker(deck.Table,allPlayers) #checks which player wins
        for i in winner:
            if i == 7:
                winNumber=winNumber+1

        for i in players: #returns players cards to the deck
           deck.ShuffledDeck.append(i.hand[0])
           deck.ShuffledDeck.append(i.hand[1])
        
        deck.ResetPlayerCards(players)
        allPlayers=[]

    #enters the input data into the array for input data
    input_data.append(player[0].hand[0][0])
    input_data.append(player[0].hand[0][1])
    input_data.append(player[0].hand[1][0])
    input_data.append(player[0].hand[1][1])
    for i in deck.Table:
        input_data.append(i[0])
        input_data.append(i[1])

    input_data.append(potOdds)
    input_data.append(position)

    #calculates whether the player should check, raise or fold for the output data 
    print(winNumber)
    if winNumber/loops < potOdds: 
        output_data=0
    elif position <= 3/8: 
        if winNumber/loops-potOdds>0.1:
            output_data=2
        else:
            output_data=1

    elif 3/8 < position and position <=5/8:
      if winNumber/loops-potOdds>0.05:
            output_data=2
      else:
            output_data=1

    elif 5/8 < position and position <=1:
        if winNumber/loops-potOdds>0.025:
            output_data=2
        else:
            output_data=1

    input_data=numConverter(input_data)

    return input_data, output_data


input_list= []
output_list= []

#creates the training data 
for i in range(100):
    list1,list2 = round0data()
    input_list.append(list1)
    output_list.append(list2)


#enters the input data into an external text file 
File1= open(testing_input,"a")

for i in input_list:
    string=""
    for j in range(len(i)):
        if j==0:
            string="\n"+ string + str(i[j]) + ","
        elif j!=len(i)-1:
            string=string + str(i[j]) + ","
        else:
            string=string +str(i[j]) 
    File1.write(string)

File1.close()

#enters the expected output data into an external text file
File2=open(testing_output,"a")

for i in output_list:
    File2.write("\n" + str(i))

File2.close()


