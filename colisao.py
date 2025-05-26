import pygame

pygame.init()

tela = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Movendo um quadrado")

# Posição do jogador
x, y = 100, 50
velocidade = 5

# Posição do adversário (fixo)
adversario_x = 300
adversario_y = 200

relogio = pygame.time.Clock()

rodando = True
while rodando:
    pygame.time.delay(30)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]: x -= velocidade
    if teclas[pygame.K_RIGHT]: x += velocidade
    if teclas[pygame.K_UP]: y -= velocidade
    if teclas[pygame.K_DOWN]: y += velocidade

    # Cria retângulos para detectar colisão
    ret_jogador = pygame.Rect(x, y, 40, 40)
    ret_adversario = pygame.Rect(adversario_x, adversario_y, 40, 40)

    # Verifica se colidiram
    if ret_jogador.colliderect(ret_adversario):
        print("Colidiu!")

    tela.fill((0, 0, 0))
    pygame.draw.rect(tela, (0, 255, 0), (x, y, 40, 40))
    pygame.draw.rect(tela, (255, 0, 0), (adversario_x, adversario_y, 40, 40))  # Adversário (vermelho)

    pygame.display.update()
    relogio.tick(60)

pygame.quit()
