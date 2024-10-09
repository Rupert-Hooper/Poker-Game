import itertools,random

def BubbleSort(hand): # bubble sort to sort hands 
     swapped= True 
     buffer=[]
     i=0
     while i< len(hand)-1 and swapped == True:
         swapped = False
         for j in range(len(hand)-1):
             if hand[j][1]>hand[j+1][1]:
                 buffer = hand[j]
                 hand[j] = hand[j+1]
                 hand[j+1] = buffer
                 swapped = True
         i+=1
     return hand


def CheckFlush(hand): #returns true if hand is a flush
    Flush = True
    checker = hand[0][0]
    for i in range(1,len(hand)):
        if hand[i][0] != checker:
            Flush = False
    return Flush

def CheckStraight(hand): #returns true if hand is a straight
    Straight=True
    sortHand= BubbleSort(hand)
    if sortHand[0][1] == 2 and sortHand[4][1] ==14:
        sortHand.insert(0,sortHand[4])
        sortHand.pop(5)
    i=0
    while i < len(sortHand)-1 and Straight == True:
           if sortHand[i][1]+1 != sortHand[i+1][1]:
              if i!=0 or sortHand[i][1]!=14 or sortHand[i+1][1]!=2:
                Straight=False
           i+=1
    return Straight

def CheckFourOfaKind(hand): #returns true if hand has a four of a kind 
    Quad = False 
    i=0
    j=0
    k=0
    n=0
    while i<len(hand) and Quad ==False:
        j=0
        while j<len(hand) and Quad ==False:
            n=0
            while n<len(hand) and Quad ==False:
                k=0
                while k<len(hand) and Quad ==False:
                    if hand[i][1] == hand[j][1] == hand[n][1] == hand[k][1] and i!=j and i!=n and i!=k and k!=n and k!=j and j!=n:
                        Quad=True
                    k+=1
                n+=1
            j+=1
        i+=1
    return Quad

def CheckFullHouse(hand): #returns true if hand is a fullhouse 
    FullHouse=False
    i=0
    j=0
    n=0
    while i<len(hand) and FullHouse == False:
        j=0
        while j<len(hand) and FullHouse == False:
            n=0
            while n<len(hand) and FullHouse == False:
                if hand[i][1] == hand[j][1] == hand[n][1] and i!=j and i!=n and j!=n:
                    x=0
                    y=0
                    while x == i or x == j or x == n:
                        x+=1
                    while y == i or y == j or y == n or y == x:
                        y+=1
                    if hand[x][1]== hand [y][1]:
                        FullHouse = True
                n+=1
            j+=1
        i+=1
    return FullHouse

def CheckThreeOfaKind(hand): #returns true if hand has a three of a kind
    Trip = False 
    i=0
    j=0
    n=0
    while i<len(hand) and Trip ==False:
        j=0
        while j<len(hand) and Trip ==False:
            n=0
            while n<len(hand) and Trip ==False:
                if hand[i][1] == hand[j][1] == hand[n][1] and i!=j and i!=n and j!=n:
                    Trip=True   
                n+=1
            j+=1
        i+=1
    return Trip 

def CheckTwoPair(hand):#returns true if hand has two pairs
    TwoPair=False
    i=0
    j=0
    k=0
    n=0
    while i<len(hand) and TwoPair ==False:
        j=0
        while j<len(hand) and TwoPair ==False:
            n=0
            while n<len(hand) and TwoPair ==False:
                k=0
                while k<len(hand) and TwoPair ==False:
                    if hand[i][1] == hand[j][1] and hand[n][1] == hand[k][1] and i!=j and i!=n and i!=k and k!=n and k!=j and j!=n:
                        TwoPair=True
                    k+=1
                n+=1
            j+=1
        i+=1
                        
    return TwoPair

def CheckPair(hand): # returns true if hand has a pair 
    Pair= False
    i=0
    j=0
    while i<len(hand) and Pair == False:
        j=0
        while j<len(hand) and Pair == False:
            if hand[i][1] == hand[j][1] and i!=j:
                Pair = True
            j+=1
        i+=1
    return Pair
      
def AssignValueToHand(hand): #assigns a value to each hand
    HandValue=0 
    if CheckFlush(hand):
        if CheckStraight(hand):
              HandValue=9
        else:
            HandValue=6

    elif CheckFourOfaKind(hand):
        HandValue=8

    elif CheckFullHouse(hand):
        HandValue=7

    elif CheckStraight(hand):
        HandValue=5

    elif CheckThreeOfaKind(hand):
        HandValue=4
    
    elif CheckTwoPair(hand):
        HandValue=3
    
    elif CheckPair(hand):
        HandValue=2

    else:
        HandValue=1
    return HandValue

def SortedHand(hand,Value): #sorts inputed hand from least valuable card to most valuable card
    sortHand=[]

    if Value == 1 or Value == 6: #sorts hands that are flushes or high cards
       sortHand= BubbleSort(hand)
    
    elif Value == 5 or Value == 9: #sorts hands that are straights
        sortHand=BubbleSort(hand)
        if sortHand[0][1] == 2 and sortHand[4][1] ==14:
            sortHand.insert(0,sortHand[4])
            sortHand.pop(5)


    elif Value == 8: #sorts hands that are four of a kind
        i=0
        j=0
        k=0
        n=0
        Quad=False
        while i<len(hand) and Quad ==False:
            j=0
            while j<len(hand) and Quad ==False:
                n=0
                while n<len(hand) and Quad ==False:
                    k=0
                    while k<len(hand) and Quad ==False:
                        if hand[i][1] == hand[j][1] == hand[n][1] == hand[k][1] and i!=j and i!=n and i!=k and k!=n and k!=j and j!=n:
                            sortHand.append(hand[i])
                            sortHand.append(hand[j])
                            sortHand.append(hand[k])
                            sortHand.append(hand[n])
                            x=0
                            while x == i or x == j or x == n or x == k:
                                x+=1
                            sortHand.insert(0,hand[x])
                            Quad=True
                        k+=1
                    n+=1
                j+=1
            i+=1
        
    elif Value == 7 or Value == 4: #sorts hands that have three of a kind
        Trip = False 
        i=0
        j=0
        n=0
        while i<len(hand) and Trip ==False:
            j=0
            while j<len(hand) and Trip ==False:
                n=0
                while n<len(hand) and Trip ==False:
                    if hand[i][1] == hand[j][1] == hand[n][1] and i!=j and i!=n and j!=n:
                        sortHand.append(hand[i])
                        sortHand.append(hand[j])
                        sortHand.append(hand[n])
                        x=0
                        y=0
                        while x == i or x == j or x == n:
                            x+=1
                        while y == i or y == j or y == n or y == x:
                            y+=1
                        if hand[x][1] > hand [y][1]:
                            sortHand.insert(0,hand[x])
                            sortHand.insert(0,hand[y])
                        else:
                            sortHand.insert(0,hand[y])
                            sortHand.insert(0,hand[x])
                        Trip=True   
                    n+=1
                j+=1
            i+=1 

    elif Value == 3: #sorts hands that have two pairs
        TwoPair=False
        i=0
        j=0
        k=0
        n=0
        while i<len(hand) and TwoPair ==False:
            j=0
            while j<len(hand) and TwoPair ==False:
                n=0
                while n<len(hand) and TwoPair ==False:
                    k=0
                    while k<len(hand) and TwoPair ==False:
                        if hand[i][1] == hand[j][1] and hand[n][1] == hand[k][1] and i!=j and i!=n and i!=k and k!=n and k!=j and j!=n:
                            if hand[i][1] > hand[n][1]:
                                sortHand.append(hand[n])
                                sortHand.append(hand[k])
                                sortHand.append(hand[i])
                                sortHand.append(hand[j])
                            else:
                                sortHand.append(hand[i])
                                sortHand.append(hand[j])
                                sortHand.append(hand[k])
                                sortHand.append(hand[n])
                            x=0
                            while x == i or x == j or x == n or x == k:
                                x+=1
                            sortHand.insert(0,hand[x])
                            TwoPair=True
                        k+=1
                    n+=1
                j+=1
            i+=1
    
    elif Value == 2: #sorts hands that have a pair
        Pair= False
        i=0
        j=0
        Hand_1= BubbleSort(hand)
        while i<len(Hand_1) and Pair == False:
            j=0
            while j<len(Hand_1) and Pair == False:
                if Hand_1[i][1] == Hand_1[j][1] and i!=j:
                    Pair = True
                    sortHand.append(Hand_1[i])
                    sortHand.append(Hand_1[j])
                    x=0
                    y=0
                    z=0
                    while x == i or x == j:
                            x+=1
                    while y == i or y == j or y == x:
                            y+=1
                    while z == i or z == j or z == x or z == y:
                            z+=1
                    sortHand.insert(0,Hand_1[z])
                    sortHand.insert(0,Hand_1[y])
                    sortHand.insert(0,Hand_1[x])
                j+=1
            i+=1


    return sortHand

def compareSortedHands(SortedHand_1,SortedHand_2): #compares two sorted hands and outputs a value to indicate which is greater or if they are equal
    SortedHand_1Greater=-1
    i=0
    while i<len(SortedHand_1):
        if SortedHand_1[4-i][1]<SortedHand_2[4-i][1]:
            SortedHand_1Greater=0
            i=5
        elif SortedHand_1[4-i][1] > SortedHand_2[4-i][1]:
            SortedHand_1Greater=1
            i=5
        i=i+1
    return SortedHand_1Greater

def FindBestHand(TotalHand):#finds the best hand from a set of 7 cards (table plus player hand)
    allHands=list(itertools.combinations(TotalHand,5)) #makes a list of all the potential hands
    BestHand=list(allHands[0])
    BestHandValue=0

    for i in allHands: # loops through the list of potential hands and compares them to find which one is the best
        newHand=list(i)
        BestHandValue=AssignValueToHand(BestHand)
        newHandValue= AssignValueToHand(newHand)
        SortedBestHand=SortedHand(BestHand,BestHandValue)
        SortedNewHand=SortedHand(newHand,newHandValue)

        if BestHandValue < newHandValue:
            BestHand=newHand
            SortedBestHand=SortedHand(BestHand,BestHandValue)

        elif BestHandValue == newHandValue and compareSortedHands(SortedBestHand,SortedNewHand)==0:
            BestHand=newHand
            BestHandValue=AssignValueToHand(BestHand)
            SortedBestHand=SortedHand(BestHand,BestHandValue)
            
    return BestHandValue,SortedBestHand
   
def WinChecker(Table,players): #finds the winning player of the round
    TotalHand=Table
    for i in players: # loops through players finding each players best hand and assigning it to them
        TotalHand.append(i.hand[0])
        TotalHand.append(i.hand[1])
        i.BestHandValue,i.BestHand=FindBestHand(TotalHand)
        TotalHand.pop(5)
        TotalHand.pop(5)
    
    if len(players[0].BestHand)>0:
        start=0
    else:
        start=1

    Winners=[start]
    for j in range(start,len(players)): #compares best hands of each player to find which player(s) win
        if len(players[j].BestHand)>0:
                if players[j].BestHandValue == players[Winners[0]].BestHandValue:
                    if compareSortedHands(players[j].BestHand,players[Winners[0]].BestHand)==1:
                        for i in range(len(Winners)):
                            Winners.pop()
                        Winners.append(j)
                    elif  compareSortedHands(players[j].BestHand,players[Winners[0]].BestHand)==-1:
                        Winners.append(j)

                elif players[j].BestHandValue > players[Winners[0]].BestHandValue:
                    for i in range(len(Winners)):
                        Winners.pop()
                    Winners.append(j)
    return Winners