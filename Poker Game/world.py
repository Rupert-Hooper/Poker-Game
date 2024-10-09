import pygame

class World(): #class to draw background of game
    def __init__(self, map_image):
        self.image = map_image
        self.Bet = "betButton.png"
        self.Fold = "foldButton.png"
        self.Check = "checkButton.png"
    
    def draw(self,surface,playersImage,playerPos): #draws background and players
        surface.blit(self.image,(0,0))
        bet= pygame.image.load(self.Bet)
        check= pygame.image.load(self.Check)
        fold= pygame.image.load(self.Fold)
        surface.blit(bet,(765,800))
        surface.blit(check,(595,800))
        surface.blit(fold,(420,800))

    
        for i in range(len(playersImage)):
            image= pygame.image.load(playersImage[i])
            surface.blit(image,(playerPos[i+1][0],playerPos[i+1][1]))



        

   