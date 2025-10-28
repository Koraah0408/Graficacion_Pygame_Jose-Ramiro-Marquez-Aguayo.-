import pygame
import sys

pygame.init()

ancho, alto = 800, 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Rastro de circulos")

BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
color_fondo = BLANCO 

rect_ancho = 50
rect_alto = 50
rect_x = (ancho - rect_ancho) // 2
rect_y = (alto - rect_alto) // 2
rect_color = AZUL 
velocidad = 0.5

# Rastro
rastro_posiciones = [] 
limite_rastro = 100

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

    # Limites
    rect_x = max(0, min(nuevo_x, ancho - rect_ancho))
    rect_y = max(0, min(nuevo_y, alto - rect_alto))
    
    
    # Calculamos el punto central del rectángulo para un rastro más limpio
    centro_x = int(rect_x + rect_ancho / 2)
    centro_y = int(rect_y + rect_alto / 2)
    
    # Añadimos la posicion actual al rastro
    rastro_posiciones.append((centro_x, centro_y))
    
    # Mantenemos el rastro dentro del límite
    if len(rastro_posiciones) > limite_rastro:
        rastro_posiciones.pop(0)

    # Dibujo 
    ventana.fill(color_fondo) 
    
    radio_rastro_fijo = 5
    
    for x, y in rastro_posiciones:
        pygame.draw.circle(ventana, ROJO, (x, y), radio_rastro_fijo)

    pygame.draw.rect(ventana, rect_color, (rect_x, rect_y, rect_ancho, rect_alto))
    
    pygame.display.flip()