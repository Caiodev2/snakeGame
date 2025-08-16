def gameOver(x, y, largura, altura, largura_tela=640, altura_tela=480):
    if (x < 0) or (x + largura > largura_tela) or (y < 0) or (y + altura > altura_tela):
        return True  # bateu na borda
    return False