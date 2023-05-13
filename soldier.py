import numpy
from settings import *
from routes import *
from entity import Identidad
import random

class Soldado(Identidad):
    def __init__(self, identidad, sprites=SOLDADO_ENEMIGO_SPRITES, x=0, y=300): 
        super().__init__(SOLDADO_ENEMIGO_SPRITES, identidad, x, y)
        self.current_sprite = sprites['spaw'][0]
        self.current_sprite_index = 0
        self.current_sprite_aux = 0
        self.distancia=DISTANCIA_PRED_SOLDADO_ENEMIGO
        self.velocidadX = 0
        self.velocidadY = 0
        self.velocidadMax = NIVEL[identidad.nivel]['Velocidad']
        self.spaw = True
        self.atacando = False
        self.tiempo_ataque = 0 
        self.tiempo_ataque_max = 100
        self.direccion_antes_ataque = 'front'
        self.direccion_actual = 'spaw'
        self.distancia_ataque = 100

    def perseguir(self,identidad):
        self.ciclarSprites()
        if(self.spaw): 
            self.spawneo()
            return

        difX = abs(identidad.x - self.x)
        difX -= self.hitAncho/2 if identidad.x > self.x else identidad.hitAncho/2
        #umbral = 50

        velocidad = self.velocidadMax

        if difX <= self.distancia_ataque:
            
            self.atacar()
            velocidad = self.velocidadMax*3/2
        else:
            self.atacando = False

        if self.x > identidad.x: 
            self.velocidadX = -velocidad
            self.direccion_actual = "left"
        else:
            self.velocidadX = velocidad
            self.direccion_actual = "right"

        self.x += self.velocidadX

    def atacar(self):
        if(not self.atacando):
            self.tiempo_ataque = pygame.time.get_ticks()
            atac = random.randint(0,len(LANCER_SOUNDS) - 2)
            self.reproducirSonido(LANCER_SOUNDS[atac])

        self.atacando = True
        if self.direccion_actual == 'left':
            self.direccion_actual = 'atackleft'
        elif self.direccion_actual == 'right':
            self.direccion_actual = 'atackright'
        
            

    def spawneo(self):
        if(int(self.current_sprite_index) != self.current_sprite_aux and self.current_sprite_aux ==8):
            self.spaw = False
        self.current_sprite_aux = int(self.current_sprite_index)

