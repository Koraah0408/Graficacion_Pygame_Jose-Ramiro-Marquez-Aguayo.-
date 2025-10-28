# ITCM - Instituto Tecnologico de Ciudad Madero
## Materia: Gráficación 2:00 - 3:00
## Alumno: **José Ramiro Márquez Aguayo**


## Repositorio

Este repositorio trata de algunas actividades hechas con Pygame para practicar junto a unas pequeñas prácticas. Contiene **10 ejercicios** que exploran los conceptos básicos de la programación gráfica en Python, desde la configuración de la ventana hasta el manejo de eventos, el dibujo de formas y la animación.


## Requisitos y Configuración

Para ejecutar cualquiera de estos *scripts*, necesitas tener **Python** y la librería **Pygame** instalada.

1.  **Instalar Pygame:** Abre tu terminal o línea de comandos y ejecuta:
    ```bash
    pip install pygame
    ```
## Contenido del Repositorio

### I. Configuración y Eventos Básicos

| Nombre del Archivo | Descripción de la Funcionalidad |
| :--- | :--- |
| `sesion1_ej1.py` | **Ventana personalizada.** Configuración mínima de Pygame y bucle principal simple con cierre por el botón 'X'. |
| `sesion2_ej2.py` | **Cerrar ventanas con Esc.** Extiende el manejo de eventos para cerrar la ventana al presionar la tecla **`Esc`**. |
| `sesion3_ej3.py` | **Cerrar ventana después de 300 frames.** Introduce el control de **FPS** (`Clock`) y un contador para terminar el programa después de un número fijo de *frames*. |
| `sesion1_mini.py` | **Cambio de fondo interactivo.** Permite cambiar el color de fondo de la ventana (alternando entre blanco y negro) al presionar la tecla **`C`**. |

### II. Dibujo de Formas y Geometría

| Nombre del Archivo | Descripción de la Funcionalidad |
| :--- | :--- |
| `sesion2_ej1.py` | **Dibujo de una tabla de ajedrez con bucle.** Utiliza bucles anidados para dibujar un patrón de $8 \times 8$ de rectángulos, generando un tablero de ajedrez. |
| `sesion2_ej2.py` | **Diseño Geométrico (Círculos).** Dibuja **círculos concéntricos** de diferentes colores con el mismo punto central, creando un efecto de diana. |
| `sesion2_mini.py` | **Casa con cambio de color.** Dibuja una casa simple cuyo cuerpo principal cambia de color según la tecla que se presiona (**R, B, G, Y, D, Q**). |

### III. Movimiento y Animación

| Nombre del Archivo | Descripción de la Funcionalidad |
| :--- | :--- |
| `sesion3_ej1.py` | **Movimiento con Límites.** Permite mover un cuadrado con las flechas del teclado. El cuadrado **cambia a color Rojo** al tocar cualquiera de los límites de la ventana. |
| `sesion3_ej2.py` | **Trayectoria Circular.** Mueve un rectángulo en una **órbita circular** constante en el centro de la pantalla, utilizando funciones trigonométricas (`math`). |
| `sesion3_mini.py` | **Rastro de círculos.** Permite mover un cuadrado y deja un **rastro de pequeños círculos** por donde pasa, implementando un historial de posiciones. |
