import numpy
from settings import *
from routes import *
from entity import Identidad
import random

class Soldado(Identidad):
    def __init__(self, identidad, sprites=SOLDADO_ENEMIGO_SPRITES, x=0, y=300): 
        super().__init__(SOLDADO_ENEMIGO_SPRITES, identidad, x, y)
        #Sprites
        self.current_sprite = sprites['spaw'][0]
        self.current_sprite_index = 0
        self.current_sprite_aux = 0
        #Velocidad
        self.distancia=DISTANCIA_PRED_SOLDADO_ENEMIGO
        self.velocidadX = 0
        #Estados
        self.spaw = True
        self.atacando = False
        self.direccion_actual = 'spaw'
        #Aumento de velocidades
        if self.x > identidad.x: 
            self.velocidadMax = -NIVEL[identidad.nivel]['Velocidad']
            self.direccion = "left"
        else:
            self.velocidadMax = NIVEL[identidad.nivel]['Velocidad']
            self.direccion = "right"
        #Ataque
        self.distancia_ataque = abs(self.velocidadMax) * 200

    #Metodo para perseguir a una identidad,
    def perseguir(self,identidad):
        self.ciclarSprites()
        if(self.spaw): 
            self.spawneo()
            return
        difX = abs(identidad.x - self.x)
        difX -= self.hitAncho/2 if identidad.x > self.x else identidad.hitAncho/2  #Consideramos la hitbox
        #umbral = 50

        #Si la distancia menor o igual a la distacia de ataque entonces ataca, de lo contrario no
        if difX <= self.distancia_ataque:
            self.atacar()
        else:
            self.atacando = False
            self.velocidadX = self.velocidadMax
            self.direccion_actual = self.direccion

        self.x += self.velocidadX

    #Metodo para atacar
    def atacar(self):
        if(not self.atacando):
            atac = random.randint(0,len(LANCER_SOUNDS) - 2) #Efectuamos cualquier sonido contenido en la lista de
            self.reproducirSonido(LANCER_SOUNDS[atac])      #sonidos para los ataques de lanceros

        self.atacando = True
        self.direccion_actual = 'atack' + self.direccion
        self.velocidadX = self.velocidadMax*2
        
    #Metodo para el spawneo, este deja de "aparecer" si uso los 9 sprites para aparecer
    def spawneo(self):
        if(int(self.current_sprite_index) != self.current_sprite_aux and self.current_sprite_aux ==8):
            self.spaw = False
        self.current_sprite_aux = int(self.current_sprite_index)

