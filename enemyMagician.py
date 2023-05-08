import numpy, random
from settings import *
from routes import *
from entity import Identidad

class MagoEnemigo (Identidad):
    def __init__(self, identidad, sprites=MAGO_ENEMIGO_SPRITES, x=0, y=50): 
        super().__init__(MAGO_ENEMIGO_SPRITES, identidad, x, y)
        self.current_sprite = sprites['front'][0]
        self.current_sprite_index = 0
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

        difX = identidad.x - self.x
        difY = identidad.y - self.y
        umbral = 10
        distancia_ataque = 50

        ahora = pygame.time.get_ticks()
        if self.atacando and (ahora - self.tiempo_ataque) >= self.tiempo_ataque_max:
            self.atacando = False # desactivar el estado de ataque si ha pasado el tiempo máximo permitido
            if self.direccion_actual == 'atackdown':
                self.direccion_actual = 'front'
        
        # Obtener la dirección en la que se mueve el mago enemigo (izquierda o derecha)
        if self.velocidadX > 0:
            self.direccion_actual = 'right'
        elif self.velocidadX < 0:
            self.direccion_actual = 'left'
        else:
            self.direccion_actual = 'front'
        
        # Moverse hacia la derecha o hacia la izquierda según corresponda
        if abs(difX) > umbral:
            if self.direccion_actual == 'left' and difX > 0:
                self.velocidadX *= -1
            elif self.direccion_actual == 'right' and difX < 0:
                self.velocidadX *= -1
            self.velocidadX = min(abs(difX), self.velocidadMax/15) * numpy.sign(difX)
        else:
            self.velocidadX = 0
        
        # Si la distancia entre el mago enemigo y la identidad es menor o igual que la distancia de ataque, atacar
        if abs(difX) <= distancia_ataque:
            self.direccion_antes_ataque = self.direccion_actual
            self.atacar()
            self.moverse(identidad)

        # Actualizar la posición del mago enemigo
        self.x += self.velocidadX

    def atacar(self):
        self.atacando = True
        if self.direccion_actual == 'front':
            self.direccion_actual = 'atackdown'
        
        self.tiempo_ataque = pygame.time.get_ticks()

    def ciclarSprites(self):
        if self.direccion_actual in ['right', 'left']:
            return super().ciclarSprites()
        if self.atacando:
            if self.direccion_actual in self.sprites:
                self.current_sprite_index = (self.current_sprite_index + 0.02) % len(self.sprites[self.direccion_actual])
                self.current_sprite = self.sprites[self.direccion_actual][int(self.current_sprite_index)]
    