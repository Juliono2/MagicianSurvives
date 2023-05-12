import numpy, random
from settings import *
from routes import *
from entity import Identidad

class MagoEnemigo (Identidad):
    def __init__(self, identidad, sprites=MAGO_ENEMIGO_SPRITES, x=0, y=50): 
        super().__init__(MAGO_ENEMIGO_SPRITES, identidad, x, y)
        self.current_sprite = sprites['front'][0]
        self.current_sprite_index = 0
        self.current_sprite_Aux = 0
        self.distancia=DISTANCIA_PRED_MAGO_ENEMIGO
        self.caminando = False
        self.velocidadX = 0
        self.velocidadY = 0
        self.velocidadMax = 5
        self.atacando = False
        self.tiempo_ataque = 0 
        self.tiempo_ataque_max = 100
        self.direccion_antes_ataque = 'front'

    def moverse(self, identidad):
        if self.direccion_antes_ataque == 'left':
            self.velocidadX *= -1
        elif self.direccion_antes_ataque == 'right':
            self.velocidadX *= -1
        else:
            self.velocidadX = 0

        self.x += self.velocidadX

        # Verificar si se ha llegado a un límite
        if self.x < LIMITE_IZQ or self.x + self.hitAncho > LIMITE_DER:
            self.perseguir(identidad)  # Llamar a la función perseguir para volver a buscar al enemigo
            return

    def perseguir(self, identidad):
        self.ciclarSprites()

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

        # Actualizar la posición del mago enemigo
        self.x += self.velocidadX

    def atacar(self):
        self.atacando = True
        self.direccion_actual = 'atackdown'
        self.tiempo_ataque = pygame.time.get_ticks()

    def ciclarSprites(self):
        if self.direccion_actual in ['right', 'left']:
            return super().ciclarSprites()
        if self.atacando:
            if self.direccion_actual in self.sprites:
                self.current_sprite_index = (self.current_sprite_index + 0.02) % len(self.sprites[self.direccion_actual])
                self.current_sprite = self.sprites[self.direccion_actual][int(self.current_sprite_index)]
    