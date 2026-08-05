import pygame
import constantes
from personaje import Personaje

pygame.init()

# Crear la ventana con las dimensiones de constantes.py
ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
pygame.display.set_caption("Mi primer juego")

def escalar_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, size=(w*scale, h*scale))
    return nueva_imagen

animaciones = []

for i in range(7):
    img = pygame.image.load(f"assets//images//caracters//player//Player_{i}.png")
    img = escalar_img(img, constantes.SCALA_PERSONAJE)

    animaciones.append(img)



jugador = Personaje(50, 50, animaciones)


#VARIABLES DE MOVIMIENTOS DE JUGADOR
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

#frame rate
reloj = pygame.time.Clock()

# Bucle principal del juego
run = True


while run == True:

#para los fps
    reloj.tick(constantes.FPS)

    ventana.fill(constantes.COLOR_BG)

#calcular el movimiento del jugador

    delta_x = 0
    delta_y = 0

    if mover_derecha== True:
        delta_x = constantes.VELOCIDAD
    if mover_izquierda==True:
        delta_x = -constantes.VELOCIDAD
    if mover_arriba == True:
        delta_y = -constantes.VELOCIDAD
    if mover_abajo == True:
        delta_y = constantes.VELOCIDAD

    #mover player
    jugador.movimiento(delta_x, delta_y)

    jugador.update()

    jugador.dibujar(ventana)

    # Capturar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type ==  pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_s:
                mover_abajo = True

#PARA CUANDO SE SUELTE LA TECLA
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_s:
                mover_abajo = False
                

    pygame.display.update()

# Salir de Pygame al cerrar la ventana
pygame.quit()