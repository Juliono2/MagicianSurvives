#Propiedades de la ventana
ANCHO, ALTO = 800, 400		

#Propiedades del escenario
LIMITE_IZQ, LIMITE_ARR = 30, 40
LIMITE_DER, LIMITE_ABA = ANCHO-LIMITE_IZQ, ALTO-LIMITE_IZQ
ANCHO_ESC, ALTO_ESC = LIMITE_DER-LIMITE_IZQ, LIMITE_ABA-LIMITE_ARR

#Constantes Identidades
IDEN_ENEMIGAS_MAX = None
DISTANCIA_PRED = 300
DISTANCIA_PRED_SOLDADO_ENEMIGO = 200
DISTANCIA_PRED_MAGO_ENEMIGO = DISTANCIA_PRED
PROBABILIDAD_SOLDADO = 2/3
PROBABILIDAD_MAGO =1/20

#Variables para el control del juego.
FPS = 60
FRAME = 1/FPS
TIEMPO = FPS/400

#Configuracion de niveles
NIVEL = [
    {'Muertes':10   , 'Spaw':5000, 'Velocidad': 0.25, 'TiempoFuego': 30},
    {'Muertes':20   , 'Spaw':3000, 'Velocidad': 0.5 , 'TiempoFuego': 60},
    {'Muertes':40   , 'Spaw':3000, 'Velocidad': 1   , 'TiempoFuego': 120},
    {'Muertes':50   , 'Spaw':2000, 'Velocidad': 2   , 'TiempoFuego': 180},
    {'Muertes':10000, 'Spaw':1000, 'Velocidad': 3   , 'TiempoFuego': 250}]

#Configuracion de nubes
NUBES = {'Ancho' : 250,
         'Inicio': 9,
         'EspacioMedio' : 16}
