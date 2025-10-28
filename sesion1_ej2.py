import pygame
import sys

pygame.init()

ventana = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Cerrar con tecla")

color_fondo = (255, 0, 0)

# Bucle principal
while True:
    for evento in pygame.event.get():
        # Cerrar con la X
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
            # Cerrar con tecla Esc
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:  # Tecla Esc
                pygame.quit()
                sys.exit()

    ventana.fill(color_fondo)
    pygame.display.flip()
