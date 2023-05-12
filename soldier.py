import numpy
from settings import *
from routes import *
from entity import Identidad

class Soldado(Identidad):
    def __init__(self, identidad, sprites=SOLDADO_ENEMIGO_SPRITES, x=0, y=300): 
        super().__init__(SOLDADO_ENEMIGO_SPRITES, identidad, x, y)
        self.current_sprite = sprites['spaw'][0]
        self.current_sprite_index = 0
        self.current_sprite_aux = 0
        self.distancia=DISTANCIA_PRED_SOLDADO_ENEMIGO
        self.velocidadX = 0
        self.velocidadY = 0
        self.velocidadMax = 5
        self.spaw = True
        self.atacando = False
        self.tiempo_ataque = 0 
        self.tiempo_ataque_max = 100
        self.direccion_antes_ataque = 'front'
        self.direccion_actual = 'spaw'

    def perseguir(self,identidad):
        self.ciclarSprites()
        if(self.spaw): 
            self.spawneo()
            return

        difX = identidad.x - self.x
        umbral = 10
        distancia_ataque = 100
        distancia_matasion = 20

        ahora = pygame.time.get_ticks()
        if self.atacando and (ahora - self.tiempo_ataque) >= self.tiempo_ataque_max:
            self.atacando = False 
            if self.direccion_actual == 'atackleft':
                self.direccion_actual = 'left'
            elif self.direccion_actual == 'atackright':
                self.direccion_actual = 'right'
        
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
        if  abs(difX) <= distancia_matasion:
            self.direccion_actual = self.direccion_antes_ataque
            self.velocidadX = 0
        elif abs(difX) <= distancia_ataque:
            self.direccion_antes_ataque = self.direccion_actual
            self.atacar()

        # Actualizar la posición del mago enemigo
        self.x += self.velocidadX

    def atacar(self):
        self.atacando = True
        if self.direccion_actual == 'left':
            self.direccion_actual = 'atackleft'
        elif self.direccion_actual == 'right':
            self.direccion_actual = 'atackright'
        
        self.tiempo_ataque = pygame.time.get_ticks()

    def spawneo(self):
        if(int(self.current_sprite_index) != self.current_sprite_aux and self.current_sprite_aux ==8):
            self.spaw = False
        self.current_sprite_aux = int(self.current_sprite_index)

