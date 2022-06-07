# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from config import WIDTH, HEIGHT, INIT, GAME, QUIT
from init_screen import init_screen
from game_screen import game_screen


pygame.init()
pygame.mixer.init()
 
# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Futebol Cabeçudo')
pygame.mixer.music.load('torcida.mpeg')
pygame.mixer.music.set_volume(0.4)
state = INIT
while state != QUIT:
    pygame.mixer.music.play(loops=-1)
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = game_screen(window)
    #elif state == TIME:
        #state = time_screen(window)
    else:
        state = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados