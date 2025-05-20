import pygame
pygame.init()

tela = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Movendo um quadrado")

x, y = 100, 50
velocidade = 5
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

    tela.fill((0, 0, 0))
    pygame.draw.rect(tela, (0, 255, 0), (x, y, 40, 40))
    pygame.display.update()
    relogio.tick(60)

pygame.quit()
