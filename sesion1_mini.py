import pygame
import sys

pygame.init()

ventana = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Cambio de color con tecla C")

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)

color_actual = blanco

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_c:
                # Cambia entre blanco y negro
                if color_actual == blanco:
                    color_actual = negro
                else:
                    color_actual = blanco

    ventana.fill(color_actual)
    pygame.display.flip()
