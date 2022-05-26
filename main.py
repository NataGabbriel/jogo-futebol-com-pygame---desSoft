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
METEOR_WIDTH = 90
METEOR_HEIGHT = 66
SHIP_WIDTH = 50
SHIP_HEIGHT = 38
font = pygame.font.SysFont(None, 48)
background = pygame.image.load('background.png').convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
skin1_img = pygame.image.load('skin1.png').convert_alpha()
skin1_img = pygame.transform.scale(skin1_img, (METEOR_WIDTH, METEOR_HEIGHT))
skin2_img = pygame.image.load('skin2.png').convert_alpha()
skin2_img = pygame.transform.scale(skin2_img, (METEOR_WIDTH, METEOR_HEIGHT))
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
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
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
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.y < 249:
            self.speedy = 0
             
        if self.rect.y >= 349:
            self.pulando = False

    def pular(self):
        if not self.pulando:
            self.speedy -= pulo
            self.pulando = True


game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30


all_sprites = pygame.sprite.Group()
# Criando o jogador
player1 = Skin1(skin1_img)
player2 = Skin2(skin2_img)
all_sprites.add(player1,player2)

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

