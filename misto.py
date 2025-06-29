import pygame
from sys import exit

# Inicialização
pygame.init()
tela = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Jogo com Sprite")
clock = pygame.time.Clock()

# Cores
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
PRETO = (0, 0, 0)

# Adversário
adversario = pygame.Rect(300, 200, 40, 40)
velocidade = 5

# Objetivo
objetivo = pygame.Rect(500, 300, 40, 40)

# Fonte para mensagens
fonte = pygame.font.SysFont(None, 60)

# Estado do jogo
jogo_ativo = True
mensagem = ""

# --- NOVO: CLASSE JOGADOR COM SPRITE ---
class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprites = [
            pygame.image.load("Walking.png"),
            pygame.image.load("Walking2.png"),
            pygame.image.load("Walking3.png"),
            pygame.image.load("Walking4.png"),
        ]
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(topleft=(100, 50))
        self.animar = False

    def update(self, teclas):
        self.animar = False
        if teclas[pygame.K_LEFT]:
            self.rect.x -= 5
            self.animar = True
        if teclas[pygame.K_RIGHT]:
            self.rect.x += 5
            self.animar = True
        if teclas[pygame.K_UP]:
            self.rect.y -= 5
            self.animar = True
        if teclas[pygame.K_DOWN]:
            self.rect.y += 5
            self.animar = True

        # Animação
        if self.animar:
            self.atual += 0.3
            if self.atual >= len(self.sprites):
                self.atual = 0
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (40, 40))

# Criação do sprite jogador
jogador = Jogador()
grupo_jogador = pygame.sprite.Group()
grupo_jogador.add(jogador)

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    if jogo_ativo:
        teclas = pygame.key.get_pressed()
        jogador.update(teclas)

        # Movimento adversário
        adversario.y += velocidade
        if adversario.top <= 0 or adversario.bottom >= 400:
            velocidade *= -1

        # Colisão com adversário
        if jogador.rect.colliderect(adversario):
            mensagem = "Game Over!"
            jogo_ativo = False

        # Colisão com objetivo
        if jogador.rect.colliderect(objetivo):
            mensagem = "Você Venceu!"
            jogo_ativo = False

    # Desenho
    tela.fill(PRETO)
    pygame.draw.rect(tela, VERMELHO, adversario)
    pygame.draw.rect(tela, AZUL, objetivo)
    grupo_jogador.draw(tela)

    if not jogo_ativo:
        texto = fonte.render(mensagem, True, (255, 255, 255))
        tela.blit(texto, (200, 150))

    pygame.display.flip()
    clock.tick(60)
