import pygame,sys
from pygame.locals import *
from deck import Deck
from checker import WinChecker
from betting import*
from world import World
from Poker_bot import PokerBot
import random,time,math

#Defines constants
Players = []
PlayersInRound= []
playersImage=["player1.png","player2.png","player3.png","player4.png","player5.png","player6.png","player7.png"]
playerPositions=[[630,800],[200,750],[50,400],[150,50],[575,50],[1000,50],[1200,400],[1000,750]]
playerCardPositions=[[325,600],[200,400],[300,200],[575,200],[900,200],[1050,450],[900,600]]
showCardPositions=[[325,600],[200,400],[300,200],[575,200],[900,200],[975,400],[850,550]]
SCREEN_WIDTH=1350
SCREEN_HEIGHT=900
FRAME_RATE=60

#sets up pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
font= pygame.font.SysFont("freesanbold.ttf",32)
pygame.display.set_caption("Poker Game")

#sets up background screen
background_image= pygame.image.load("background.png")
world = World(background_image)

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
    
    def showAttributes(self,surface,playerPos): # shows the attributes of the players 
         currency = font.render("£"+str(self.currency), True,"blue")
         surface.blit(currency,(playerPos[self.position][0]-50,playerPos[self.position][1]-40))

         bet = font.render("bet: £"+str(self.bet), True,"blue")
         surface.blit(bet,(playerPos[self.position][0]+50,playerPos[self.position][1]-40))

    def showCards(self,surface,cardPos,roundNum,deckImage,showCardPos): #shows cards of players 
         
        if self.position == 0: #if it is the real player displays cards to the player 
          
          for i in range(len(self.hand)):
            if self.hand[i][0] == "C":
                image= pygame.image.load(deckImage[0][int(self.hand[i][1])-2])
            elif self.hand[i][0] == "D":
                image= pygame.image.load(deckImage[1][int(self.hand[i][1])-2])
            elif self.hand[i][0] == "H":
                image= pygame.image.load(deckImage[2][int(self.hand[i][1])-2])
            else:
                image= pygame.image.load(deckImage[3][int(self.hand[i][1])-2])
            surface.blit(image,(570 +i*110,550))
          
         
        if self.position != 0: # checks if it is an AI player 

            if roundNum<4: #checks if the round is still going and if it is it displays cards face down
               cardImage= pygame.image.load("cards.png")
               surface.blit(cardImage,(cardPos[self.position-1][0],cardPos[self.position-1][1]))

            elif roundNum>=4:#checks if the round is over and if it is it shows the cards of the AI 
                  for i in range(len(self.hand)):
                    if self.hand[i][0] == "C":
                        image= pygame.image.load(deckImage[0][int(self.hand[i][1])-2])
                    elif self.hand[i][0] == "D":
                        image= pygame.image.load(deckImage[1][int(self.hand[i][1])-2])
                    elif self.hand[i][0] == "H":
                        image= pygame.image.load(deckImage[2][int(self.hand[i][1])-2])
                    else:
                        image= pygame.image.load(deckImage[3][int(self.hand[i][1])-2])
                    surface.blit(image,(showCardPos[self.position-1][0] +i*110,showCardPos[self.position-1][1]))
                 

def showPot(surface,Pot): #displays the pot on the GUI
     potText = font.render("Pot: £"+str(Pot), True,"blue")
     surface.blit(potText,(650,500))

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
     
     

def main(): #runs the game

    #declares all the variables needed in the game
    pot=0
    rounds=0
    passes=0
    playerGo=0
    raiseRequired=0
    running = True
    winner=[]
    startRound0=True 
    startRound1=True
    startRound2=True
    startRound3=True
    ticker=0

    while running: 
         
        if rounds>=4 and ticker%10==0: # resets everything for new game 

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
            PlayersInRound[0].check=False
            PlayersInRound[0].Raise=False
            PlayersInRound[0].fold=False



        screen.fill("black")
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
        

        world.draw(screen,playersImage,playerPositions) #displays background images
        
        mouse_pos = pygame.mouse.get_pos() 


        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN: #checks if mouse is pressed 
                 
                 if foldButton_clicked(mouse_pos): #checks if the fold button is pressed
                     PlayersInRound[0].fold=True
                     PlayersInRound[0].check=False
                     PlayersInRound[0].Raise=False

                 if betButton_clicked(mouse_pos): #checks if the raise button is pressed
                     PlayersInRound[0].fold=False
                     PlayersInRound[0].check=False
                     PlayersInRound[0].Raise=True

                 if checkButton_clicked(mouse_pos): #checks if the check button is pressed
                     PlayersInRound[0].fold=False
                     PlayersInRound[0].check=True
                     PlayersInRound[0].Raise=False

            deck.ShowTableCards(screen) #displays the table cards on the GUI
            showPot(screen,pot) #displays the pot in the GUI

            for i in PlayersInRound: #displays all the players attributes on the GUI (bet, currency)
               i.showAttributes(screen,playerPositions)

            for i in PlayersInRound: #displays all the players cards on the GUI
               i.showCards(screen,playerCardPositions,rounds,deck.DeckImage,showCardPositions)

            if event.type == pygame.QUIT:
                    running = False
                    sys.exit()        
            pygame.display.update()

        if PlayersInRound[playerGo].position==0 and rounds<4: #checks real players decision
            
            #allows the player to check/call
            if  PlayersInRound[playerGo].check==True: 
                call(PlayersInRound[playerGo],raiseRequired)
                PlayersInRound[playerGo].check=False
                playerGo+=1

            #allows the player to raise 
            elif  PlayersInRound[playerGo].Raise==True:
                raiseRequired= Raise(PlayersInRound[playerGo],raiseRequired)
                PlayersInRound[playerGo].Raise=False
                playerGo+=1

            #allows the player to fold
            elif  PlayersInRound[playerGo].fold==True: 
                fold(PlayersInRound[playerGo],PlayersInRound,Players,pot)
                PlayersInRound[playerGo].fold=False

        elif PlayersInRound[playerGo].position!=0 and rounds<4 and ticker%3==0 and len(PlayersInRound)>1: #checks AI decision
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
        
        for i in PlayersInRound: #displays the players cards 
             i.showCards(screen,playerCardPositions,rounds,deck.DeckImage,showCardPositions)

        if rounds==4: #pauses game so players can see who won the round
            winner=(WinChecker(deck.Table,PlayersInRound))
            for i in winner: #adds pot to the currency of the winner(s) of the round
                PlayersInRound[i].currency= PlayersInRound[i].currency + int(math.ceil(pot/len(winner)))
            pot=0
            rounds+=1

        if rounds>=4: #pauses the game so that the player can see who wins and other players hands 
            time.sleep(1)

        
            
        ticker+=1



             
main()

    


         

