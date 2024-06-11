import pygame
import time
import random

# Inicializa o Pygame
pygame.init()

# Definindo as cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0 , 0 , 255) #opcional
#pode inserir cores diferentes

# Definindo o tamanho da tela
largura_tela = 800
altura_tela = 600

# Inicializando a tela do jogo
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Jogo da Cobrinha")

# Definindo o relógio
relogio = pygame.time.Clock()

# Definindo o tamanho do bloco e a velocidade
tamanho_bloco = 20
velocidade = 15

# Definindo a fonte do jogo
fonte = pygame.font.SysFont(None, 35)


def mensagem(msg, cor):
    texto = fonte.render(msg, True, cor)
    tela.blit(texto, [largura_tela / 6, altura_tela / 3])


def jogo():
    game_over = False
    game_close = False

    x1 = largura_tela / 2
    y1 = altura_tela / 2

    x1_mudanca = 0
    y1_mudanca = 0

    corpo_cobra = []
    comprimento_cobra = 1

    comida_x = round(random.randrange(0, largura_tela - tamanho_bloco) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura_tela - tamanho_bloco) / 20.0) * 20.0

    while not game_over:

        while game_close:
            tela.fill(preto)
            mensagem("Você perdeu! Pressione C-Continuar ou Q-Sair", vermelho)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        jogo()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_mudanca = -tamanho_bloco
                    y1_mudanca = 0
                elif event.key == pygame.K_RIGHT:
                    x1_mudanca = tamanho_bloco
                    y1_mudanca = 0
                elif event.key == pygame.K_UP:
                    y1_mudanca = -tamanho_bloco
                    x1_mudanca = 0
                elif event.key == pygame.K_DOWN:
                    y1_mudanca = tamanho_bloco
                    x1_mudanca = 0
        if x1 >= largura_tela or x1 < 0 or y1 >= altura_tela or y1 < 0:
            game_close = True
        x1 += x1_mudanca #gerar a movimentação de forma semi automatica
        y1 += y1_mudanca
        tela.fill(preto)
        pygame.draw.rect(
            tela, verde, [comida_x, comida_y, tamanho_bloco, tamanho_bloco]
        )
        cabeca_cobra = []
        cabeca_cobra.append(x1)
        cabeca_cobra.append(y1)
        corpo_cobra.append(cabeca_cobra)
        if len(corpo_cobra) > comprimento_cobra:
            del corpo_cobra[0]
        for x in corpo_cobra[:-1]:
            if x == cabeca_cobra:
                game_close = True
        for segmento in corpo_cobra:
            pygame.draw.rect(
                tela, branco, [segmento[0], segmento[1], tamanho_bloco, tamanho_bloco]
            )
        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = (
                round(random.randrange(0, largura_tela - tamanho_bloco) / 20.0) * 20.0
            )
            comida_y = (
                round(random.randrange(0, altura_tela - tamanho_bloco) / 20.0) * 20.0
            )
            comprimento_cobra += 1
        relogio.tick(velocidade)
    pygame.quit()
    quit()


jogo()
