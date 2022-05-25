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

'''
ship_img = pygame.image.load('assets/img/playerShip1_orange.png').convert_alpha()
ship_img = pygame.transform.scale(ship_img, (SHIP_WIDTH, SHIP_HEIGHT))
'''

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
        
    def update(self):
        
        # Atualização da posição da nave
        self.rect.x += self.speedx
        
        self.rect.y += self.speedy
            
        if self.rect.y < 359:
            self.rect.y += 15

        
        
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.y < 314:
            self.speedy += 45
            operador = False

class Skin2(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH / 2) + 100
        self.rect.bottom = HEIGHT -75
        self.speedx = 0

    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

'''
class Meteor(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-METEOR_WIDTH)
        self.rect.y = random.randint(-100, -METEOR_HEIGHT)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-METEOR_WIDTH)
            self.rect.y = random.randint(-100, -METEOR_HEIGHT)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)
'''
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
            if event.key == pygame.K_w and operador == True:
                player1.speedy -= 45
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_a:
                player1.speedx += 8
            if event.key == pygame.K_d:
                player1.speedx -= 8
            if event.key == pygame.K_w:
                operador = True
        
        
            
        

        
        #Player 2
    
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player2.speedx -= 8
            if event.key == pygame.K_RIGHT:
                player2.speedx += 8
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

