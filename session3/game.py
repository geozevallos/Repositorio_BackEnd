import sys
import pygame

pygame.init()

#Configuracion de la pantalla de juego
size = 800,600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Juego")

#Cargar imagnes
ball = pygame.image.load("pelota.png")
ballrect = ball.get_rect()

bar = pygame.image.load("barra.png")
barrect = bar.get_rect()

#movimiento
speed = [1,1]

#Control del ciclo
run = True
barrect.move_ip(400,260)
while run:
    pygame.time.delay(2)
    #Verificar si se cerro
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #Deteccion de teclas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        barrect = barrect.move(0, 1)
    if keys[pygame.K_UP]:
        barrect = barrect.move(0, -1)
    if (barrect.colliderect(ballrect)):
        speed[0] = -speed[0]
    #Moviendo
    ballrect = ballrect.move(speed)

    #detectar colision
    if ballrect.left < 0 or ballrect.right > 800:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > 600:
        speed[1] = -speed[1]

    #renderizarlo
    white = (255,255,255)
    screen.fill(white)
    screen.blit(ball, ballrect)
    screen.blit(bar, barrect)
    pygame.display.flip()

pygame.quit()