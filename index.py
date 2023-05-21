import pygame, numpy
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
DERROTA = pygame.USEREVENT + 1

def inicializar():
    global mago,fuego,magosenemigos,soldadosenemigos,fuegoEnemigo
    global ultimoMago,ultimoSoldao,timeSoldao,timeMago
    global space_key_down,score, enemigos, inicio, perdiste
    # Crear instancia del mago
    mago = Mago()

    fuego = []
    magosenemigos = []
    soldadosenemigos = []
    fuegoEnemigo = []

    space_key_down = False

    #Variables Spaw
    timeMago = NIVEL[0]['Spaw']
    ultimoMago = 0
    timeSoldao = NIVEL[0]['Spaw']
    ultimoSoldao = 0

    #Score
    score = 0
    enemigos = 0
    inicio = pygame.time.get_ticks()

#Variable Derrota
perdiste = False

inicializar()

# Bucle principal
while True:

    reloj = pygame.time.Clock()
    keys = pygame.key.get_pressed()

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        #Derrota
        if (event.type == DERROTA):
            
            if(CANAL1.get_busy() or CANAL1.get_queue()!=None):
                break

            # Guardar Score
            scores = []

            with open("highscore.txt","r") as file:
                for linea in file:
                    preScore =int(linea.split("=")[1])
                    if(score > preScore):
                        scores.append(score)
                        score = preScore
                    else: 
                        scores.append(preScore)


            with open("highscore.txt","w") as file:
                for scr in scores:
                    file.write("Score = " + (str)(scr) + "\n")

            #Salir

    if(perdiste): 
        
        i = 0
        if(keys[pygame.K_RETURN]):
            inicializar()
            #Musiquita
            pygame.mixer.music.play(-1)
            perdiste = False        
        continue

    #Spaw enemigos
    if(timeMago - ultimoMago >= NIVEL[mago.nivel]['Spaw']):
        ultimoMago = pygame.time.get_ticks()
        timeMago = 0
        magosenemigos.append(MagoEnemigo(mago))
    else:
        timeMago = pygame.time.get_ticks()

    if(timeSoldao -ultimoSoldao >= NIVEL[mago.nivel]['Spaw']):
        ultimoSoldao = pygame.time.get_ticks()
        timeSoldao = 0
        soldadosenemigos.append(Soldado(mago))
    else:
        timeSoldao = pygame.time.get_ticks()

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

    mago.limites()

    
    #Movimiento enemigos
    for i in magosenemigos:
        i.moverse(mago)

    for i in soldadosenemigos:
        i.perseguir(mago)

    #Disparo de magos enemigos
    for i in magosenemigos:
        if(int(i.current_sprite_index) != i.current_sprite_aux and i.atacando):
            if (i.current_sprite_aux == 0):
                bolaF = BolaFuego(i)
                fuegoEnemigo.append(bolaF)
                bolaF.reproducirSonido(ENEMY_MAGICIAN_SOUNDS[0])
            elif (i.current_sprite_aux == 1):
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
                enemigos += 1
                mago.enemigosDerrotados += 1
                score += int(((pygame.time.get_ticks() - inicio) / 1000)**(1/3)) * (mago.nivel + 1)
                break

        
        for j in soldadosenemigos:
            if(j.rect().colliderect(i.rect())):
                i.reproducirSonido(FIREBALL_SOUNDS[1])  
                fuego.remove(i)
                soldadosenemigos.remove(j)
                enemigos += 1
                mago.enemigosDerrotados += 1
                score += int(((pygame.time.get_ticks() - inicio) / 1000)**(1/3)) * (mago.nivel + 1)
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
    pantalla.blit(NUBE,(9,65))
    pantalla.blit(NUBE,(275,65))
    pantalla.blit(NUBE,(541,65))
    pantalla.blit(FUENTE.render('LEVEL :', True, (0,0,0)),(10,10))
    pantalla.blit(FUENTE.render(f'{mago.nivel + 1}', True, (0,0,0)),(90,10))
    pantalla.blit(FUENTE.render('ENEMIES :', True, (0,0,0)),(200,10))
    pantalla.blit(FUENTE.render(f'{enemigos}', True, (0,0,0)),(310,10))
    pantalla.blit(FUENTE.render('TIME :', True, (0,0,0)),(400,10))
    pantalla.blit(FUENTE.render(f'{int((pygame.time.get_ticks() - inicio)/1000)}', True, (0,0,0)),(510,10))
    pantalla.blit(FUENTE.render('SCORE :', True, (0,0,0)),(600,10))
    pantalla.blit(FUENTE.render(f'{score}', True, (0,0,0)),(710,10))
    pygame.draw.line(pantalla,(0,0,0),(9,0),(9,ALTO))
    pygame.draw.line(pantalla,(0,0,0),(259,0),(259,ALTO))
    pygame.draw.line(pantalla,(0,0,0),(275,0),(275,ALTO))
    pygame.draw.line(pantalla,(0,0,0),(525,0),(525,ALTO))
    pygame.draw.line(pantalla,(0,0,0),(541,0),(541,ALTO))
    pygame.draw.line(pantalla,(0,0,0),(791,0),(791,ALTO))

    pantalla.blit(mago.current_sprite, mago.rect())
    for i in magosenemigos:
        pantalla.blit(i.current_sprite, i.rect())
    
    for i in soldadosenemigos:
        pantalla.blit(i.current_sprite, i.rect())
    
    for i in fuego: i.dibujar(pantalla)

    for i in fuegoEnemigo: i.dibujar(pantalla)  

    pygame.display.flip()
    #print(reloj)
