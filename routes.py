import pygame, os

pygame.mixer.init()
pygame.font.init()

#Fondo
BACKGROUND = pygame.image.load(os.path.join('assets','Sprites','Background','Background.png'))

#Nube
NUBE = pygame.image.load(os.path.join('assets','Sprites','Cloud','Nube.png'))

#Jugador caminao
MAGICIAN_FRONT = pygame.image.load(os.path.join('assets','Sprites','Magician','FrontMagician.png'))
MAGICIAN_WALK_DE1 = pygame.image.load(os.path.join('assets','Sprites','Magician','DeMagician.png'))
MAGICIAN_WALK_DE2 = pygame.image.load(os.path.join('assets','Sprites','Magician','DeMagician2.png'))
MAGICIAN_WALK_IZ1 = pygame.image.load(os.path.join('assets','Sprites','Magician','IzMagician.png'))
MAGICIAN_WALK_IZ2 = pygame.image.load(os.path.join('assets','Sprites','Magician','IzMagician2.png')) 

#Jugador ataque
MAGICIAN_ATACK_FRONT1 = pygame.image.load(os.path.join('assets','Sprites','Magician','AtackFrontMagician.png'))
MAGICIAN_ATACK_FRONT2 = pygame.image.load(os.path.join('assets','Sprites','Magician','AtackFrontMagician2.png'))
MAGICIAN_ATACK_IZ1 = pygame.image.load(os.path.join('assets','Sprites','Magician','AtackIzMagician.png'))
MAGICIAN_ATACK_IZ2 = pygame.image.load(os.path.join('assets','Sprites','Magician','AtackIzMagician2.png'))
MAGICIAN_ATACK_DE1 = pygame.image.load(os.path.join('assets','Sprites','Magician','AtackDeMagician.png'))
MAGICIAN_ATACK_DE2 = pygame.image.load(os.path.join('assets','Sprites','Magician','AtackDeMagician2.png')) 

#Para cargar sprites del mago
MAGO_SPRITES = {
    'front': [MAGICIAN_FRONT],
    'right': [MAGICIAN_WALK_DE1, MAGICIAN_WALK_DE2],
    'left': [MAGICIAN_WALK_IZ1, MAGICIAN_WALK_IZ2],
    'up': [MAGICIAN_ATACK_FRONT1],
    'atackup': [MAGICIAN_ATACK_FRONT1,MAGICIAN_ATACK_FRONT2],
    'atackleft': [MAGICIAN_ATACK_IZ1,MAGICIAN_ATACK_IZ2],
    'atackright': [MAGICIAN_ATACK_DE1,MAGICIAN_ATACK_DE2]
}

#Mago Enemigo Caminao
ENEMY_MAGICIAN_FRONT = pygame.image.load(os.path.join('assets','Sprites','EnemyMagician','FrontEnemyMagician.png'))
ENEMY_MAGICIAN_WALK_DE1 = pygame.image.load(os.path.join('assets','Sprites','EnemyMagician','DeEnemyMagician.png'))
ENEMY_MAGICIAN_WALK_DE2 = pygame.image.load(os.path.join('assets','Sprites','EnemyMagician','DeEnemyMagician2.png'))
ENEMY_MAGICIAN_WALK_IZ1 = pygame.image.load(os.path.join('assets','Sprites','EnemyMagician','IzEnemyMagician.png'))
ENEMY_MAGICIAN_WALK_IZ2 = pygame.image.load(os.path.join('assets','Sprites','EnemyMagician','IzEnemyMagician2.png'))

#Ataque Mago Enemigo
ENEMY_MAGICIAN_ATACK1 = pygame.image.load(os.path.join('assets','Sprites','EnemyMagician','AtackFrontEnemyMagician.png'))
ENEMY_MAGICIAN_ATACK2 = pygame.image.load(os.path.join('assets','Sprites','EnemyMagician','AtackFrontEnemyMagician2.png'))

# Animacion de spawn
SPAWN1 = pygame.image.load(os.path.join('assets','Sprites','Spawn','Spawn1.png'))
SPAWN2 = pygame.image.load(os.path.join('assets','Sprites','Spawn','Spawn2.png'))
SPAWN3 = pygame.image.load(os.path.join('assets','Sprites','Spawn','Spawn3.png'))
SPAWN4 = pygame.image.load(os.path.join('assets','Sprites','Spawn','Spawn4.png'))
SPAWN5 = pygame.image.load(os.path.join('assets','Sprites','Spawn','Spawn5.png'))
SPAWN6 = pygame.image.load(os.path.join('assets','Sprites','Spawn','Spawn6.png'))
SPAWN7 = pygame.image.load(os.path.join('assets','Sprites','Spawn','Spawn7.png'))
SPAWN8 = pygame.image.load(os.path.join('assets','Sprites','Spawn','Spawn8.png'))
SPAWN9 = pygame.image.load(os.path.join('assets','Sprites','Spawn','Spawn9.png'))
SPAWNLIST = [SPAWN1,SPAWN2,SPAWN3,SPAWN4,SPAWN5,SPAWN6,SPAWN7,SPAWN8,SPAWN9]

#Para cargar sprites del mago enemigo
MAGO_ENEMIGO_SPRITES = {
    'spaw' : SPAWNLIST,
    'front': [ENEMY_MAGICIAN_FRONT],
    'right': [ENEMY_MAGICIAN_WALK_DE1, ENEMY_MAGICIAN_WALK_DE2],
    'left': [ENEMY_MAGICIAN_WALK_IZ1, ENEMY_MAGICIAN_WALK_IZ2],
    'down': [ENEMY_MAGICIAN_ATACK1],
    'atackdown': [ENEMY_MAGICIAN_ATACK1,ENEMY_MAGICIAN_ATACK2]
}

#Lancero (derecha a izquierda) enemigo caminao
ENEMY_LANCER_WALK_DE1 = pygame.image.load(os.path.join('assets','Sprites','EnemyLancer','DeEnemyLancer.png'))
ENEMY_LANCER_WALK_DE2 = pygame.image.load(os.path.join('assets','Sprites','EnemyLancer','DeEnemyLancer2.png'))

#Lancero (izquierda a derecha) enemigo caminao
ENEMY_LANCER_WALK_IZ1 = pygame.image.load(os.path.join('assets','Sprites','EnemyLancer','IzEnemyLancer.png'))
ENEMY_LANCER_WALK_IZ2 = pygame.image.load(os.path.join('assets','Sprites','EnemyLancer','IzEnemyLancer2.png'))

#Ataque Lancero (derecha a izquierda) Enemigo
ENEMY_LANCER_ATACK_DE1 = pygame.image.load(os.path.join('assets','Sprites','EnemyLancer','AtackDeEnemyLancer.png'))
ENEMY_LANCER_ATACK_DE2 = pygame.image.load(os.path.join('assets','Sprites','EnemyLancer','AtackDeEnemyLancer2.png'))

#Ataque Lancero (izquierda a derecha) Enemigo
ENEMY_LANCER_ATACK_IZ1 = pygame.image.load(os.path.join('assets','Sprites','EnemyLancer','AtackIzEnemyLancer.png'))
ENEMY_LANCER_ATACK_IZ2 = pygame.image.load(os.path.join('assets','Sprites','EnemyLancer','AtackIzEnemyLancer2.png'))


#Diccionario de estados de los sprites de soldado enemigo
SOLDADO_ENEMIGO_SPRITES ={
    'spaw':SPAWNLIST,
    'front':SPAWNLIST,
    'left':[ENEMY_LANCER_WALK_DE1,ENEMY_LANCER_WALK_DE2],
    'right':[ENEMY_LANCER_WALK_IZ1,ENEMY_LANCER_WALK_IZ2],
    'atackleft':[ENEMY_LANCER_ATACK_DE1,ENEMY_LANCER_ATACK_DE2],
    'atackright':[ENEMY_LANCER_ATACK_IZ1,ENEMY_LANCER_ATACK_IZ2]
}

#Bola de fuego arriba, abajo, derecha e izquierda.
FIREUP0 = pygame.image.load(os.path.join('assets','Sprites','FireBall','FireUp0.png'))
FIREUP1 = pygame.image.load(os.path.join('assets','Sprites','FireBall','FireUp1.png'))
FIREUP2 = pygame.image.load(os.path.join('assets','Sprites','FireBall','FireUp2.png'))
FIREUP3 = pygame.image.load(os.path.join('assets','Sprites','FireBall','FireUp3.png'))
FIREDO0 = pygame.image.load(os.path.join('assets','Sprites','FireBall','FireDo0.png'))
FIREDO1 = pygame.image.load(os.path.join('assets','Sprites','FireBall','FireDo1.png'))
FIREDO2 = pygame.image.load(os.path.join('assets','Sprites','FireBall','FireDo2.png'))
FIREDO3 = pygame.image.load(os.path.join('assets','Sprites','FireBall','FireDo3.png'))
FIREDE0 = pygame.image.load(os.path.join('assets','Sprites','FireBall','FireDe0.png'))
FIREDE1 = pygame.image.load(os.path.join('assets','Sprites','FireBall','FireDe1.png'))
FIREDE2 = pygame.image.load(os.path.join('assets','Sprites','FireBall','FireDe2.png'))
FIREDE3 = pygame.image.load(os.path.join('assets','Sprites','FireBall','FireDe3.png'))
FIREIZ0 = pygame.image.load(os.path.join('assets','Sprites','FireBall','FireIz0.png'))
FIREIZ1 = pygame.image.load(os.path.join('assets','Sprites','FireBall','FireIz1.png'))
FIREIZ2 = pygame.image.load(os.path.join('assets','Sprites','FireBall','FireIz2.png'))
FIREIZ3 = pygame.image.load(os.path.join('assets','Sprites','FireBall','FireIz3.png'))

#Diccionario de estados de las bolas de fuego
BOLA_FUEGO_SPRITE={
    'front':[FIREDE0],
    'atackup':[FIREUP0,FIREUP1,FIREUP2,FIREUP3],
    'atackdown':[FIREDO0,FIREDO1,FIREDO2,FIREDO3],
    'atackright':[FIREDE0,FIREDE1,FIREDE2,FIREDE3],
    'atackleft':[FIREIZ0,FIREIZ1,FIREIZ2,FIREIZ3]
}

#---------------------------------------------
#FUENTES

FUENTE = pygame.font.Font(os.path.join('assets','Fuente','super_smash.ttf'),20)

#---------------------------------------------
# SONIDOS
BACK_MUSIC = pygame.mixer.music.load(os.path.join('assets','Sounds','SoundBack.mp3'))
LEVEL_SOUND = pygame.mixer.Sound(os.path.join('assets','Sounds','SubirNivel.mp3'))
LOSE_SOUND = pygame.mixer.Sound(os.path.join('assets','Sounds','Perder.mp3'))
FIREBALL_SOUND1 = pygame.mixer.Sound(os.path.join('assets','Sounds','BolaFuego.mp3'))
FIREBALL_SOUND2 = pygame.mixer.Sound(os.path.join('assets','Sounds','BolaFuego2.mp3'))
LANCER_SOUND1 = pygame.mixer.Sound(os.path.join('assets','Sounds','LancerosAtaque.mp3'))
LANCER_SOUND2 = pygame.mixer.Sound(os.path.join('assets','Sounds','LancerosAtaque2.mp3'))
IMPACT_FIREBALL = pygame.mixer.Sound(os.path.join('assets','Sounds','ImpactoBolaFuego.mp3'))
IMPACT_LANCE = pygame.mixer.Sound(os.path.join('assets','Sounds','ImpactoLancero.mp3'))
FIREBALL_SOUNDS = [FIREBALL_SOUND2,FIREBALL_SOUND1]
LANCER_SOUNDS = [LANCER_SOUND1,LANCER_SOUND2,IMPACT_LANCE]
ENEMY_MAGICIAN_SOUNDS = [FIREBALL_SOUND2,IMPACT_FIREBALL]
#CANALES
pygame.mixer.set_reserved(2)
CANAL1 = pygame.mixer.Channel(0)
CANAL2 = pygame.mixer.Channel(1)