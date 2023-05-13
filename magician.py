import numpy, pygame
from settings import *
from routes import *
from entity import Identidad

class Mago(Identidad):
    def __init__(self,identidad=None, sprites=MAGO_SPRITES, x=400, y=300):
        super().__init__(MAGO_SPRITES,identidad, x, y)
        self.current_sprite = sprites['front'][0]
        self.current_sprite_index = 0
        self.caminando = False
        self.velocidadX = 0
        self.velocidadY = 0
        self.velocidadMax = 5
        self.atacando = False
        self.tiempo_ataque = 0 
        self.tiempo_ataque_max = 100
        self.nivel = 0
        self.enemigosDerrotados = 0

    def atacar(self):
        self.atacando = True
        if self.direccion_actual == 'left':
            self.direccion_actual = 'atackleft'
        elif self.direccion_actual == 'right':
            self.direccion_actual = 'atackright'
        elif self.direccion_actual == 'up':
            self.direccion_actual = 'atackup'
        
        self.tiempo_ataque = pygame.time.get_ticks()

    def actualizar(self):
        if(self.enemigosDerrotados >= NIVEL[0]['Muertes']):
            self.enemigosDerrotados = 0
            self.nivel += 1
            self.reproducirSonido(LEVEL_SOUND)
        self.ciclarSprites()
        if abs(self.velocidadX) <= 0.1 and abs(self.velocidadY) <= 0.1:
            if not self.atacando:
               self.current_sprite = self.sprites[self.direccion_actual][0]

        # Actualizacion de ataque, limitando el tiempo de la accion.
        ahora = pygame.time.get_ticks()
        if self.atacando and (ahora - self.tiempo_ataque) >= self.tiempo_ataque_max:
            self.atacando = False # desactivar el estado de ataque si ha pasado el tiempo máximo permitido
            if self.direccion_actual == 'atackleft':
                self.direccion_actual = 'left'
            elif self.direccion_actual == 'atackright':
                self.direccion_actual = 'right'
            elif self.direccion_actual == 'atackup':
                self.direccion_actual = 'up'

        # Aceleración para detenerse
        aceleracionX = (-self.velocidadX) / TIEMPO
        aceleracionY = (-self.velocidadY) / TIEMPO

        self.calculoVel(aceleracionX, aceleracionY)

        # Cálculo de la aceleración si se está oprimiendo una tecla
        if self.direccion_actual == 'left':
            aceleracionX = (-self.velocidadMax - self.velocidadX) / TIEMPO
        elif self.direccion_actual == 'right':
            aceleracionX = (self.velocidadMax - self.velocidadX) / TIEMPO
        elif self.direccion_actual == 'up':
            self.velocidadX = 0  

        self.velocidad = numpy.sqrt(self.velocidadX**2 + self.velocidadY**2)

        # Pone techo a la velocidad en velocidadMax
        if self.velocidadX > self.velocidadMax:
            self.velocidadX = self.velocidadMax
        elif self.velocidadX < -self.velocidadMax:
            self.velocidadX = -self.velocidadMax
        if self.velocidadY > self.velocidadMax:
            self.velocidadY = self.velocidadMax
        elif self.velocidadY < -self.velocidadMax:
            self.velocidadY = -self.velocidadMax

        # Aplica el movimiento
        self.x += self.velocidadX
        self.y += self.velocidadY  
  
    def calculoVel(self, aceleracionX, aceleracionY):
        self.velocidadX += aceleracionX * FRAME
        self.velocidadY += aceleracionY * FRAME

    def moverDerecha(self):
        self.direccion_actual = 'right'
        aceleracionX = (self.velocidadMax - self.velocidadX) / TIEMPO
        self.calculoVel(aceleracionX, 0)
        self.ciclarSprites()
        self.caminando = True
        self.atacando = False

        if self.caminando:
            self.current_sprite_index = (self.current_sprite_index + 0.2) % len(self.sprites['right'])
            self.current_sprite = self.sprites['right'][int(self.current_sprite_index)]

    def moverIzquierda(self):
        self.direccion_actual = 'left'
        aceleracionX = (-self.velocidadMax - self.velocidadX) / TIEMPO
        self.calculoVel(aceleracionX, 0)
        self.ciclarSprites()
        self.caminando = True
        self.atacando = False

        if self.caminando:
            self.current_sprite_index = (self.current_sprite_index + 0.2) % len(self.sprites['left'])
            self.current_sprite = self.sprites['left'][int(self.current_sprite_index)]

    def mirarArriba(self):
        self.direccion_actual = 'up'
        self.caminando = False
        self.atacando = False
        self.ciclarSprites()
