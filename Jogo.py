import pygame
import os
import sys
os.chdir('C:\\Users\\) #Coloque o diretório onde estão os arquivos do jogo
pygame.init()

WIDTH = 960
HEIGHT = 540
VELOCIDADE_JOGO = 8
SPACE_WIDTH = 2 * WIDTH
POS_X_NAVE = 0
POS_Y_NAVE = 244
POS_MUDAR_NAVE_X = 0
POS_MUDAR_NAVE_Y = 0
clock = pygame.time.Clock()

TELA = pygame.display.set_mode((WIDTH, HEIGHT))
PAPEL_DE_PAREDE = pygame.image.load('space.png')
nave = pygame.image.load('nave.png')
nave = pygame.transform.scale(nave, (160, 52))

#tiro da nave
bullet = pygame.image.load('bullet.png')
bullet = pygame.transform.scale(bullet, (56, 40))
bulletX = POS_X_NAVE + 100
bulletY = POS_Y_NAVE
bulletX_Travel = 10
bulletY_Travel = 0
bulletState = "pronto"

class Space_move(pygame.sprite.Sprite):

    def __init__(self, posicaoX):
        pygame.sprite.Sprite.__init__(self)

        self.image = PAPEL_DE_PAREDE
        self.image = pygame.transform.scale(self.image, (SPACE_WIDTH, HEIGHT))

        self.rect = self.image.get_rect()
        self.rect[0] = posicaoX

    def update(self):
        self.rect[0] -= VELOCIDADE_JOGO

def is_off_screen(sprite):
    return sprite.rect[0] < -(sprite.rect[2])

def atirar_bala(x, y):
    global bulletState
    bulletState = "atirar"
    TELA.blit(bullet, (x + 135, y - 5))

space_move_group = pygame.sprite.Group()
for i in range(2):
    space_move = Space_move(SPACE_WIDTH * i)
    space_move_group.add(space_move)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                POS_MUDAR_NAVE_X = 50
                POS_X_NAVE += POS_MUDAR_NAVE_X
            if event.key == pygame.K_a:
                POS_MUDAR_NAVE_X = -50
                POS_X_NAVE += POS_MUDAR_NAVE_X
            if event.key == pygame.K_w:
                POS_MUDAR_NAVE_Y = -50
                POS_Y_NAVE += POS_MUDAR_NAVE_Y
            if event.key == pygame.K_s:
                POS_MUDAR_NAVE_Y = 50
                POS_Y_NAVE += POS_MUDAR_NAVE_Y
            if event.key == pygame.K_SPACE:
                if bulletState is "pronto":
                    bulletX = POS_X_NAVE
                    bulletY = POS_Y_NAVE
                    atirar_bala(bulletX, bulletY)

    clock.tick(60)

    TELA.fill((0, 0, 0))

    space_move_group.update()

    space_move_group.draw(TELA)
    TELA.blit(nave, (POS_X_NAVE, POS_Y_NAVE))

    if is_off_screen(space_move_group.sprites()[0]):
        space_move_group.remove(space_move_group.sprites()[0])

        new_space = Space_move(SPACE_WIDTH - 20)
        space_move_group.add(new_space)
    
    if bulletX >= 940:
        bulletX = 0
        bulletState = "pronto"

    if bulletState is "atirar":
        atirar_bala(bulletX, bulletY)
        bulletX += bulletX_Travel
    
    pygame.display.update()
