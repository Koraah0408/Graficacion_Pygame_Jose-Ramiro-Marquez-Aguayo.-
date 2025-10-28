import pygame
import sys

pygame.init()

ventana = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Explorando el bucle principal")

color_fondo = (0, 255, 0)
# Agregamos un reloj para controlar los FPS
clock = pygame.time.Clock()
# Contador de frames
frame = 0
max_frames = 300

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Incrementar y mostrar el contador de frames
    frame += 1
    print(f"Frame: {frame}")

    ventana.fill(color_fondo)
    pygame.display.flip()

    # Control de FPS 
    clock.tick(60)

    # Salir después de 300 frames
    if frame >= max_frames:
        pygame.quit()
        sys.exit()
