import pygame

# Inicialização
pygame.init()
tela = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

# Jogador
jogador = pygame.Rect(100, 50, 40, 40)

# Adversário
adversario = pygame.Rect(300, 200, 40, 40)
velocidade = 5

# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Controles do jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]: jogador.x -= 5
    if teclas[pygame.K_RIGHT]: jogador.x += 5
    if teclas[pygame.K_UP]: jogador.y -= 5
    if teclas[pygame.K_DOWN]: jogador.y += 5

    # Movimento automático do adversário
    adversario.x += velocidade

    # Rebater nas bordas
    if adversario.right >= 600 or adversario.left <= 0:
        velocidade *= -1

    # Verifica colisão
    if jogador.colliderect(adversario):
        print("Colidiu!")

    # Desenho
    tela.fill((0, 0, 0))
    pygame.draw.rect(tela, (0, 255, 0), jogador)
    pygame.draw.rect(tela, (255, 0, 0), adversario)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
