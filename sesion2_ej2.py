import pygame
import sys

pygame.init()
ventana = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Diseño geométrico")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
BG = (200, 200, 200)  # Fondo gris claro

def dibujar_circulos(surface):
   
    # Círculo 1
    pygame.draw.circle(surface, BLANCO, (500, 400), 20, 3) 
    # Círculo 2
    pygame.draw.circle(surface, NEGRO, (500, 400), 40, 3)
    # Círculo 3
    pygame.draw.circle(surface, ROJO, (500, 400), 60, 3)
    # Círculo 4
    pygame.draw.circle(surface, VERDE, (500, 400), 80, 3)
    # Círculo 5
    pygame.draw.circle(surface, AZUL, (500, 400), 100, 3)

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ventana.fill(BG)               # Fondo
    dibujar_circulos(ventana)      # Dibuja los círculos con contorno
    pygame.display.flip()          # Actualiza la pantalla