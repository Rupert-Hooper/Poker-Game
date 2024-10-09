import random, pygame

pygame.init()

class Deck (): #creating the class deck 
    def __init__ (self): #creating the constructor for the deck
        self.OriginalDeck = [["H",14],["H",13],["H",12],["H",11],["H",10],["H",9],["H",8],["H",7],["H",6],["H",5],["H",4],["H",3],["H",2], #creates a 2D list of a deck of cards
                              ["D",14],["D",13],["D",12],["D",11],["D",10],["D",9],["D",8],["D",7],["D",6],["D",5],["D",4],["D",3],["D",2],
                              ["C",14],["C",13],["C",12],["C",11],["C",10],["C",9],["C",8],["C",7],["C",6],["C",5],["C",4],["C",3],["C",2],
                              ["S",14],["S",13],["S",12],["S",11],["S",10],["S",9],["S",8],["S",7],["S",6],["S",5],["S",4],["S",3],["S",2],] 
        self.ShuffledDeck = [] #empty list that cards can be appended randomly to, to create a shuffled deck
        self.Table=[]
        self.DeckImage = [["2C.png","3C.png","4C.png","5C.png","6C.png","7C.png","8C.png","9C.png","10C.png","11C.png","12C.png","13C.png","14C.png"],
                          ["2D.png","3D.png","4D.png","5D.png","6D.png","7D.png","8D.png","9D.png","10D.png","11D.png","12D.png","13D.png","14D.png"],
                          ["2H.png","3H.png","4H.png","5H.png","6H.png","7H.png","8H.png","9H.png","10H.png","11H.png","12H.png","13H.png","14H.png"],
                          ["2S.png","3S.png","4S.png","5S.png","6S.png","7S.png","8S.png","9S.png","10S.png","11S.png","12S.png","13S.png","14S.png",]]

    def ShuffleDeck (self): # creates a shuffled deck and stores it in shuffled deck, by appending cards to shuffled deck in a random order
        for i in range(len(self.OriginalDeck)): 
            index= random.randint(0,len(self.OriginalDeck)-1) 
            self.ShuffledDeck.append(self.OriginalDeck[index]) 
            self.OriginalDeck.pop(index) 
        self.OriginalDeck = [["H",14],["H",13],["H",12],["H",11],["H",10],["H",9],["H",8],["H",7],["H",6],["H",5],["H",4],["H",3],["H",2], 
                              ["D",14],["D",13],["D",12],["D",11],["D",10],["D",9],["D",8],["D",7],["D",6],["D",5],["D",4],["D",3],["D",2],
                              ["C",14],["C",13],["C",12],["C",11],["C",10],["C",9],["C",8],["C",7],["C",6],["C",5],["C",4],["C",3],["C",2],
                              ["S",14],["S",13],["S",12],["S",11],["S",10],["S",9],["S",8],["S",7],["S",6],["S",5],["S",4],["S",3],["S",2],] 
        
    def ResetDeck (self): #resets the deck 
        self.ShuffledDeck=[]

    def ResetPlayerCards(self,players): #resets all the players hands
            for i in players:  
                i.hand=[]                  

    def DealCardsToPlayers(self,players): #deals cards randomly out to each player
        for i in range(len(players)):  
            for j in range (2): 
                index = random.randint(0,len(self.ShuffledDeck)-1) 
                players[i].hand.append(self.ShuffledDeck[index]) 
                self.ShuffledDeck.pop(index) 


    def DealCardsToTable(self,numCards): #deals a chosen number of cards randomly out to the table 
        for i in range(0,numCards): 
            index = random.randint(0,len(self.ShuffledDeck)-1) 
            self.Table.append(self.ShuffledDeck[index]) 
            self.ShuffledDeck.pop(index)  
    
    def ResetTable(self): #resets the table 
       self.Table=[]


    def ShowTableCards(self,surface): #displays the table cards as imgages on the GUI
        
        for i in range(len(self.Table)):
            if self.Table[i][0] == "C":
                image= pygame.image.load(self.DeckImage[0][int(self.Table[i][1])-2])
            elif self.Table[i][0] == "D":
                image= pygame.image.load(self.DeckImage[1][int(self.Table[i][1])-2])
            elif self.Table[i][0] == "H":
                image= pygame.image.load(self.DeckImage[2][int(self.Table[i][1])-2])
            else:
                image= pygame.image.load(self.DeckImage[3][int(self.Table[i][1])-2])
            surface.blit(image,(420+i*110,370))
            
