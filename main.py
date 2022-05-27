# ===== Inicialização =====
# ----- Importa e inicia pacotes
from email.mime import base
import pygame
import random

pygame.init()

# ----- Gera tela principal
WIDTH = 1300
HEIGHT = 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Futebol Cabeçudo')

# ----- Inicia assets
PLAYER_WIDTH = 90
PLAYER_HEIGHT = 66
SHIP_WIDTH = 50
SHIP_HEIGHT = 38
font = pygame.font.SysFont(None, 48)
background = pygame.image.load('background.png').convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
skin1_img = pygame.image.load('skin1.png').convert_alpha()
skin1_img = pygame.transform.scale(skin1_img, (PLAYER_WIDTH, PLAYER_HEIGHT))
skin2_img = pygame.image.load('skin2.png').convert_alpha()
skin2_img = pygame.transform.scale(skin2_img, (PLAYER_WIDTH, PLAYER_HEIGHT))
bola_img = pygame.image.load('bola55.png').convert_alpha()
bola_img = pygame.transform.scale(bola_img, (PLAYER_WIDTH-45, PLAYER_HEIGHT-31))
operador = True
pulo = 75


# ----- Inicia estruturas de dados
# Definindo os novos tipos
class Skin1(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH / 2) - 100
        self.rect.bottom = HEIGHT -75
        self.speedx = 0
        self.speedy = 0
        self.pulando = False
        
    def update(self):
        
        # Atualização da posição da nave
        self.rect.x += self.speedx
        
        self.rect.y += self.speedy
            
        if self.rect.y < 359:
            
            self.rect.y += 10
            
            
        # Mantem dentro da tela
        if self.rect.right > WIDTH - 150:
            self.rect.right = WIDTH - 150
        if self.rect.left < 150:
            self.rect.left = 150
        if self.rect.y < 249:
            self.speedy = 0
             
        if self.rect.y >= 349:
            self.pulando = False

    def pular(self):
        if not self.pulando:
            self.speedy -= pulo
            self.pulando = True


class Skin2(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH / 2) + 100
        self.rect.bottom = HEIGHT -75
        self.speedx = 0
        self.speedy = 0

    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx
        
        self.rect.y += self.speedy
            
        if self.rect.y < 359:
            
            self.rect.y += 10
        
        # Mantem dentro da tela
        if self.rect.right > WIDTH - 150 :
            self.rect.right = WIDTH - 150
        if self.rect.left < 150:
            self.rect.left = 150
        if self.rect.y < 249:
            self.speedy = 0
             
        if self.rect.y >= 349:
            self.pulando = False

    def pular(self):
        if not self.pulando:
            self.speedy -= pulo
            self.pulando = True

class Bola(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH / 2)
        self.rect.bottom = HEIGHT -75
        self.speedy = 0
        self.speedx = 0

        # Mantem dentro da tela
        if self.rect.right > WIDTH - 140 :
            self.rect.right = WIDTH - 140
        if self.rect.left < 140:
            self.rect.left = 140
        if self.rect.y < 249:
            self.speedy = 0
        #if self.rect.y < 100:
        #   self.speedy += 2

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        if self.rect.right > WIDTH - 65 :
            self.rect.right = WIDTH - 65
        if self.rect.left < 65:
            self.rect.left = 65
        if self.rect.y < 249:
            self.speedy -= 10

game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30

#colisoes
player1s = pygame.sprite.Group()
player2s = pygame.sprite.Group()
bolas = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()

# Criando o jogador
player1 = Skin1(skin1_img)
player2 = Skin2(skin2_img)
bola = Bola(bola_img)
all_sprites.add(player1,player2)
all_sprites.add(bola)
bolas.add(bola)



# ===== Loop principal =====
while game:
    clock.tick(FPS)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
    
        if event.type == pygame.QUIT:
            game = False
        # Verifica se apertou alguma tecla.
    
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_a:
                player1.speedx -= 8
            if event.key == pygame.K_d:
                player1.speedx += 8
            
            if event.key == pygame.K_w:
                player1.pular()
        # Verifica se soltou alguma tecla.
        
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_a:
                player1.speedx += 8
            if event.key == pygame.K_d:
                player1.speedx -= 8
            
        #Player 2

        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player2.speedx -= 8
            if event.key == pygame.K_RIGHT:
                player2.speedx += 8
            if event.key == pygame.K_UP:
                player2.pular()

        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player2.speedx += 8
            if event.key == pygame.K_RIGHT:
                player2.speedx -= 8

    colisao1 = pygame.sprite.spritecollide(player1, bolas, False)
    colisao2 = pygame.sprite.spritecollide(player2, bolas, False)
    #colisao3 = pygame.sprite.groupcollide(player1, player2, False)
    
    if len(colisao1) > 0:
        bola.speedx = 0
        bola.speedx += 7
        bola.speedy -= 0
        colisao1 = []
    if len(colisao2) > 0:
        bola.speedx = 0
        bola.speedx -= 7
        bola.speedy -= 0
        colisao2 = []

    #if len(colisao3) > 0:
    #   player1.speedx = 1
    #    player2.speedx = 1
    #    colisao3 = []

    # ----- Atualiza estado do jogo
    
    
    all_sprites.update()

    
    # ----- Gera saídas
    #window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    all_sprites.draw(window)#window.blit(skin1_img, (550, 360))
    # Desenhando meteoros
    #all_sprites.draw(window)

    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

