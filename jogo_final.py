import pygame

# Inicialização
pygame.init()
tela = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Jogo final 3C")
clock = pygame.time.Clock()

# Jogador
jogador = pygame.Rect(100, 50, 40, 40)

# Adversário (vermelho)
adversario = pygame.Rect(300, 200, 40, 40)
velocidade = 5

# Objetivo (azul)
objetivo = pygame.Rect(500, 300, 40, 40)

# Fonte para mensagens
fonte = pygame.font.SysFont(None, 60)

# Estado do jogo
jogo_ativo = True
mensagem = ""

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    if jogo_ativo:
        # Controles do jogador
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]: jogador.x -= 5
        if teclas[pygame.K_RIGHT]: jogador.x += 5
        if teclas[pygame.K_UP]: jogador.y -= 5
        if teclas[pygame.K_DOWN]: jogador.y += 5

        # Movimento automático do adversário
        adversario.y += velocidade

        # Rebater nas bordas
        if adversario.top <= 0 or adversario.bottom >= 400:
            velocidade *= -1

        # Verifica colisão com o adversário
        if jogador.colliderect(adversario):
            mensagem = "Game Over!"
            jogo_ativo = False

        # Verifica colisão com o objetivo
        if jogador.colliderect(objetivo):
            mensagem = "Você Venceu!"
            jogo_ativo = False

    # Desenho
    tela.fill((0, 0, 0))
    pygame.draw.rect(tela, (0, 255, 0), jogador)
    pygame.draw.rect(tela, (255, 0, 0), adversario)
    pygame.draw.rect(tela, (0, 0, 255), objetivo)

    if not jogo_ativo:
        texto = fonte.render(mensagem, True, (255, 255, 255))
        tela.blit(texto, (200, 150))

    pygame.display.flip()
    clock.tick(60)
