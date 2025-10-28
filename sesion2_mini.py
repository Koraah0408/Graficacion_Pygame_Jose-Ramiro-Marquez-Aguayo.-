import pygame
import sys

# Inicialización
pygame.init()
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Casa con cambio de color")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 200, 0)
MARRON = (139, 69, 19)
GRIS = (180, 180, 180)
AMARILLO = (255, 255, 0)
AZUL_CIELO = (135, 206, 235)
color_casa = ROJO

def dibujar_casa(surface, color):

    # Fondo
    surface.fill((135, 206, 235)) 

    # Cuerpo de la casa
    pygame.draw.rect(surface, color, (325, 250, 150, 150)) 

    # Techo
    pygame.draw.polygon(surface, MARRON, [
        (305, 250),  
        (495, 250),  
        (400, 170)   
    ])

    # Puerta 
    pygame.draw.rect(surface, MARRON, (385, 330, 30, 70))

    # Ventanas
    pygame.draw.circle(surface, BLANCO, (360, 290), 10) 
    pygame.draw.circle(surface, BLANCO, (440, 290), 10) 

color_casa = ROJO 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Cambiar color con teclas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color_casa = ROJO
            elif event.key == pygame.K_b:
                color_casa = AZUL
            elif event.key == pygame.K_g:
                color_casa = VERDE
            elif event.key == pygame.K_y:
                color_casa = AMARILLO
            elif event.key == pygame.K_d:
                color_casa = NEGRO
            elif event.key == pygame.K_q:
                color_casa = GRIS

    dibujar_casa(ventana, color_casa)
    pygame.display.flip()