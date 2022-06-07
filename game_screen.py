# ===== Inicialização =====
# ----- Importa e inicia pacotes

from turtle import done
from config import *
from sprites import Chao, Skin, Bola, Placar
import pygame
import random





def game_screen(window):

    # ----- Gera tela principal

    #window = pygame.display.set_mode((WIDTH, HEIGHT))
    #pygame.display.set_caption('Futebol Cabeçudo')
    pygame.font.init() 
    # ----- Inicia assets
    fonte = pygame.font.get_default_font()
    font = pygame.font.SysFont(fonte, 60)
    fonte2 = pygame.font.get_default_font()
    font2 = pygame.font.SysFont(fonte2, 25)
    fonte3 = pygame.font.get_default_font()
    font3 = pygame.font.SysFont(fonte3, 40)
    background = pygame.image.load('background.png').convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    chao_img = pygame.image.load('chao.png').convert()
    chao_img = pygame.transform.scale(chao_img, (1300, 110))

    placar_img = pygame.image.load('placar.png').convert_alpha()
    placar_img = pygame.transform.scale(placar_img, (400, 80))

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
    chao_g = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    # Criando o jogador
    player1 = Skin(skin1_img, sent11, sent12)
    player2 = Skin(skin2_img, sent21, sent22)
    bola = Bola(bola_img)
    chao = Chao(chao_img)
    placar = Placar(placar_img)
    all_sprites.add(chao, player1, player2, placar, bola)
    players.add(player1, player2)
    player1s.add(player1)
    player2s.add(player2)
    bola_g.add(bola)
    chao_g.add(chao)
    p1_gols = 0
    p2_gols = 0
    time = 0
    p_bola = 0

    DONE = 0
    PLAYING = 1
    EXPLODING = 2
    state = PLAYING

    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)
        time += 1
        tempo = 90 - int(time/FPS)
        colisao0 = pygame.sprite.groupcollide(players, bola_g, False, False, pygame.sprite.collide_mask)
        colisao1 = pygame.sprite.groupcollide(player1s, bola_g, False, False, pygame.sprite.collide_mask)
        colisao2 = pygame.sprite.groupcollide(player2s, bola_g, False, False, pygame.sprite.collide_mask)
        colisao3 = pygame.sprite.groupcollide(player1s, player2s, False, False, pygame.sprite.collide_mask)
        colisao4 = pygame.sprite.groupcollide(chao_g, bola_g, False, False, pygame.sprite.collide_mask) 
        # ----- Trata eventos

        if bola.rect.x < 150: 
            p2_gols += 1
            print("Gol do Player 2!!!!")
            print(f"O player 2 está com {p2_gols} gols!")
            bola.rect.x = 630
            bola.speedx = 0
            player1.rect.x = 300
            player1.rect.y = 359
            player2.rect.x = 910
            player2.rect.y = 359
            # player1.speedx = 0
            # player1.speedy = 0
            # player2.speedx = 0
            # player2.speedy = 0
            
        elif bola.rect.x > 1100:
            p1_gols += 1
            print("Gol do Player 1!!!!")
            print(f"O player 1 está com {p1_gols} gols!")
            bola.rect.x = 630
            bola.speedx = 0
            player1.rect.x = 300
            player1.rect.y = 359
            player2.rect.x = 910
            player2.rect.y = 359
            # player1.speedx = 0
            # player1.speedy = 0
            # player2.speedx = 0
            # player2.speedy = 0
            
        
        p2_gols_str = font.render(str(p2_gols),  1, (255,255,255))
        p1_gols_str = font.render(str(p1_gols),  1, (255,255,255))
        temporizador = font3.render(str(tempo), 1, (255,255,0))
        player1_str = font2.render(str('Player 1'), 1, (255,255,255))
        player2_str = font2.render(str('Player 2'), 1, (255,255,255))

        for event in pygame.event.get():
            # ----- Verifica consequências
        
            if event.type == pygame.QUIT:
                state = DONE
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
                if event.key == pygame.K_KP_ENTER:
                    if len(colisao2) > 0:
                        bola.speedx = -20
                if event.key == pygame.K_RSHIFT:
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
                print(colisao0)
            if len(colisao1) > 0:
                if player1.speedx == 0 or player1.speedx > 0 and bola.speedx < 0 or player1.speedx < 0 and bola.speedx <0:
                    bola.speedx = 0
                    bola.rect.x += 0.2*bola.speedx
                    bola.speedy = 0  
                    print(colisao1)
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
            
            if len(colisao1) > 1 and player1.rect.y < 390:
                bola.speedx = 50
                bola.speedy = -30
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
            
            if len(colisao2) and player2.rect.y < 390:
                bola.speedy = -30
                bola.speedx = -50
                
                colisao2 = []

        if len(colisao4) > 0:
            if bola.speedy > 5:
                bola.speedy = - 0.5*bola.speedy
                p_bola += 1
                print("Aconteci")
                if p_bola > 5:
                    bola.speedy = 0
                    bola.rect.y = 390
                    p_bola = 0
                    print("FIZ")
            colisao4 = []

        if len(colisao3) > 0:
            player1.rect.x -= 8
            player2.rect.x += 8 
            
            
        
        all_sprites.update()
        
        
        window.blit(background, (0, 0))
        
        all_sprites.draw(window)
        window.blit(p1_gols_str, (560, 50))
        window.blit(p2_gols_str, (710, 50))
        window.blit(player1_str, (550, 25))
        window.blit(player2_str, (680, 25))
        
        if tempo < 10:
            window.blit(temporizador, (640,62))
        else:
            window.blit(temporizador, (630,62))
        if tempo == 0:
            state = DONE

        pygame.display.update()  # Mostra o novo frame para o jogador

    # ===== Finalização =====
    pygame.quit()  # Função do PyGame que finaliza os recursos utilizados