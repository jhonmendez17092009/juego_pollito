import pygame
import sys

f = (135, 255, 0)
m = (82, 66, 1)
r = (255, 0, 0)
P = (250, 248, 98)
v = (0, 0, 0)
g = (111, 101, 100)
a = (255, 255, 0)
n = (255, 255, 255)
k = (0, 0, 255)
A = (0, 0, 255)

pygame.init()

ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pollito aplastado")
clock = pygame.time.Clock()

xx1, xx2 = 300, 350 
xx3, xx4 = 450, 500  
MOVIMIENTO_DERECHA = 3  
MOVIMIENTO_IZQUIERDA = -3  
TAM_CUADRADO = 50  
movimiento_derecha1 = MOVIMIENTO_DERECHA
movimiento_derecha2 = MOVIMIENTO_DERECHA
movimiento_izquierda3 = MOVIMIENTO_IZQUIERDA
movimiento_izquierda4 = MOVIMIENTO_IZQUIERDA

pollito_x, pollito_y = 375, 500  
pollito_vel = 5  
vidas = 3  

movimiento_derecha1 = MOVIMIENTO_DERECHA
movimiento_derecha2 = MOVIMIENTO_DERECHA
movimiento_izquierda3 = MOVIMIENTO_IZQUIERDA
movimiento_izquierda4 = MOVIMIENTO_IZQUIERDA

def mostrar_vidas():
    fuente = pygame.font.SysFont("Arial", 30)
    texto = fuente.render(f'Vidas: {vidas}', True, (255, 0, 0))
    ventana.blit(texto, (10, 10))

def detectar_colision(pollito_rect, carros):
    for carro in carros:
        if pollito_rect.colliderect(carro):  
            return True
    return False

while True:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT]:
        pollito_x -= pollito_vel
    if keys[pygame.K_RIGHT]:
        pollito_x += pollito_vel
    if keys[pygame.K_UP]:
        pollito_y -= pollito_vel
    if keys[pygame.K_DOWN]:
        pollito_y += pollito_vel

    pollito_x = max(0, min(pollito_x, 800 - TAM_CUADRADO))
    pollito_y = max(0, min(pollito_y, 600 - TAM_CUADRADO))

    xx1 += movimiento_derecha1
    xx2 += movimiento_derecha2
    xx3 += movimiento_izquierda3
    xx4 += movimiento_izquierda4
   
    if xx1 >= 800 - TAM_CUADRADO: 
        xx1 = 800 - TAM_CUADRADO  
        movimiento_derecha1 = -MOVIMIENTO_DERECHA  

    if xx2 >= 800 - TAM_CUADRADO: 
        xx2 = 800 - TAM_CUADRADO  
        movimiento_derecha2 = -MOVIMIENTO_DERECHA 
   
    if xx3 <= 0:  
        xx3 = 0  
        movimiento_izquierda3 = MOVIMIENTO_DERECHA  

    if xx4 <= 0:  
        xx4 = 0  
        movimiento_izquierda4 = MOVIMIENTO_DERECHA 

    #  carros
    carros = [
        pygame.Rect(xx1, 160, TAM_CUADRADO, TAM_CUADRADO),
        pygame.Rect(xx2, 230, TAM_CUADRADO, TAM_CUADRADO),
        pygame.Rect(xx3, 315, TAM_CUADRADO, TAM_CUADRADO),
        pygame.Rect(xx4, 390, TAM_CUADRADO, TAM_CUADRADO)
    ]
    
    #  pollito
    pollito_rect = pygame.Rect(pollito_x, pollito_y, TAM_CUADRADO, TAM_CUADRADO)

    # Verificar colisiones
    if detectar_colision(pollito_rect, carros):
        vidas -= 1  
        pollito_x, pollito_y = 375, 500 
        if vidas <= 0:
            print("El pollito ha muerto")
            pygame.quit()
            sys.exit()

    ventana.fill(f)

    # acera
    pygame.draw.rect(ventana, g, ((0, 100), (800, 50)))  
    pygame.draw.rect(ventana, g, ((0, 450), (800, 50)))  


    # techo inferior
    puntos = [(50, 500), (150, 500), (100, 470)]
    pygame.draw.polygon(ventana, r, puntos)
    puntos1 = [(200, 500), (300, 500), (250, 470)]
    pygame.draw.polygon(ventana, r, puntos1)
    puntos2 = [(350, 500), (450, 500), (400, 470)]
    pygame.draw.polygon(ventana, r, puntos2)
    puntos3 = [(500, 500), (600, 500), (550, 470)]
    pygame.draw.polygon(ventana, r, puntos3)
    puntos4 = [(650, 500), (750, 500), (700, 470)]
    pygame.draw.polygon(ventana, r, puntos4)
    # techo superior
    puntos5 = [(50, 100), (150, 100), (100, 130)]
    pygame.draw.polygon(ventana, r, puntos5)
    puntos6 = [(200, 100), (300, 100), (250, 130)]
    pygame.draw.polygon(ventana, r, puntos6)
    puntos7 = [(350, 100), (450, 100), (400, 130)]
    pygame.draw.polygon(ventana, r, puntos7)
    puntos8 = [(500, 100), (600, 100), (550, 130)]
    pygame.draw.polygon(ventana, r, puntos8)
    puntos9 = [(650, 100), (750, 100), (700, 130)]
    pygame.draw.polygon(ventana, r, puntos9)

    # via
    pygame.draw.rect(ventana, v, ((0, 150), (800, 300)))

    # separador de via
    pygame.draw.rect(ventana, a, ((0, 290), (50, 20)))
    pygame.draw.rect(ventana, a, ((150, 290), (50, 20)))
    pygame.draw.rect(ventana, a, ((300, 290), (50, 20)))
    pygame.draw.rect(ventana, a, ((450, 290), (50, 20)))
    pygame.draw.rect(ventana, a, ((600, 290), (50, 20)))
    pygame.draw.rect(ventana, a, ((750, 290), (50, 20)))

    # separador de carril superior
    pygame.draw.line(ventana, n, (0, 220), (50, 220), 5)
    pygame.draw.line(ventana, n, (150, 220), (200, 220), 5)
    pygame.draw.line(ventana, n, (300, 220), (350, 220), 5)
    pygame.draw.line(ventana, n, (450, 220), (500, 220), 5)
    pygame.draw.line(ventana, n, (600, 220), (650, 220), 5)
    pygame.draw.line(ventana, n, (750, 220), (800, 220), 5)

    # seperador de carril inferior
    pygame.draw.line(ventana, n, (0, 370), (50, 370), 5)
    pygame.draw.line(ventana, n, (150, 370), (200, 370), 5)
    pygame.draw.line(ventana, n, (300, 370), (350, 370), 5)
    pygame.draw.line(ventana, n, (450, 370), (500, 370), 5)
    pygame.draw.line(ventana, n, (600, 370), (650, 370), 5)
    pygame.draw.line(ventana, n, (750, 370), (800, 370), 5)

    # Pared de la casa
    pygame.draw.rect(ventana, n, ((50, 500), (100, 100)))
    pygame.draw.rect(ventana, n, ((200, 500), (100, 100)))
    pygame.draw.rect(ventana, n, ((350, 500), (100, 100)))
    pygame.draw.rect(ventana, n, ((500, 500), (100, 100)))
    pygame.draw.rect(ventana, n, ((650, 500), (100, 100)))
    pygame.draw.rect(ventana, n, ((50, 0), (100, 100)))
    pygame.draw.rect(ventana, n, ((200, 0), (100, 100)))
    pygame.draw.rect(ventana, n, ((350, 0), (100, 100)))
    pygame.draw.rect(ventana, n, ((500, 0), (100, 100)))
    pygame.draw.rect(ventana, n, ((650, 0), (100, 100)))

    # puerta
    pygame.draw.rect(ventana, m, ((80, 0), (40, 50)))
    pygame.draw.rect(ventana, m, ((230, 0), (40, 50)))
    pygame.draw.rect(ventana, m, ((380, 0), (40, 50)))
    pygame.draw.rect(ventana, m, ((530, 0), (40, 50)))
    pygame.draw.rect(ventana, m, ((680, 0), (40, 50)))
    pygame.draw.rect(ventana, m, ((80, 550), (40, 50)))
    pygame.draw.rect(ventana, m, ((230, 550), (40, 50)))
    pygame.draw.rect(ventana, m, ((380, 550), (40, 50)))
    pygame.draw.rect(ventana, m, ((530, 550), (40, 50)))
    pygame.draw.rect(ventana, m, ((680, 550), (40, 50)))

    # carros
    pygame.draw.rect(ventana, k, (xx1, 160, 50, 50))  
    pygame.draw.rect(ventana, k, (xx2, 230, 50, 50))  
    pygame.draw.rect(ventana, k, (xx3, 315, 50, 50))  
    pygame.draw.rect(ventana, k, (xx4, 390, 50, 50))

    # pollito
    pygame.draw.rect(ventana, (255, 255, 0), pollito_rect) 
    mostrar_vidas()

    pygame.display.flip()
