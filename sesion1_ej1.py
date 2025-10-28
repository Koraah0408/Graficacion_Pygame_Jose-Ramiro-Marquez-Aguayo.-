import pygame 
import sys

# Inicializamos pygame
pygame.init()

# Programamos el ancho y alto
ancho, alto = 1000, 800
# Le pones a la ventana el ancho y alto
ventana = pygame.display.set_mode((ancho, alto))
# Le pones un título a la ventana
pygame.display.set_caption("Mi primer programa grafico")

# Color de fondo 
color_fondo = (255, 0, 0)

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ventana.fill(color_fondo)
    pygame.display.flip()
