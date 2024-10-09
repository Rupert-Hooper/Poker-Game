import random,time


def betButton_clicked(mouse_pos):#checks if the raise button is clicked 
    xpos= 765
    ypos= 800
    width=171
    height=57
    if xpos < mouse_pos[0] < xpos + width and ypos < mouse_pos[1] < ypos + height:
        return True
    else:
        return False

def checkButton_clicked(mouse_pos):#checks if the check button is clicked 
    xpos= 595
    ypos= 800
    width=170
    height=57
    if xpos < mouse_pos[0] < xpos + width and ypos < mouse_pos[1] < ypos + height:
        return True
    else:
        return False

def foldButton_clicked(mouse_pos):#checks if the fold button is clicked 
    xpos= 420
    ypos= 800
    width=171
    height=57
    if xpos < mouse_pos[0] < xpos + width and ypos < mouse_pos[1] < ypos + height:
        return True
    else:
        return False


def call(player,raiseNeeded): #makes the players bet equal to the required bet and takes it away from their total currency
    if player.bet < raiseNeeded:
        player.currency = player.currency+ player.bet-raiseNeeded
        player.bet= raiseNeeded


def fold(player,players,playersOut,pot):#removes player from the game
    pot=pot + player.bet
    player.bet=0
    playersOut.append(player)
    players.remove(player)
    

def Raise(player,raiseNeeded): # allows player to raise the amount being bet in a round 
    player.bet = player.bet+ 400
    player.currency = player.currency -player.bet
    raiseNeeded = player.bet
    
    return raiseNeeded
    

def totalBets(players): #totals up the all the bets from a round
    total=0
    for i in players:
        total=total+i.bet
        i.bet = 0 
    return total

def betsEqual(players): #checks if every players bet is equal
    betsEqual=True
    bet=players[0].bet
    for i in players:
       if bet != i.bet:
           betsEqual=False
    return betsEqual
        


        
            




