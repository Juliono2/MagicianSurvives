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
magoenemigo = MagoEnemigo(mago)
soldao = Soldado(mago)

fuego = []
magosenemigos = [magoenemigo]
soldadosenemigos = [soldao]
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

#Musiquita
# pygame.mixer.music.play(-1)

# Bucle principal
while True:
    
    reloj = pygame.time.Clock()

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
     
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
        i.perseguir(mago)

    for i in soldadosenemigos:
        i.perseguir(mago)

    #Disparo de magos enemigos
    for i in magosenemigos:
        if(int(i.current_sprite_index) != i.current_sprite_Aux and i.atacando and i.current_sprite_Aux ==0):
            bolaF = BolaFuego(i)
            fuegoEnemigo.append(bolaF)
        i.current_sprite_Aux = int(i.current_sprite_index)
    
    #Disparos del Mago
    for i in fuego: 
        i.trayectoria()
        for j in magosenemigos:
            if(j.rect().colliderect(i.rect())):
                fuego.remove(i)
                magosenemigos.remove(j)
                break

        
        for j in soldadosenemigos:
            if(j.rect().colliderect(i.rect())):
                fuego.remove(i)
                soldadosenemigos.remove(j)
                break

    # Ataques Enemigos
    for i in fuegoEnemigo:
        i.trayectoria()    
        if(mago.rect().colliderect(i.rect())):
            fuegoEnemigo.remove(i)

            print("derrota")
            
    for i in soldadosenemigos:
        if(mago.rect().colliderect(i.rect())):
            
            print("derrota")

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
