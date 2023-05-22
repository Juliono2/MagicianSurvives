import pygame, time, random
from settings import *
from routes import *

class Identidad:
    def __init__(self,sprites, identidad=None, x=0, y=0):
        #Sprites
        self.sprites = sprites
        self.spriteClock = int(round(time.time() * 1000))
        #Hitbox
        self.hitAncho = 32
        self.hitAlto = 32
        #Velocidad
        self.direccion_actual = 'front'
        self.o_velocidad = 0
        self.velocidad = self.o_velocidad
        self.distancia=DISTANCIA_PRED
        #Posicion
        if identidad is not None:
            self.generarPosicion(identidad)
            self.y=y
        else:
            self.x = x
            self.y = y

    #Metodo para dibujar en pantalla
    def dibujar(self, pantalla):
        pantalla.blit(self.current_sprite, self.rect(),pygame.Rect(14,10,20,20))
        pygame.draw.lines(pantalla,(0,0,0),True,[(self.x,self.y),(self.x,self.y + self.hitAlto),(self.x + self.hitAncho,self.y + self.hitAlto),(self.x + self.hitAncho,self.y)])
    
    #Genera una posicion aleatoria en x dependiendo el limite y la distancia con la identidad
    def generarPosicion(self, identidad):
        random.seed()
        while True:
            self.x = random.randrange(LIMITE_IZQ, LIMITE_DER-self.hitAncho)
            if abs(identidad.x - self.x) > self.distancia:
                break

    #Metodo para el ciclado de sprites dependiendo la direccion actual 
    def ciclarSprites(self):
        if self.direccion_actual in self.sprites:       #Funciona como estados al consultar la llave del diccionario
            self.current_sprite_index = (self.current_sprite_index + 0.1) % len(self.sprites[self.direccion_actual])
            self.current_sprite = self.sprites[self.direccion_actual][int(self.current_sprite_index)]
        else:
            self.current_sprite = self.sprites['front'][0]

    #Metodo para definir el uso de rectangulos en pygame
    def rect(self):
        return pygame.Rect(self.x, self.y, self.hitAncho, self.hitAlto)

    #Limite de las identidades dentro de la pantalla
    def limites(self):
        while self.x < LIMITE_IZQ:
            self.x += 1
        while self.y < LIMITE_ARR:
            self.y += 1
        while self.x+self.hitAncho > LIMITE_DER:
            self.x -= 1
        while self.y+self.hitAlto > LIMITE_ABA:
            self.y -= 1    

    #Metodo definido para el aumento de velocidades usando los niveles
    def aumenVel(self, nivel):
        self.velocidad = self.o_velocidad + (self.o_velocidad * nivel / 4)

    #Reproduccion de sonidos 
    def reproducirSonido(self,sonido:pygame.mixer.Sound):
        # Buscar un canal disponible para reproducir el sonido
        canal = pygame.mixer.find_channel()
        if canal is not None:       #Si se encuentra un canal disponible, reproducir el sonido en ese canal
            canal.play(sonido)
        else:                       #Si no hay canales disponibles, aumentar el número de canales disponibles en el mezclador de sonido
            pygame.mixer.set_num_channels(pygame.mixer.get_num_channels() + 1)
            canal = pygame.mixer.find_channel()
            canal.play(sonido)