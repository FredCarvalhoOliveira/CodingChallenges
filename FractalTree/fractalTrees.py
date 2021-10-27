import pygame
import math

#Inicia o modulo pygame
pygame.init()

#Cria uma janela
largura = 800
altura  = 600
tamanho = (largura, altura)
janela  =  pygame.display.set_mode(tamanho)
pygame.display.set_caption("Fractal Tree")

#Imagem a mostrar
nova_frame = None

#Tipo de letra do número da frame
#Tamanho
font_size = 25
#Fonte pré-definida
font = pygame.font.Font(None, font_size)
#Suavização
antialias = True
#Cor (tuplo com os valores Red, Green, Blue entre 0 e 255)
WHITE = (255, 255, 255)
BACKGROUND = (20, 20, 20)


#Variável de controlo do ciclo principal
fim = False

nova_frame = pygame.Surface(tamanho)
nova_frame.fill(BACKGROUND)

openAng = 25
sizeFactor = 0.67
branch_init_size = 150
pos_inicial = [int(largura/2), altura - 1]
pos_final = [pos_inicial[0], pos_inicial[1] - branch_init_size]
ang_inicial = -90



def branch(x1, y1, angle, length):
    global nova_frame

    if length > 3:
        x2 = x1 + math.cos(math.radians(angle)) * length
        y2 = y1 + math.sin(math.radians(angle)) * length

        pygame.draw.line(nova_frame, WHITE, (x1, y1), (x2, y2), 3)
        
        branch(x2, y2, angle + openAng, length * sizeFactor)
        branch(x2, y2, angle - openAng, length * sizeFactor)


while not fim:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fim = True

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT]:
        openAng -= 1
    if keys_pressed[pygame.K_RIGHT]:
        openAng += 1
    if keys_pressed[pygame.K_UP]:
        sizeFactor += 0.01
    if keys_pressed[pygame.K_DOWN]:
        sizeFactor -= 0.01

    nova_frame.fill(BACKGROUND)
    branch(pos_inicial[0], pos_inicial[1], ang_inicial, branch_init_size)            

    janela.blit(nova_frame, (0, 0))
    pygame.display.flip()

pygame.quit()
   
