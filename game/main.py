from fight import Fight
from bojovnik import Bojovnik
import pygame
if __name__=="__main__":
    #boj1=Bojovnik("Kárl",15,8,100)
    #boj2=Bojovnik("Chábr",12,15,80)
    #souboj=Fight(boj1,boj2)
    #souboj.process(100) # Random value podle ktere se pocita sance na utok prvniho nebo druheho bojovnika
    pygame.init()
    
    #maimenu
    width,height = 1280, 720
    gameScreen = pygame.image.load("img/GAMEscreen.png")
    mainMenu = pygame.image.load("img/mainmenu.png")
    mainSurface = pygame.display.set_mode((width, height))
    pygame.display.set_caption("hra lol")
    mainSurface.blit(mainMenu, (0,0))
    
    #vars
    currentScreen = "mainMenu"

    #cudliky
    red = pygame.image.load('img/red.png')
    green = pygame.image.load('img/green.png')
    widthButton, heightButton = 330, 50

    #strat cudl
    startHry = pygame.Rect(135,240,widthButton,heightButton)
    backButton = pygame.Rect(0,0,widthButton-200,heightButton)
    redButton = pygame.transform.scale(red, (widthButton, heightButton))
    greenButton = pygame.transform.scale(green, (widthButton, heightButton))

    #while
    opened = True
    while opened:
        a,b = pygame.mouse.get_pos()
        if currentScreen == "mainMenu":
            if startHry.x <= a <= startHry.x + widthButton and startHry.y <= b <= startHry.y + heightButton:
                mainSurface.blit(redButton, (135, 240))
            elif currentScreen:
                mainSurface.blit(greenButton, (135, 240))
        elif currentScreen == "game":
            if backButton.x <= a <= backButton.x + widthButton-200 and backButton.y <= b <= backButton.y + heightButton:
                mainSurface.blit(redButton, (-200, 0))
            elif currentScreen:
                mainSurface.blit(greenButton, (-200, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                opened = False
            # KLIK NA CUDL
            if event.type == pygame.MOUSEBUTTONDOWN:
                if currentScreen == "mainMenu":
                    if startHry.collidepoint(event.pos):
                        mainSurface.blit(gameScreen, (0,0))
                        currentScreen = "game"
                elif currentScreen == "game":
                    if backButton.collidepoint(event.pos):
                        mainSurface.blit(mainMenu, (0,0))
                        currentScreen = "mainMenu"
#                if startHry.collidepoint(event.pos):
#                    if currentScreen == "mainMenu":
#                        mainSurface.blit(gameScreen, (0,0))
#                        currentScreen = "game"
#                    elif currentScreen == "game":
#                       mainSurface.blit(mainMenu, (0,0))
#                        currentScreen = "mainMenu"

        pygame.display.update()
