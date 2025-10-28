import pygame
import sys

BOARD_COLS = 8               # numero de columnas del tablero
BOARD_ROWS = 8               # numero de filas del tablero 
WINDOW_SIZE = 480            # tamaño de la ventana 
SQUARE_SIZE = WINDOW_SIZE // BOARD_COLS  # tamaño de cada casilla

# Colores 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
ventana = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Tablero de ajedrez")

def dibujar_ajedrez(surface): # Dibuja el tablero de ajedrez
    for row in range(BOARD_ROWS): # Recorre las filas
        for col in range(BOARD_COLS): # Recorre las columnas

            if (row + col) % 2 == 0: # Casilla blanca
                color = WHITE
            else:                    # Casilla negra
                color = BLACK

            x = col * SQUARE_SIZE 
            y = row * SQUARE_SIZE 
            rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE) # Rectángulo de la casilla
            pygame.draw.rect(surface, color, rect) # Dibuja la casilla

while True:
    for evento in pygame.event.get():
        # Cerrar con la X
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    dibujar_ajedrez(ventana)
    pygame.display.flip()

