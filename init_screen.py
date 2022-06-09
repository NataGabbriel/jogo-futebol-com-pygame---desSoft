# ----- Importa e inicia pacotes
import pygame
import random
from os import path

from config import *

# Função da tela inicial que é invocaada pelo Main
def init_screen(screen):
    """Função da tela inicial"""
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    
    # Carrega as imagens, as fontes da página inicial e as variáveis da página inicial
    back = pygame.image.load('init_screen.png').convert_alpha()
    back = pygame.transform.scale(back, (1300, 550))
    head = pygame.image.load('Head Boll.png').convert_alpha()
    head = pygame.transform.scale(head, (500, 220))
    fonte4 = pygame.font.get_default_font()
    font4 = pygame.font.SysFont(fonte4, 40)
    running = True
    t = 0
    # Inicia o looping principal da página inicial
    while running:

        # Ajusta a velocidade do jogo e cria variável temp para contar o tempo
        t += 1
        clock.tick(60)
        temp = int(t/FPS)
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = GAME
                running = False

        # Faz o nome do jogo piscar utilizando quando a variável de temp como condicional para desenhar o nome na tela
        
        screen.blit(back, (0,0))
        if temp % 2 == 0:
            screen.blit(head, (400,130))
            jogar_dnv = font4.render(str("Aperte qualquer tecla para começar o jogo!"), 1, (255,255, 255))
            screen.blit(jogar_dnv, (370, 450))
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state