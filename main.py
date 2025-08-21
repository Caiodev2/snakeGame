import pygame
from bibFuncoes import colisao_borda  
from bibFuncoes import nova_maca
from bibFuncoes import colisao_cobra


# Cores 
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)

#iniciando pygame
pygame.init()


#pontuacao
pontos = 0


# configracao da tela
tela_w = 640
tela_h = 480
GRID = 20 
tela = pygame.display.set_mode((tela_w, tela_h))
pygame.display.set_caption("Jogo da cobra")

# fontes e textos 
fonteGamerOver = pygame.font.SysFont(None, 50)
textoGamerOver = fonteGamerOver.render("GAME OVER", True, VERMELHO)
txtGamerOver_w, txtGamerOver_h = textoGamerOver.get_size()

fontePressioneR = pygame.font.SysFont(None, 30)
textoPressioneR = fontePressioneR.render("Pressione R para retornar", True, BRANCO)

fontePontos = pygame.font.SysFont(None, 25)
textoPontos = fontePontos.render(f"PONTOS: {pontos}",True, BRANCO)

# posição centralizada dos textos 
centro_texto_x = (tela_w - txtGamerOver_w) // 2
centro_texto_y = (tela_h - txtGamerOver_h) // 2



# --- Estado inicial ---
cordX = (tela_w // GRID // 2) * GRID
cordY = (tela_h // GRID // 2) * GRID
largura, altura = GRID, GRID
movimento = "direita" #começar sempre na direita
velocidade = GRID 


#cobra estado inicial
cobra = [[cordX,cordY]]
tamanho_cobra = 1


macaX, macaY = nova_maca()
clock = pygame.time.Clock()


#--------------Main---------------
controlador = True
while controlador:

    #eventos das teclas
    for acao in pygame.event.get():
        if acao.type == pygame.QUIT:
            controlador = False

        if acao.type == pygame.KEYDOWN:
            if acao.key == pygame.K_UP and movimento != "baixo":
                movimento = "cima"
            elif acao.key == pygame.K_DOWN and movimento != "cima":
                movimento = "baixo"
            elif acao.key == pygame.K_LEFT and movimento != "direita":
                movimento = "esquerda"
            elif acao.key == pygame.K_RIGHT and movimento != "esquerda":
                movimento = "direita"

    #movimento ou game over
    print(colisao_borda(cordX, cordY, largura, altura))
    if not colisao_borda(cordX, cordY, largura, altura) and not colisao_cobra(cobra):
        if movimento == "cima":
            cordY -= velocidade
        elif movimento == "baixo":
            cordY += velocidade
        elif movimento == "esquerda":
            cordX -= velocidade
        elif movimento == "direita":
            cordX += velocidade
        cobra.append([cordX, cordY])
        
    else:
        # tela de game over + espera por R
        tela.fill(PRETO)
        tela.blit(textoGamerOver, [centro_texto_x, centro_texto_y])
        tela.blit(textoPressioneR, [centro_texto_x, centro_texto_y + 60])
        pygame.display.flip()

        esperando = True
        while esperando:

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    controlador = False
                    esperando = False
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_r:
                    # reinicia tudo alinhado pra grade
                    cordX = (tela_w // GRID // 2) * GRID
                    cordY = (tela_h // GRID // 2) * GRID
                    movimento = "direita"
                    macaX, macaY = nova_maca()
                    tamanho_cobra = 1
                    cobra = []
                    pontos = 0

                    esperando = False


    #crescer conforme come a maçã
    if len(cobra) > tamanho_cobra:
        del cobra[0]

    #colisão com a maçã 
    if (cordX == macaX) and (cordY == macaY):
        macaX, macaY = nova_maca()
        pontos +=1
        tamanho_cobra +=1

    #desenho
    tela.fill(PRETO)
    print(cobra)

    #desenhando cada segmento da cobra
    for segmento in cobra:
        pygame.draw.rect(tela, VERDE, [segmento[0], segmento[1], largura, altura])

    pygame.draw.ellipse(tela, VERMELHO, [macaX, macaY, GRID, GRID])# maçã

    textoPontos = fontePontos.render(f"PONTOS: {pontos}",True, BRANCO)
    tela.blit(textoPontos,[centro_texto_x - 180,centro_texto_y -220]) #x=320 y=240
    pygame.display.flip()

    clock.tick(10)  #fps

pygame.quit()
