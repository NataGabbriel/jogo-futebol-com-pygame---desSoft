import pygame
import random
from os import path

from config import FPS, GAME, QUIT, WIDTH, HEIGHT


def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    back = pygame.image.load('init_screen.png').convert()
    back = pygame.transform.scale(back, (WIDTH, HEIGHT))

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(0)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = GAME
                

        # A cada loop, redesenha o fundo e os sprites
        
        screen.blit(back, (0,0))

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state

