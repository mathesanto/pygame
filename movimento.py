import pygame

# Inicialização
pygame.init()
tela = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

# Quadrado
quadrado = pygame.Rect(100, 250, 50, 50)
velocidade = 5

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()

    # Movimento automático (horizontal)
    quadrado.x += velocidade

    # Rebater nas bordas
    if quadrado.right >= 600 or quadrado.left <= 0:
        velocidade *= -1

    # Desenho
    tela.fill((0, 0, 0))  # Limpa a tela
    pygame.draw.rect(tela, (255, 0, 0), quadrado)
    pygame.display.flip()
    clock.tick(60)  # 60 FPS
