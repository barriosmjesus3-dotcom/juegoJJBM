import pygame
import constantes

class Personaje:
    def __init__(self, x, y):
        
        self.forma = pygame.Rect(0, 0, constantes.ANCHO_PERSONAJE, constantes.ALTO_PERSONAJE)
        
        self.forma.center = (x, y)

    def movimiento(self, delta_x, delta_y):
            self.forma.x = self.forma.x + delta_x
            self.forma.y = self.forma.y + delta_y
            


    def dibujar(self, interfaz):

        # Dibuja el rectángulo en la interfaz con color amarillo (255, 255, 0)
        pygame.draw.rect(interfaz, constantes.COLOR_PERSONAJE, self.forma)