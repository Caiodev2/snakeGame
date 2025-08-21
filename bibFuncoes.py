import random

def colisao_borda(x, y, largura, altura, largura_tela=640, altura_tela=480):
    if (x < 0) or (x + largura > largura_tela) or (y < 0) or (y + altura > altura_tela):
        return True  # bateu na borda
    return False


def nova_maca(GRID = 20,tela_w = 640, tela_h = 480):
    x = random.randrange(0, tela_w - GRID, GRID)
    y = random.randrange(0, tela_h - GRID, GRID)
    return x, y

def colisao_cobra(c):
   if len(c) < 2:
       return False
   cabeca = c[0]
   corpo = c[1:]

   return cabeca in corpo