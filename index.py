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
bola = BolaFuego(mago)

identidades = [mago]
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
pygame.mixer.music.play(-1)

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
        identidades.append(BolaFuego(mago))
        space_key_down = True
    elif not keys[pygame.K_SPACE]:
        space_key_down = False

    for i in identidades:
        if isinstance(i,BolaFuego):
            i.trayectoria()
            print(i.x, i.y)
            pantalla.blit(i.current_sprite, i.rect())
            i.dibujar(pantalla)

    # Actualizar estado del mago
    magoenemigo.limites()
    soldao.limites()
    mago.limites()

    bola.trayectoria()
    soldao.perseguir(mago)
    magoenemigo.perseguir(mago)

    mago.actualizar()

    # Dibujar en pantalla
    pantalla.blit(BACKGROUND,(0,0))
    pantalla.blit(NUBE,(0,65))
    pantalla.blit(NUBE,(266,65))
    pantalla.blit(NUBE,(533,65))
    pantalla.blit(mago.current_sprite, mago.rect())
    pantalla.blit(bola.current_sprite, bola.rect())
    pantalla.blit(magoenemigo.current_sprite, magoenemigo.rect())
    pantalla.blit(soldao.current_sprite, soldao.rect())
    pygame.display.flip()
