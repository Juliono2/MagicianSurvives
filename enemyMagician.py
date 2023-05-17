import numpy, random
from settings import *
from routes import *
from entity import Identidad

class MagoEnemigo (Identidad):
    def __init__(self, identidad, sprites=MAGO_ENEMIGO_SPRITES, x=0, y=50): 
        super().__init__(MAGO_ENEMIGO_SPRITES, identidad, x, y)
        self.generarPosicion(identidad)
        self.nivel = identidad.nivel
        #Sprites
        self.current_sprite = sprites['spaw'][0]
        self.current_sprite_index = 0
        self.current_sprite_aux = 0
        #Velocidad
        self.velocidadX = 0
        self.velocidadMax = NIVEL[self.nivel]['Velocidad']
        #Estados
        self.spaw = True
        self.paseando = False
        self.atacando = False
        #Ataque
        self.tiempo_ataque = NIVEL[len(NIVEL) - 1]['TiempoFuego']
        self.tiempo_ataque_max = NIVEL[self.nivel]['TiempoFuego']
        self.direccion_antes_ataque = 'left'
        self.direccion_actual = 'spaw'

    def generarPosicion(self, identidad:Identidad):
        self.limitesNube = [0,0]
        posx = (identidad.x + identidad.hitAncho/2) - (NUBES['Inicio'] - NUBES['EspacioMedio']//2)
        nube = 0
        if(posx < 0):
            nube = 1
        else:
            nube = posx // (NUBES['Ancho'] + NUBES['EspacioMedio'])
        
        self.limitesNube[0]  = NUBES['Inicio'] + (NUBES['Ancho'] + NUBES['EspacioMedio'])*nube
        self.limitesNube[1]  = NUBES['Inicio'] + (NUBES['Ancho'] + NUBES['EspacioMedio'])*(nube+1) - NUBES['EspacioMedio']
        self.x = self.limitesNube[0] + random.randint(0,250 - self.hitAncho)

    def moverse(self, identidad: Identidad):
        self.ciclarSprites()
        if(self.spaw): 
            self.spawneo()
            return
        enRango = ((identidad.x + identidad.hitAncho//2)  >= self.limitesNube[0] and identidad.x + identidad.hitAncho//2 <= self.limitesNube[1])
        
        if not self.paseando and enRango:                
            self.perseguir(identidad)
        else:
            #retomar dirreccion que tenia antes de atacar
            self.direccion_actual = self.direccion_antes_ataque

            if self.direccion_actual == 'left': 
                self.velocidadX = -self.velocidadMax
            else:
                self.velocidadX = self.velocidadMax

            # Verificar si se ha llegado a un límite
            if(self.x - self.velocidadMax < self.limitesNube[0] and self.direccion_antes_ataque == 'left'):
                self.paseando = False
                self.direccion_antes_ataque = 'right'
                self.direccion_actual = 'right'
            elif(self.x + self.hitAncho + self.velocidadMax > self.limitesNube[1] and self.direccion_antes_ataque == 'right'):
                self.paseando = False
                self.direccion_antes_ataque = 'left'
                self.direccion_actual = 'left'
                
        
        # Actualizar la posición del mago enemigo
        self.x += self.velocidadX

    def perseguir(self, identidad):

        #distancia hasta el jugador
        difX = abs(identidad.x - self.x)
        difX -= self.hitAncho/2 if identidad.x > self.x else identidad.hitAncho/2
        distancia_ataque = 0

        #ataque
        if difX <= distancia_ataque or self.atacando:
            self.atacar()
            self.velocidadX = 0
        
        #persecucion
        else:
            if self.x > identidad.x: 
                self.velocidadX = -self.velocidadMax
                self.direccion_actual = "left"
            else:
                self.velocidadX = self.velocidadMax
                self.direccion_actual = "right"

    def atacar(self):
        self.tiempo_ataque += 1
        if not self.atacando:
            #primer ataque tras "pasear"
            if self.tiempo_ataque >= self.tiempo_ataque_max:
                if (self.direccion_actual == 'spaw'): self.direccion_actual = 'left'
                self.direccion_antes_ataque = self.direccion_actual
                self.tiempo_ataque = 0
            #ataque al alcanzar al jugador
            self.current_sprite_index = 1
            self.current_sprite_aux = 0
            self.direccion_actual = 'atackdown'
            self.atacando = True

        #desactivar el estado de ataque si ha pasado el tiempo máximo permitido
        if self.atacando and (self.tiempo_ataque) >= self.tiempo_ataque_max:
            self.atacando = False 
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
        if(int(self.current_sprite_index) != self.current_sprite_aux and self.current_sprite_aux == 8):
            self.spaw = False
        self.current_sprite_aux = int(self.current_sprite_index)