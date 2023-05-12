import pygame
from settings import *
from routes import *

from fireBall import BolaFuego
from magician import Mago
from enemyMagician import MagoEnemigo
from soldier import Soldado

pygame.init()
pygame.mixer.init()

# Configuración de la ventana
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Magician Survives")

# Crear instancia del mago
mago = Mago()

fuego = []
magosenemigos = []
soldadosenemigos = []
fuegoEnemigo = []

space_key_down = False

#region
MAGICIAN_FRONT.convert_alpha()
MAGICIAN_WALK_DE1.convert_alpha()
MAGICIAN_WALK_DE2.convert_alpha()
MAGICIAN_WALK_IZ1.convert_alpha()
MAGICIAN_WALK_IZ2.convert_alpha()
MAGICIAN_ATACK_FRONT1.convert_alpha()
MAGICIAN_ATACK_FRONT2.convert_alpha()
MAGICIAN_ATACK_DE1.convert_alpha()
MAGICIAN_ATACK_DE2.convert_alpha()
MAGICIAN_ATACK_IZ1.convert_alpha()
MAGICIAN_WALK_IZ2.convert_alpha() 
#endregion

#Constanes Spaw
spawmago = 1000
spawSoldao = 1000

#Variables Spaw
timeMago = spawmago
ultimoMago = 0
timeSoldao = spawSoldao
ultimoSoldao = 0

#Musiquita
pygame.mixer.music.play(-1)
DERROTA = pygame.USEREVENT+1

#Variable Derrota
perdiste = False

# Bucle principal
while True:
    
    reloj = pygame.time.Clock()

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        #Derrota
        if (event.type == DERROTA):
            if(CANAL1.get_busy() or CANAL1.get_queue()!=None):
                break

            #Salir
            pygame.quit()
            quit()

    if(perdiste): continue

    #Spaw enemigos
    if(timeMago -ultimoMago >= spawmago):
        ultimoMago = pygame.time.get_ticks()
        timeMago = 0
        magosenemigos.append(MagoEnemigo(mago))
    else:
        timeMago = pygame.time.get_ticks()

    if(timeSoldao -ultimoSoldao >= spawSoldao):
        ultimoSoldao = pygame.time.get_ticks()
        timeSoldao = 0
        soldadosenemigos.append(Soldado(mago))
    else:
        timeSoldao = pygame.time.get_ticks()

    # Obtener el estado actual del teclado
    keys = pygame.key.get_pressed()

    # Mover al mago según la tecla presionada
    if keys[pygame.K_RIGHT]:
        mago.moverDerecha()
    elif keys[pygame.K_LEFT]:
        mago.moverIzquierda()
    elif keys[pygame.K_UP]:
        mago.mirarArriba()

    if keys[pygame.K_SPACE] and not space_key_down:
        mago.atacar()
        bolaF = BolaFuego(mago)
        fuego.append(bolaF)
        bolaF.reproducirSonido(FIREBALL_SOUNDS[0])
        space_key_down = True
    elif not keys[pygame.K_SPACE]:
        space_key_down = False


    # Actualizar estado del mago
    for i in magosenemigos:
        i.limites()

    for i in soldadosenemigos:
        i.limites()

    mago.limites()

    
    #Movimiento enemigos
    for i in magosenemigos:
        i.moverse(mago)

    for i in soldadosenemigos:
        i.perseguir(mago)

    #Disparo de magos enemigos
    for i in magosenemigos:
        if(int(i.current_sprite_index) != i.current_sprite_aux and i.atacando and i.current_sprite_aux ==0):
            bolaF = BolaFuego(i)
            fuegoEnemigo.append(bolaF)
            bolaF.reproducirSonido(ENEMY_MAGICIAN_SOUNDS[0])
            i.atacando = False
        i.current_sprite_aux = int(i.current_sprite_index)
    
    #Disparos del Mago
    for i in fuego: 
        i.trayectoria()
        for j in magosenemigos:
            if(j.rect().colliderect(i.rect())):
                i.reproducirSonido(FIREBALL_SOUNDS[1])
                fuego.remove(i)
                magosenemigos.remove(j)
                break

        
        for j in soldadosenemigos:
            if(j.rect().colliderect(i.rect())):
                i.reproducirSonido(FIREBALL_SOUNDS[1])  
                fuego.remove(i)
                soldadosenemigos.remove(j)
                break

    # Ataques Enemigos
    for i in fuegoEnemigo:
        i.trayectoria()    
        if(mago.rect().colliderect(i.rect())):
            fuegoEnemigo.remove(i)
            perdiste = True
            pygame.mixer.music.stop()
            CANAL1.play(ENEMY_MAGICIAN_SOUNDS[len(ENEMY_MAGICIAN_SOUNDS) - 1])
            CANAL1.queue(LOSE_SOUND)
            CANAL1.set_endevent(DERROTA)
            
    for i in soldadosenemigos:
        if(mago.rect().colliderect(i.rect())):
            perdiste = True
            pygame.mixer.music.stop()
            CANAL1.play(LANCER_SOUNDS[len(LANCER_SOUNDS) - 1])
            CANAL1.queue(LOSE_SOUND)
            CANAL1.set_endevent(DERROTA)

    mago.actualizar()

    # Dibujar en pantalla
    pantalla.blit(BACKGROUND,(0,0))
    pantalla.blit(NUBE,(0,65))
    pantalla.blit(NUBE,(266,65))
    pantalla.blit(NUBE,(533,65))

    pantalla.blit(mago.current_sprite, mago.rect())
    for i in magosenemigos:
        pantalla.blit(i.current_sprite, i.rect())
    
    for i in soldadosenemigos:
        pantalla.blit(i.current_sprite, i.rect())
    
    for i in fuego: i.dibujar(pantalla)

    for i in fuegoEnemigo: i.dibujar(pantalla)  

    pygame.display.flip()
    #print(reloj)
