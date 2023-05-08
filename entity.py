import pygame, time, random
from settings import *
from routes import *

class Identidad:
    def __init__(self,sprites, identidad=None, x=0, y=0):
        self.sprites = sprites
        self.spriteClock = int(round(time.time() * 1000))
        self.hitAncho = 32
        self.hitAlto = 32
        self.direccion_actual = 'front'
        self.o_velocidad = 0
        self.velocidad = self.o_velocidad
        self.distancia=DISTANCIA_PRED
        if identidad is not None:
            self.generarPosicion(identidad)
            self.y=y
        else:
            self.x = x
            self.y = y

    def dibujar(self, pantalla):
        pantalla.blit(self.current_sprite, self.rect())
    
    def generarPosicion(self, identidad):
        random.seed()
        while True:
            self.x = random.randrange(LIMITE_IZQ, LIMITE_DER-self.hitAncho)
            if abs(identidad.x - self.x) > self.distancia:
                break

    def ciclarSprites(self):

        if self.direccion_actual in self.sprites:
            self.current_sprite_index = (self.current_sprite_index + 0.2) % len(self.sprites[self.direccion_actual])
            self.current_sprite = self.sprites[self.direccion_actual][int(self.current_sprite_index)]

        else:
            self.current_sprite = self.sprites['front'][0]

    def rect(self):
        return pygame.Rect(self.x, self.y, self.hitAncho, self.hitAlto)


    def limites(self):
        while self.x < LIMITE_IZQ:
            self.x += 1
        while self.y < LIMITE_ARR:
            self.y += 1
        while self.x+self.hitAncho > LIMITE_DER:
            self.x -= 1
        while self.y+self.hitAlto > LIMITE_ABA:
            self.y -= 1    

    def aumenVel(self, nivel):
        self.velocidad = self.o_velocidad + (self.o_velocidad * nivel / 4)

