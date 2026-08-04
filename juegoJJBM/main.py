import pygame
import constantes
from personaje import Personaje

jugador = Personaje(x=50, y=50)

pygame.init()

# Crear la ventana con las dimensiones de constantes.py
ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
pygame.display.set_caption("Mi primer juego")

# Bucle principal del juego
run = True
while run:

    jugador.dibujar(ventana)
    # Capturar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
        

# Salir de Pygame al cerrar la ventana
pygame.quit()