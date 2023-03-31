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
    mainSurface = pygame.display.set_mode((width, height))
    pygame.display.set_caption("hra lol")
    mainMenu = pygame.image.load('img/mainmenu.png')
    mainSurface.blit(mainMenu, (0,0))
    
    #cudliky
    red = pygame.image.load('img/red.png')
    green = pygame.image.load('img/green.png')
    widthButton, heightButton = 330, 50
    #strat cudl
    startHry = pygame.Rect(135,240,widthButton,heightButton)
    startHryIMG = pygame.transform.scale(red, (widthButton, heightButton))
    startHryIMGNajeto = pygame.transform.scale(green, (widthButton, heightButton))

    #while
    opened = True
    while opened:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                opened = False
            # KLIK NA CUDL
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startHry.collidepoint(event.pos):
                    print("posunu se do char creatu")
            # druha moznost LOAD?
            # na vic cudliku jsem uz linej
        a,b = pygame.mouse.get_pos()
        if startHry.x <= a <= startHry.x + widthButton and startHry.y <= b <= startHry.y + heightButton:
            mainSurface.blit(startHryIMG, (135, 240))
        else:
            mainSurface.blit(startHryIMGNajeto, (135, 240))



        pygame.display.update()
