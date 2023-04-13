import pygame
from random import randint

# Inicialización de Pygame
pygame.init()

# Creación de la ventana
ventana = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Ejemplo 4")

# Carga de imágenes y definición de rectángulos
fondo = pygame.image.load("fondo.jpg").convert()
fondo = pygame.transform.scale(fondo, (1280, 720))
ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
ballrect.width //= 3  # Reducir el ancho del rectángulo de la pelota a la mitad
ballrect.height //= 3  # Reducir la altura del rectángulo de la pelota a la mitad
ball = pygame.transform.scale(ball, (ballrect.width, ballrect.height))
bate = pygame.image.load("bate.png")
baterect = bate.get_rect()
baterect.move_ip(10, 660)

# Configuración de la fuente del texto en pantalla
fuente = pygame.font.Font(None, 36)

# Configuración de la velocidad de la pelota
speed = [randint(3, 6), randint(3, 6)]
ballrect.move_ip(0, 0)

# Bucle principal
jugando = True
while jugando:

    # Manejo de eventos de Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    # Movimiento del bate con las teclas izquierda y derecha
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        baterect = baterect.move(-5, 0)
    if keys[pygame.K_RIGHT]:
        baterect = baterect.move(5, 0)

    # Comprobación de colisión entre el bate y la pelota
    if baterect.colliderect(ballrect):
        speed[1] = -speed[1]

    # Movimiento de la pelota
    ballrect = ballrect.move(speed)

    # Comprobación de colisión con los bordes de la ventana
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0:
        speed[1] = -speed[1]

    # Comprobación de colisión con el borde inferior de la ventana (fin del juego)
    if ballrect.bottom > ventana.get_height():
        texto = fuente.render("Game Over", True, (125, 125, 125))
        texto_rect = texto.get_rect()
        texto_x = ventana.get_width() / 2 - texto_rect.width / 2
        texto_y = ventana.get_height() / 2 - texto_rect.height / 2
        ventana.blit(texto, [texto_x, texto_y])
    else:
        # Dibujado del fondo y los sprites
        ventana.blit(fondo, (0, 0))
        ventana.blit(ball, ballrect)
        ventana.blit(bate, baterect)

    # Actualización de la pantalla
    pygame.display.flip()

    # Limitación de la tasa de refresco a 60 FPS
    pygame.time.Clock().tick(60)

# Salida de Pygame
pygame.quit()
