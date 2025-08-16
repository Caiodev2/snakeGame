import time
import pygame
from random import randint
from bibFuncoes import gameOver


#cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO= (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)


#iniciando o pygames
pygame.init()

#definindo tela
tela_w, tela_h = 640, 480
tela = pygame.display.set_mode((tela_w,tela_h))
pygame.display.set_caption("Jogo da cobra")

#Definindo fonte e mensagens
fonteGamerOver = pygame.font.SysFont(None,50)
textoGamerOver = fonteGamerOver.render("GAME OVER",True, VERMELHO)
txtGamerOver_w, txtGamerOver_h = textoGamerOver.get_size()

fontePrecionarR = pygame.font.SysFont(None,30)
textoPrecionarR = fontePrecionarR.render("Precione R para retornar",True,BRANCO)


#posicao centralizada
x = (tela_w - txtGamerOver_w) // 2
y = (tela_h - txtGamerOver_h) // 2


#cobra tamanho
cordX,cordY = x,y 
largura,altura = 20,20
movimento = "direita" #sempre comecar seguindo a direita
velocidade = 5

#fps
clock = pygame.time.Clock()


#main

controlador = True
while controlador:


    tela.fill(PRETO)
    pygame.draw.rect(tela, VERDE, [cordX, cordY, largura, altura])
    pygame.display.flip()


    for acao in pygame.event.get():
        if acao.type == pygame.QUIT:
            controlador = False

        if acao.type == pygame.KEYDOWN:
            
            if acao.key == pygame.K_UP:
                movimento = "cima"
            elif acao.key == pygame.K_DOWN:
                movimento = "baixo"
            elif acao.key == pygame.K_LEFT:
                movimento = "esquerda"
            elif acao.key == pygame.K_RIGHT:
                movimento = "direita"

    # Atualiza posição

    if(gameOver(cordX,cordY,largura,altura) != True):

        if movimento == "cima":
            cordY -= velocidade
        elif movimento == "baixo":
            cordY += velocidade
        elif movimento == "esquerda":
            cordX -= velocidade
        elif movimento == "direita":
            cordX += velocidade
    else:

        tela.blit(textoGamerOver,[x,y])
        tela.blit(textoPrecionarR,[x,300])
        pygame.display.flip()

        esperando = True
        while esperando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    controlador = False
                    esperando = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_r:
                        # Reinicia posição e direção
                        cordX,cordY = x,y 
                        movimento = "direita"
                        esperando = False



    pygame.display.flip()
    clock.tick(30)  # controla FPS



