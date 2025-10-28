import pygame
import sys

pygame.init()

ancho, alto = 800, 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Movimiento con limites mejorados")


BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
color_fondo = BLANCO 

# Rectangulo
rect_ancho = 50
rect_alto = 50
# Posicion inicial
rect_x = (ancho - rect_ancho) // 2
rect_y = (alto - rect_alto) // 2
rect_color = AZUL 
velocidad = 0.5

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    rect_color = AZUL 

    nuevo_x = rect_x
    nuevo_y = rect_y

    if teclas[pygame.K_LEFT]:
        nuevo_x -= velocidad
    if teclas[pygame.K_RIGHT]:
        nuevo_x += velocidad
    if teclas[pygame.K_UP]:
        nuevo_y -= velocidad
    if teclas[pygame.K_DOWN]:
        nuevo_y += velocidad


    if nuevo_x < 0:
        rect_x = 0
        rect_color = ROJO # Cambia a rojo al tocar el limite izquierdo
    elif nuevo_x > ancho - rect_ancho:
        rect_x = ancho - rect_ancho
        rect_color = ROJO # Cambia a rojo al tocar el limite derecho
    else:
        rect_x = nuevo_x 

    if nuevo_y < 0:
        rect_y = 0
        rect_color = ROJO # Cambia a rojo al tocar el limite superior
    elif nuevo_y > alto - rect_alto:
        rect_y = alto - rect_alto
        rect_color = ROJO # Cambia a rojo al tocar el limite inferior
    else:
        rect_y = nuevo_y # Aplica la traslacion
        
    ventana.fill(color_fondo)
    
    # Dibuja 
    pygame.draw.rect(ventana, rect_color, (rect_x, rect_y, rect_ancho, rect_alto))
    
    pygame.display.flip()