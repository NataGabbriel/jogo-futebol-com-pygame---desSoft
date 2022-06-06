# ===== Inicialização =====
# ----- Importa e inicia pacotes
from pyparsing import col
from config import WIDTH, HEIGHT, pulo, PLAYER_HEIGHT, PLAYER_WIDTH, SHIP_HEIGHT, SHIP_WIDTH, sent11, sent12, sent21, sent22, FPS
from sprites import Skin, Bola
from email.mime import base
import pygame
import random





pygame.init()

# ----- Gera tela principal

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Futebol Cabeçudo')

# ----- Inicia assets
font = pygame.font.SysFont(None, 48)
background = pygame.image.load('background.png').convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
skin1_img = pygame.image.load('skin1.png').convert_alpha()
skin1_img = pygame.transform.scale(skin1_img, (PLAYER_WIDTH, PLAYER_HEIGHT))
skin2_img = pygame.image.load('skin2.png').convert_alpha()
skin2_img = pygame.transform.scale(skin2_img, (PLAYER_WIDTH, PLAYER_HEIGHT))
bola_img = pygame.image.load('bola55.png').convert_alpha()
bola_img = pygame.transform.scale(bola_img, (PLAYER_WIDTH-45, PLAYER_HEIGHT-31))
game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()


#colisoes
players = pygame.sprite.Group()
player1s = pygame.sprite.Group()
player2s = pygame.sprite.Group()
bola_g = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()

# Criando o jogador
player1 = Skin(skin1_img, sent11, sent12)
player2 = Skin(skin2_img, sent21, sent22)
bola = Bola(bola_img)
all_sprites.add(player1, player2, bola)
players.add(player1, player2)
player1s.add(player1)
player2s.add(player2)
bola_g.add(bola)
player1_gols = 0
player2_gols = 0


# ===== Loop principal =====
while game:
    clock.tick(FPS)

    colisao0 = pygame.sprite.groupcollide(players, bola_g, False, False, pygame.sprite.collide_mask)
    colisao1 = pygame.sprite.groupcollide(player1s, bola_g, False, False, pygame.sprite.collide_mask)
    colisao2 = pygame.sprite.groupcollide(player2s, bola_g, False, False, pygame.sprite.collide_mask)
    colisao3 = pygame.sprite.groupcollide(player1s, player2s, False, False, pygame.sprite.collide_mask)
    colisao4 = pygame.sprite.spritecollide(player1, players, False, pygame.sprite.collide_mask) 
    # ----- Trata eventos
    
    if bola.rect.x < 150:
        player2_gols += 1
        print("Gol do Player 1!!!!")
    elif bola.rect.x > 1100:
        player1_gols += 1
        print("Gol do Player 2!!!!")
    for event in pygame.event.get():
        # ----- Verifica consequências
    
        if event.type == pygame.QUIT:
            game = False
        # Verifica se apertou alguma tecla.
    
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                bola.reset()


        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_a:
                player1.speedx -= 8
            if event.key == pygame.K_d:
                player1.speedx += 8
            if event.key == pygame.K_w:
                player1.pular()
            if event.key == pygame.K_q:
                if len(colisao1) > 0:
                    bola.speedx = 20
            if event.key == pygame.K_e:
                if len(colisao1) > 0:
                    bola.speedx = 50
                    bola.speedy = -30
        
        
        
        
        # Verifica se soltou alguma tecla.
        
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_a:
                player1.speedx += 8
            if event.key == pygame.K_d:
                player1.speedx -= 8
            if event.key == pygame.K_e:
                if len(colisao1) > 0:
                    bola.speedx = 25
                    bola.speedy = 30
        #Player 2





        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player2.speedx -= 8
            if event.key == pygame.K_RIGHT:
                player2.speedx += 8
            if event.key == pygame.K_UP:
                player2.pular()
            if event.key == pygame.K_RSHIFT:
                if len(colisao2) > 0:
                    bola.speedx = -20
            if event.key == pygame.K_KP_ENTER:
                if len(colisao2) > 0:
                    bola.speedx = -50
                    bola.speedy = -30
        
        
        
            
        
       
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player2.speedx += 8
            if event.key == pygame.K_RIGHT:
                player2.speedx -= 8
        
        

    if len(colisao0) > 0:
        if len(colisao1) > 0 and len(colisao2) > 0:
            player1.rect.x -= player1.speedx
            player1.rect.x += player2.speedx
            bola.speedy = -20
        if len(colisao1) > 0:
            if player1.speedx == 0 or player1.speedx > 0 and bola.speedx < 0 or player1.speedx < 0 and bola.speedx <0:
                bola.speedx = 0
                bola.rect.x += 0.2*bola.speedx
                bola.speedy = 0 
                if bola.rect.y < 390:
                    bola.speedy = 5
                
                print ("if 1")
            elif player1.rect.x < bola.rect.x:
                bola.rect.x += 8
                player1.rect.x -= 1
            
                print("Elif 1")
            elif player1.rect.x > bola.rect.x:
                bola.rect.x -= 8
                player1.rect.x += 1
                
                print("Elif 2")
            colisao1 = []           
            
        if len(colisao2) > 0:
            if player2.speedx == 0 or player1.speedx < 0 and bola.speedx > 0 or player1.speedx > 0 and bola.speedx > 0:
                bola.speedx = 0
                bola.speedy = 0
                if bola.rect.y < 390:
                    bola.speedy = 5
                print("if2")
            if player2.rect.x < bola.rect.x:
                bola.rect.x += 8
                player2.rect.x -= 1
                
                
            elif player2.rect.x > bola.rect.x:
                bola.rect.x -= 8
                player2.rect.x += 1
                
                
            colisao2 = []
        #elif len(colisao2) > 0:
        #    bola.speedx -= player2.speedx - 1
    #else:
        #if bola.speedx > 0 and len(colisao0) == 0:
        #    if chute_p1_de == True:
        #        bola.speedx -= 1
        #    if chute_p1_ed == True:
        #        bola.speedx += 1
    if len(colisao3) > 0:
        player1.rect.x -= 8
        player2.rect.x += 8 
        
        
    
    all_sprites.update()

    
    
    window.blit(background, (0, 0))
    all_sprites.draw(window)
    
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados