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
        self.spaw = True
        self.atacando = False
        self.direccion_actual = 'spaw'
        if self.x > identidad.x: 
            self.velocidadMax = -NIVEL[identidad.nivel]['Velocidad']
            self.direccion = "left"
        else:
            self.velocidadMax = NIVEL[identidad.nivel]['Velocidad']
            self.direccion = "right"
        self.distancia_ataque = abs(self.velocidadMax) * 200

    def perseguir(self,identidad):
        self.ciclarSprites()
        if(self.spaw): 
            self.spawneo()
            return
        print("fin")
        difX = abs(identidad.x - self.x)
        difX -= self.hitAncho/2 if identidad.x > self.x else identidad.hitAncho/2
        #umbral = 50


        if difX <= self.distancia_ataque:
            self.atacar()
        else:
            self.atacando = False
            self.velocidadX = self.velocidadMax
            self.direccion_actual = self.direccion

        self.x += self.velocidadX

    def atacar(self):
        if(not self.atacando):
            atac = random.randint(0,len(LANCER_SOUNDS) - 2)
            self.reproducirSonido(LANCER_SOUNDS[atac])

        self.atacando = True
        self.direccion_actual = 'atack' + self.direccion
        self.velocidadX = self.velocidadMax*2
        
            

    def spawneo(self):
        if(int(self.current_sprite_index) != self.current_sprite_aux and self.current_sprite_aux ==8):
            self.spaw = False
        self.current_sprite_aux = int(self.current_sprite_index)

