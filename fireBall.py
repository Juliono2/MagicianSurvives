import numpy, random
from settings import *
from routes import *
from entity import Identidad

class BolaFuego (Identidad):
    def __init__(self, identidad, sprites=BOLA_FUEGO_SPRITE): 
        super().__init__(BOLA_FUEGO_SPRITE, identidad, identidad.x, identidad.y)
        self.current_sprite = sprites['atackleft'][0]
        self.current_sprite_index = 0
        self.o_velocidad = 30
        self.velocidad = self.o_velocidad
        self.dirDisparo = identidad.direccion_actual

    def trayectoria(self):
        if self.dirDisparo == 'atackleft':
            self.x -= self.velocidad
        elif self.dirDisparo == 'atackright':
            self.x += self.velocidad
        elif self.dirDisparo == 'atackdown':
            self.y += self.velocidad
        elif self.dirDisparo == 'atackup':
            self.y -= self.velocidad

        self.ciclarSprites()

    def limites(self):
        if self.x < LIMITE_IZQ or self.y < LIMITE_ARR or self.x+self.hitAncho > LIMITE_DER or self.y+self.hitAlto > LIMITE_ABA:
            return True
        return False
    
    def generarPosicion(self, identidad):
        self.x = identidad.x
        self.y = identidad.y
    