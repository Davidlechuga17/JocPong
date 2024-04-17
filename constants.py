
class Constants():

    AMPLE_ESCENARI = 600

    ALCADA_ESCENARI = 400

    VERD = (0,255, 0)

    BLAU = (0, 0, 255)

    POSICIO_MARGE_DE_DALT = (0, 0, 600, 10)

    POSICIO_MARGE_DE_BAIX = (0, 390, 600, 10)

    #POSICIOJ1 = (10,180, 10, 40)
    #POSICIOJ2 = (580,180, 10,40)

    COLOR_J1 = (255, 0, 0)
    COLOR_J2= (85,0,255)

    def MovimentJugador1(teclas, pygame, jugador1):
        if teclas[pygame.K_w] and jugador1.posY>Constants.POSICIO_MARGE_DE_DALT[3]:
            jugador1.posY -= jugador1.vel

        if teclas[pygame.K_s] and jugador1.posY<Constants.ALCADA_ESCENARI-Constants.POSICIO_MARGE_DE_BAIX[3]-41:
            jugador1.posY += jugador1.vel

    def MovimentJugador2(teclas, pygame, jugador2):
        if teclas[pygame.K_UP] and jugador2.posY>Constants.POSICIO_MARGE_DE_DALT[3]:
            jugador2.posY -= jugador2.vel

        if teclas[pygame.K_DOWN] and jugador2.posY<Constants.ALCADA_ESCENARI-Constants.POSICIO_MARGE_DE_BAIX[3]-41:
            jugador2.posY += jugador2.vel



#MIDA_FINESTRA = pygame.display.set_mode((600, 400))

#COLOR_FONS_VERD = finestraJoc.fill((0,155, 0))

#MARGE_DE_DALT = pygame.draw.rect(finestraJoc, (0, 0, 255), (0, 0, 600, 10))

#MARGE_DE_BAIX =  pygame.draw.rect(finestraJoc, (0, 0, 255), (0, 390, 600, 10))



