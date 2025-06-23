import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480

PRETO = (0, 0, 0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Sprites')


class Homem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('Walking.png'))
        self.sprites.append(pygame.image.load('Walking2.png'))
        self.sprites.append(pygame.image.load('Walking3.png'))
        self.sprites.append(pygame.image.load('Walking4.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (108 * 3, 102 * 3))

        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100

        self.animar = False

    def andar(self):
        self.animar = True

    def update(self):
        if self.animar == True:
            self.atual = self.atual + 0.5
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (108 * 3, 102 * 3))


todas_as_sprites = pygame.sprite.Group()
homem = Homem()
todas_as_sprites.add(homem)

relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill(PRETO)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            homem.andar()

    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()