import pygame
import constantes


class Personaje:
    def __init__(self, x, y):
        # Forma rectangular de 20x20 píxeles
        self.forma = pygame.Rect(0, 0, constantes.ANCHO_PERSONAJE,
                                  constantes.ALTO_PERSONAJE)
        # Posiciona el centro del rectángulo en las coordenadas (x, y)
        self.forma.center = (x, y)

    def dibujar(self, interfaz):

        # Dibuja el rectángulo en la interfaz con color amarillo (255, 255, 0)
        pygame.draw.rect(interfaz, constantes.COLOR_PERSONAJE, self.forma)