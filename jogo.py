import pygame
import random

# Inicializa o Pygame
pygame.init()

# Configurações do jogo
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")

# Cores
preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (255, 0, 0)
branco = (255, 255, 255)

# Parâmetros da cobra
tamanho_quadrado = 20
velocidade = 10

# Função para exibir a pontuação
def mostrar_pontuacao(pontos):
    fonte = pygame.font.SysFont("arial", 25)
    texto = fonte.render(f"Pontos: {pontos}", True, branco)
    tela.blit(texto, [10, 10])

# Função principal do jogo
def jogo():
    fim_jogo = False
    game_over = False

    # Posição inicial da cobra
    x = largura / 2
    y = altura / 2

    # Velocidade inicial
    dx = 0
    dy = 0

    # Corpo da cobra
    corpo = []
    comprimento = 1

    # Posição inicial da comida
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 20.0) * 20.0

    relogio = pygame.time.Clock()

    while not fim_jogo:

        while game_over:
            tela.fill(preto)
            fonte = pygame.font.SysFont("arial", 35)
            msg = fonte.render("Fim de Jogo! Pressione C para continuar ou Q para sair", True, vermelho)
            tela.blit(msg, [largura / 8, altura / 3])
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        fim_jogo = True
                        game_over = False
                    if evento.key == pygame.K_c:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and dx == 0:
                    dx = -tamanho_quadrado
                    dy = 0
                elif evento.key == pygame.K_RIGHT and dx == 0:
                    dx = tamanho_quadrado
                    dy = 0
                elif evento.key == pygame.K_UP and dy == 0:
                    dy = -tamanho_quadrado
                    dx = 0
                elif evento.key == pygame.K_DOWN and dy == 0:
                    dy = tamanho_quadrado
                    dx = 0

        # Atualiza posição da cobra
        x += dx
        y += dy

        # Verifica colisões
        if x >= largura or x < 0 or y >= altura or y < 0:
            game_over = True

        # Atualiza a tela
        tela.fill(preto)
        pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho_quadrado, tamanho_quadrado])

        # Atualiza o corpo da cobra
        cabeca = []
        cabeca.append(x)
        cabeca.append(y)
        corpo.append(cabeca)
        if len(corpo) > comprimento:
            del corpo[0]

        # Verifica colisão com o próprio corpo
        for segmento in corpo[:-1]:
            if segmento == cabeca:
                game_over = True

        # Desenha a cobra
        for segmento in corpo:
            pygame.draw.rect(tela, verde, [segmento[0], segmento[1], tamanho_quadrado, tamanho_quadrado])

        # Verifica se a cobra comeu a comida
        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 20.0) * 20.0
            comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 20.0) * 20.0
            comprimento += 1

        # Exibe pontuação
        mostrar_pontuacao(comprimento - 1)

        pygame.display.update()
        relogio.tick(velocidade)

    pygame.quit()
    quit()

jogo()
