import numpy, random
from settings import *
from routes import *
from entity import Identidad

class BolaFuego (Identidad):
    def __init__(self, identidad, sprites=BOLA_FUEGO_SPRITE): 
        super().__init__(BOLA_FUEGO_SPRITE, identidad, identidad.x, identidad.y)
        self.direccion_actual = identidad.direccion_actual
        self.current_sprite = sprites[identidad.direccion_actual][0]
        self.current_sprite_index = 0
        self.hitAlto = 16
        self.hitAncho = 16
        self.velocidadX = 0
        self.velocidadY = 0
        self.vel = NIVEL[identidad.nivel]['Velocidad'] * 2

        if identidad.direccion_actual == 'atackleft':
            self.velocidadX = -self.vel
            self.hitAncho = 18
            self.y += 8
        elif identidad.direccion_actual == 'atackright':
            self.velocidadX = self.vel
            self.hitAncho = 18
            self.y += 8
        elif identidad.direccion_actual == 'atackdown':
            self.velocidadY = self.vel
            self.x += 8
        elif identidad.direccion_actual == 'atackup':
            self.velocidadY = -self.vel
            self.x += 8

    def trayectoria(self):
        self.x += self.velocidadX
        self.y += self.velocidadY
        self.ciclarSprites()

    def limites(self):
        if self.x < LIMITE_IZQ or self.y < LIMITE_ARR or self.x+self.hitAncho > LIMITE_DER or self.y+self.hitAlto > LIMITE_ABA:
            return True
        return False
    
    def generarPosicion(self, identidad):
        self.x = identidad.x
        self.y = identidad.y
    