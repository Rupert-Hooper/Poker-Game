
from deck import Deck
from checker import WinChecker
from betting import*
from Poker_bot import PokerBot
import math

#Defines constants
Players = []
PlayersInRound= []


class Player():  #creating the class player 
    def __init__(self):
        self.hand=[]
        self.BestHand=[]
        self.BestHandValue=0
        self.currency=10000
        self.bet=0
        self.decision=""
        self.check=False
        self.Raise=False
        self.fold=False
        self.position= 0
    

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
         

PlayersInRound = [Player(),Player(),Player(),Player(),Player(),Player(),Player(),Player()] #creates a list of 8 players in a round 

deck=Deck() # instantiates the deck

for i in range(len(PlayersInRound)): # assigns each player a position on the table 
     PlayersInRound[i].position=i
     
InputData=[[],[],[],[],[],[],[],[]]
OutputData=[[],[],[],[],[],[],[],[]]


     

def main(): #runs the game

    #declares all the variables needed in the game
    pot=0
    rounds=0
    passes=0
    playerGo=0
    raiseRequired=0
    winner=[]
    startRound0=True 
    startRound1=True
    startRound2=True
    startRound3=True
  

    for x in range(2000): 
         
        if rounds>=4: # resets everything for new game 

            for i in range(len(PlayersInRound)): #removes players from round and puts them all in a separate list
                   Players.append(PlayersInRound[0])
                   PlayersInRound.pop(0)
            
            for i in range(0,len(Players)): #returns players all back to list of players in the round all in order
                for j in Players:
                    if j.position==i:
                        j.bet=0 
                        PlayersInRound.append(j)
            
            for i in range(len(Players)):#resets list of players not in round
                 Players.pop()

            #resets everything so it is how it was at the start of the game 
            deck.ResetTable()
            deck.ResetPlayerCards(PlayersInRound)
            deck.ResetDeck()
            rounds=0
            startRound0=True 
            startRound1=True
            startRound2=True
            startRound3=True
            pot=0
            playerGo=0
            raiseRequired=0

        if rounds==0 and startRound0==True:#starts the first round of betting 
            deck.ShuffleDeck()
            deck.DealCardsToPlayers(PlayersInRound)
            startRound0=False
            
        
        if rounds==1 and startRound1==True:#starts the second round of betting
            deck.DealCardsToTable(3)
            startRound1=False
            raiseRequired=0

        if rounds==2 and startRound2==True:#starts the third round of betting
            deck.DealCardsToTable(1)
            startRound2=False
            raiseRequired=0
        
        if rounds==3 and startRound3==True:#starts the fourth round of betting 
            deck.DealCardsToTable(1)
            startRound3=False
            raiseRequired=0
        

        if rounds<4 and len(PlayersInRound)>1: #checks AI decision
            #generates inputs for the AI bot
            inputs=[]
            for i in PlayersInRound[playerGo].hand:
                inputs.append(i[0])
                inputs.append(i[1])

            for i in deck.Table:
                inputs.append(i[0])
                inputs.append(i[1])

            while len(inputs)<14:
                inputs.append(0)
 
            if pot== 0:
                inputs.append(1/8)
            else:
                inputs.append(400/pot)

            inputs.append((playerGo+1)/len(PlayersInRound))
            inputs.append(len(PlayersInRound))
       
            inputs= numConverter(inputs)
            #obtains an output from the AI
            decision = PokerBot(inputs)

            InputData[PlayersInRound[playerGo].position].append(inputs)
            #print(InputData)
            OutputData[PlayersInRound[playerGo].position].append(decision.item())


            #checks the AIs decision and allows them to check,raise or fold accordingly
            if decision == 1: 
                call(PlayersInRound[playerGo],raiseRequired)
                playerGo+=1
            elif decision == 0:
                fold(PlayersInRound[playerGo],PlayersInRound,Players,pot)

            else:
                raiseRequired= Raise(PlayersInRound[playerGo],raiseRequired)
                playerGo+=1
            

        if betsEqual(PlayersInRound) == False and playerGo == len(PlayersInRound): #returns the index to the start of the list of players if the round is still going 
                playerGo=0
                passes= passes+1
        

        if betsEqual(PlayersInRound) == True and playerGo == len(PlayersInRound) or len(PlayersInRound)==1: #ends the round of betting 
                playerGo=0
                rounds=rounds+1
                passes=0
                pot=pot +totalBets(PlayersInRound)

                
        elif betsEqual(PlayersInRound) == True and passes>=1 or len(PlayersInRound)==1: #ends the round of betting 
                playerGo=0
                rounds=rounds+1
                passes=0
                pot=pot +totalBets(PlayersInRound)
        

        if rounds==4: #pauses game so players can see who won the round
            winner=(WinChecker(deck.Table,PlayersInRound))
            for i in winner: #adds pot to the currency of the winner(s) of the round
                PlayersInRound[i].currency= PlayersInRound[i].currency + int(math.ceil(pot/len(winner)))
            pot=0
            rounds+=1


main()


#checks which AI performed the best
bestCurrency=0
for i in range(len(PlayersInRound)): 
    if PlayersInRound[i].currency>PlayersInRound[bestCurrency].currency:
        bestCurrency=i


trainingInput= ("SelfInputBatch1.txt")
trainingOutput= ("SelfOutputBatch1.txt")
trainingInput2= ("SelfInputBatch2.txt")
trainingOutput2= ("SelfOutputBatch2.txt")

#enters the input data into an external text file 
File1= open(trainingInput2,"a")

for i in InputData[bestCurrency]:
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
File2=open(trainingOutput2,"a")

for i in OutputData[bestCurrency]:
    File2.write("\n" + str(i))

File2.close()
            
            
        
        

        

             


    


         

