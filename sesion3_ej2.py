import pygame
import sys
import math 

pygame.init()

ancho, alto = 800, 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Trayectoria predefinida")


BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
color_fondo = BLANCO 

rect_ancho = 50
rect_alto = 50
rect_color = AZUL 


# Centro del circulo
centro_x = 400 
centro_y = 300 
# Radio de la orbita
radio = 200 
# Angulo inciial
angulo_actual = 0.0 
# Velocidad de rotacion
velocidad_rotacion = 0.0005


# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    angulo_actual += velocidad_rotacion
    
    # Esto asegura que el ángulo se mantenga entre 0 y 2*pi
    if angulo_actual > 2 * math.pi:
        angulo_actual -= 2 * math.pi

    # Calculamos la nueva posición (x, y) usando trigonometria
    posicion_relativa_x = radio * math.cos(angulo_actual)
    posicion_relativa_y = radio * math.sin(angulo_actual)

    # Posición final en la ventana, sumando las coordenadas del centro
    # Restamos la mitad del ancho/alto para centrar el rectángulo
    rect_x = centro_x + posicion_relativa_x - (rect_ancho // 2)
    rect_y = centro_y + posicion_relativa_y - (rect_alto // 2)

    ventana.fill(color_fondo) 
    
    pygame.draw.rect(ventana, rect_color, (rect_x, rect_y, rect_ancho, rect_alto))
    
    # --- Actualización de Pantalla ---
    pygame.display.flip()
