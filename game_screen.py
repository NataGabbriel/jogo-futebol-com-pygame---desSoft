# ===== Inicialização =====
# ----- Importa e inicia pacotes

from turtle import delay, done
from config import *
from sprites import Chao, Skin, Bola, Placar
import pygame
import random





def game_screen(window):
    """Função da tela do jogo"""

    # ----- Gera tela principal

    
    pygame.font.init() 
    
    # ----- Inicia imagens, fontes e músicas
    fonte = pygame.font.get_default_font()
    font = pygame.font.SysFont(fonte, 60)
    fonte2 = pygame.font.get_default_font()
    font2 = pygame.font.SysFont(fonte2, 25)
    fonte3 = pygame.font.get_default_font()
    font3 = pygame.font.SysFont(fonte3, 40)
    fonte4 = pygame.font.get_default_font()
    font4 = pygame.font.SysFont(fonte4, 40)
    fonte5 = pygame.font.get_default_font()
    font5 = pygame.font.SysFont(fonte3, 70)
    background = pygame.image.load('background.png').convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    gol =  pygame.image.load('gol.png').convert_alpha()
    gol = pygame.transform.scale(gol, (500, 220))
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
    
    # Carrega os sons do jogo
    pygame.mixer.music.load('torcida.mpeg')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1)
    gol_sound = pygame.mixer.Sound('gol2.mpeg')
    apito_sound = pygame.mixer.Sound('apito.mpeg')
    
    
    
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()


    # Criando os sprites e os grupos de sprites
    players = pygame.sprite.Group()
    player1s = pygame.sprite.Group()
    player2s = pygame.sprite.Group()
    bola_g = pygame.sprite.Group()
    chao_g = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    
    
    player1 = Skin(skin1_img, sent11, sent12)
    player2 = Skin(skin2_img, sent21, sent22)
    bola = Bola(bola_img)
    chao = Chao(chao_img)
    placar = Placar(placar_img)
    all_sprites.add(chao, player2, player1,  placar, bola)
    players.add(player1, player2)
    player1s.add(player1)
    player2s.add(player2)
    bola_g.add(bola)
    chao_g.add(chao)

    # Cria as variáveis do jogo

    p1_gols = 0
    p2_gols = 0
    time = 0
    p_bola = 0
    p1_gols_str = ()
    p1_gols_str = ()
    player1_str = ()
    player2_str = ()
    cont2 = 0
    gool = False
    DONE = 0
    PLAYING = 1
    TIME = 2
    GOOL = 3
    state = PLAYING

    # ===== Loop principal =====
   
    while state != DONE:
        
        # Inicia com o som de um apito
        if time==0:
            apito_sound.play()
        
        # Condicional do fim de jogo - aba onde aparece o vencedor e dá a escolha de jogar novamente ou não.
        if state == TIME:
            clock.tick(60)
            time += 1
            tempo = int(time/FPS)
            
            if p2_gols > p1_gols:
                
                window.blit(background, (0, 0))
                p2_vence = font5.render(str("O player 2 venceu o jogo!"), 1, (255,150,0))
                window.blit(p2_vence, (350, 150))
            
            if p1_gols > p2_gols:

                window.blit(background, (0, 0))
                p1_vence = font5.render(str("O player 1 venceu o jogo!"), 1, (255,150,0))
                window.blit(p1_vence, (350, 150))
            
            if p1_gols == p2_gols:
                window.blit(background, (0, 0))
                empata1 = font5.render(str("Jogo de pato é assim mesmo,"), 1, (255,150,0))
                window.blit(empata1, (300, 110))
                empata2 = font5.render(str("termina empatado!"), 1, (255,150,0))
                window.blit(empata2, (400, 160))    

            window.blit(placar.image, placar.rect)
            window.blit(p1_gols_str, (560, 50))
            window.blit(p2_gols_str, (710, 50))
            window.blit(player1_str, (550, 25))
            window.blit(player2_str, (680, 25))
            if tempo % 2 == 0:
                jogar_dnv = font4.render(str("Aperte espaço para jogar de novo!"), 1, (255,255, 255))
                window.blit(jogar_dnv, (425, 450))
            
            for event in pygame.event.get():
                # ----- Verifica consequências
            
                if event.type == pygame.QUIT:
                    state = DONE
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        state = PLAYING
                        
                        time = 0
                        p1_gols = 0
                        p2_gols = 0
                        time = 0
                        p_bola = 0
                        bola.reset()
                        player1.speedx = 0
                        player1.speedy = 0
                        player2.speedx = 0
                        player2.speedy = 0
                        player1.reset(sent11, sent12)
                        player2.reset(sent21, sent22)
           
        
            pygame.display.update()  # Mostra o novo frame para o jogador
            
        # Condicional do início do jogo - o sistema entra nesse if até o tempo do jogo acabar
        if state == PLAYING:
            clock.tick(FPS)
            
            # Cria contador do tempo
            time += 1
            tempo = 90 - int(time/FPS)


            #Cria as colisões
            colisao0 = pygame.sprite.groupcollide(players, bola_g, False, False, pygame.sprite.collide_mask)
            colisao1 = pygame.sprite.groupcollide(player1s, bola_g, False, False, pygame.sprite.collide_mask)
            colisao2 = pygame.sprite.groupcollide(player2s, bola_g, False, False, pygame.sprite.collide_mask)
            colisao3 = pygame.sprite.groupcollide(player1s, player2s, False, False, pygame.sprite.collide_mask)
            colisao4 = pygame.sprite.groupcollide(chao_g, bola_g, False, False, pygame.sprite.collide_mask) 
            # ----- Trata eventos
            
            # Verifica a ocorrência de gols e reseta a posição da bola e dos jogadores se houver.
            if bola.rect.x < 150: 
                gool = True
                p2_gols += 1
                
                
                bola.reset()
                player1.reset(sent11, sent12)
                player2.reset(sent21, sent22)
                bola.tocar()
                window.blit(gol, (680, 25))
                
                
                
            elif bola.rect.x > 1100:
                gool = True
                p1_gols += 1
                
                
                bola.reset()
                player1.reset(sent11, sent12)
                player2.reset(sent21, sent22)
                bola.tocar()
                window.blit(gol, (680, 25))
                cont2 += 1
                
            # Renderiza o texto do placar (gols, tempo e players)
            p2_gols_str = font.render(str(p2_gols),  1, (255,255,255))
            p1_gols_str = font.render(str(p1_gols),  1, (255,255,255))
            temporizador = font3.render(str(tempo), 1, (255,255,0))
            player1_str = font2.render(str('Player 1'), 1, (255,255,255))
            player2_str = font2.render(str('Player 2'), 1, (255,255,255))

            # Verifica entradas e roda o jogo de acordo com elas
            for event in pygame.event.get():
                # ----- Verifica consequências

                #Botão para sair
                if event.type == pygame.QUIT:
                    state = DONE
                
            
                # Botão de reset da bola
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        bola.reset()
                        apito_sound.play()

                # Jogador 1
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
                            bola.speedx = 30
                    if event.key == pygame.K_e:
                        if len(colisao1) > 0:
                            bola.speedx = 30
                            bola.speedy = -20
                
                
                
                
                # Verifica se soltou alguma tecla.
                
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key == pygame.K_a:
                        player1.speedx += 8
                    if event.key == pygame.K_d:
                        player1.speedx -= 8
                    




                #Jogador 2
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
                            bola.speedx = -30
                    if event.key == pygame.K_RSHIFT:
                        if len(colisao2) > 0:
                            bola.speedx = -30
                            bola.speedy = -20
                
                
                
                    
                
            
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key == pygame.K_LEFT:
                        player2.speedx += 8
                    if event.key == pygame.K_RIGHT:
                        player2.speedx -= 8
                
                
            # Verifica a ocorrência das colisões e executa os comandos necessários para cada uma delas

            # Colisão dos jogadores com a bola
            if len(colisao0) > 0:

                # Colisão ao mesmo tempo dos dois jogadores e a bola
                if len(colisao1) > 0 and len(colisao2) > 0:
                    player1.rect.x -= player1.speedx
                    player1.rect.x += player2.speedx
                    bola.speedy = -50
                    
                
                # Colisão do jogador 1 e a bola
                if len(colisao1) > 0:
                    if player1.speedx == 0  or player1.speedx > 0 and bola.speedx < 0 or player1.speedx < 0 and bola.speedx < 0:
                        if player1.rect.y == 359:
                            bola.speedx = 0
                            bola.speedy = 0  
                            
                            colisao0 = []
                            colisao1 = []
                            colisao2 = []
                            if bola.rect.y < 390:
                                bola.speedy = 5
                                colisao0 = []
                                colisao1 = []
                                colisao2 = []
                        else: 
                            bola.speedx = -0.7*bola.speedx
                            colisao0 = []
                            colisao1 = []
                            colisao2 = []
                        
                        
                    elif player1.rect.x < bola.rect.x:
                        bola.rect.x += 8
                        player1.rect.x -= 0
                        colisao0 = []
                        colisao1 = []

                        
                    elif player1.rect.x > bola.rect.x:
                        bola.rect.x -= 8
                        player1.rect.x += 0
                        colisao0 = []
                        colisao1 = []

                        
                    colisao1 = []    
                
                
                # Colisão do jogador 2 e a bola
                if len(colisao2) > 0:
                    if player2.speedx == 0 or player1.speedx < 0 and bola.speedx > 0 or player1.speedx > 0 and bola.speedx > 0:
                        if player2.rect.y == 359:
                            bola.speedx = 0
                            bola.speedy = 0  
                            
                            colisao0 = []
                            colisao1 = []
                            colisao2 = []
                            if bola.rect.y < 390:
                                bola.speedy = 5
                                colisao0 = []
                                colisao1 = []
                                colisao2 = []
                        else: 
                            bola.speedx = -0.7*bola.speedx
                            colisao0 = []
                            colisao1 = []                
                            colisao2 = []


                    elif player2.rect.x < bola.rect.x:
                        bola.rect.x += 8
                        player2.rect.x -= 0
                        colisao0 = []
                        colisao2 = []
                        
                    elif player2.rect.x > bola.rect.x:
                        bola.rect.x -= 8
                        player2.rect.x += 0
                        if player2.speedx > 0:
                            bola.speedx = 0
                        colisao0 = []
                        colisao2 = []
                        
                    colisao0 = []
                    colisao2 = []
                
                
            # Colisão da bola com o chão - faz a bola pingar
            if len(colisao4) > 0:
                if bola.speedy > 5:
                    bola.speedy = - 0.6*bola.speedy
                    p_bola += 1
                    
                    if p_bola > 5:
                        bola.speedy = 0
                        bola.rect.y = 390
                        p_bola = 0
                        
                colisao0 = []
                colisao4 = []

            # Colisão entre os players
            if len(colisao3) > 0:
                player1.rect.x -= 8
                player2.rect.x += 8 
                colisao0 = []
                colisao3 = []
                
            # atualiza todos os sprites
            all_sprites.update()
            
            # Desenha a tela de fundo
            window.blit(background, (0, 0))
            
            # Desenha os sprites e os textos na tela
            all_sprites.draw(window)
            window.blit(p1_gols_str, (560, 50))
            window.blit(p2_gols_str, (710, 50))
            window.blit(player1_str, (550, 25))
            window.blit(player2_str, (680, 25))
            
            # Verifica a ocorrência de gol para mostrar texto de gol na tela
            if gool == True:
                
                if cont2 < 20 or cont2 > 30 and cont2 < 45 :
                    window.blit(gol, (420, 110))
                cont2 += 1
                player1.reset(sent11, sent12)
                player2.reset(sent21, sent22)
                if cont2 > 45:
                    gool = False
                    cont2 = 0
            
            # Condicional para organizar a forma como o tempo aparece no placar
            if tempo < 10:
                window.blit(temporizador, (640,62))
            else:
                window.blit(temporizador, (630,62))
            
            # atualiza o display
            pygame.display.update()  # Mostra o novo frame para o jogador
        
        # condicional para verificar se o tempo do jogo já acabou
        if tempo <= 0:
            state = TIME
    # ===== Finalização =====
    pygame.quit()  # Função do PyGame que finaliza os recursos utilizados