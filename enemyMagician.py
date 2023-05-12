import numpy, random
from settings import *
from routes import *
from entity import Identidad

class MagoEnemigo (Identidad):
    def __init__(self, identidad, sprites=MAGO_ENEMIGO_SPRITES, x=0, y=50): 
        super().__init__(MAGO_ENEMIGO_SPRITES, identidad, x, y)
        self.current_sprite = sprites['spaw'][0]
        self.current_sprite_index = 0
        self.current_sprite_aux = 0
        self.distancia=DISTANCIA_PRED_MAGO_ENEMIGO
        self.velocidadX = 0
        self.velocidadY = 0
        self.velocidadMax = 5
        self.spaw = True
        self.paseando = False
        self.atacando = False
        self.tiempo_ataque = 100 
        self.tiempo_ataque_max = 100
        self.direccion_antes_ataque = 'front'
        self.direccion_actual = 'spaw'

    def moverse(self, identidad):
        self.ciclarSprites()
        if(self.spaw): 
            self.spawneo()
            return
    
        if not self.paseando:
            self.perseguir(identidad)
        else:
            self.direccion_actual = self.direccion_antes_ataque
            if self.direccion_antes_ataque == 'left': 
                self.velocidadX = -self.velocidadMax/15
            else:
                self.velocidadX = self.velocidadMax/15
            
            # Verificar si se ha llegado a un límite
            if self.x - 1 < LIMITE_IZQ or self.x + self.hitAncho +1 > LIMITE_DER: self.paseando = False
        
        # Actualizar la posición del mago enemigo
        self.x += self.velocidadX

    def perseguir(self, identidad):

        difX = abs(identidad.x - self.x)
        difX -= self.hitAncho/2 if identidad.x > self.x else identidad.hitAncho/2
        #umbral = 50
        distancia_ataque = 0

        if difX <= distancia_ataque or self.atacando:
            
            self.atacar()
            self.velocidadX = 0
        else:
            if self.x > identidad.x: 
                self.velocidadX = -self.velocidadMax/15
                self.direccion_actual = "left"
            else:
                self.velocidadX = self.velocidadMax/15
                self.direccion_actual = "right"

    def atacar(self):
        self.tiempo_ataque += 1
        if not self.atacando:
            if self.tiempo_ataque >= self.tiempo_ataque_max:
                self.direccion_antes_ataque = self.direccion_actual
                self.tiempo_ataque = 0
            self.direccion_actual = 'atackdown'
            self.atacando = True

        if self.atacando and (self.tiempo_ataque) >= self.tiempo_ataque_max:
            self.atacando = False # desactivar el estado de ataque si ha pasado el tiempo máximo permitido
            self.paseando = True
            if self.direccion_actual == 'atackdown':
                self.direccion_actual = 'front'

    def ciclarSprites(self):
        if self.direccion_actual in ['right', 'left', 'spaw']:
            return super().ciclarSprites()
        if self.atacando:
            if self.direccion_actual in self.sprites:
                self.current_sprite_index = (self.current_sprite_index + 0.02) % len(self.sprites[self.direccion_actual])
                self.current_sprite = self.sprites[self.direccion_actual][int(self.current_sprite_index)]
    
    def spawneo(self):
        if(int(self.current_sprite_index) != self.current_sprite_aux and self.current_sprite_aux ==8):
            self.spaw = False
        self.current_sprite_aux = int(self.current_sprite_index)