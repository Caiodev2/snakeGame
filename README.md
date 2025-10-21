# 🐍 Python Snake Game (Oficina UFPB)

Este é um projeto do clássico "Snake Game" (Jogo da Cobrinha) desenvolvido em Python utilizando a biblioteca Pygame. O projeto foi criado como material didático para uma oficina de introdução ao desenvolvimento de jogos realizada na Universidade Federal da Paraíba (UFPB), Campus IV - Rio Tinto/Mamanguape.

O código é intencionalmente claro e dividido em um arquivo principal (para o loop do jogo) e um arquivo de biblioteca (`bibFuncoes.py`) para modularizar as funções de lógica.

## ✨ Funcionalidades

* Movimentação da cobra baseada em grade (grid).
* A cobra cresce ao comer uma fruta.
* Contagem de pontuação em tempo real.
* Detecção de colisão com as bordas da tela.
* Detecção de colisão com o próprio corpo da cobra.
* Tela de "Game Over" ao colidir.
* Opção de reiniciar o jogo pressionando a tecla 'R' após o Game Over.
* Velocidade do jogo controlada (10 FPS).

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Pygame** (biblioteca para desenvolvimento de jogos em Python)

## ⚙️ Instalação

1.  Certifique-se de ter o [Python 3](https://www.python.org/downloads/) instalado.

2.  Clone este repositório 

3.  Navegue até o diretório do projeto pelo terminal.

4.  Instale a biblioteca Pygame:
    ```bash
    pip install pygame
    ```

## 🚀 Como Executar

Com o Pygame instalado e os **dois arquivos** (`snake_game.py` e `bibFuncoes.py`) no mesmo diretório, execute o arquivo principal:

```bash
python snake_game.py
