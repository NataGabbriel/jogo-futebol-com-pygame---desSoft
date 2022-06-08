# ----- Importa e inicia pacotes
import pygame
import random
from config import WIDTH, HEIGHT, INIT, GAME, QUIT
from init_screen import init_screen
from game_screen import game_screen

#inicia o pygame e a parte musical
pygame.init()
pygame.mixer.init()
 
# ----- Gera tela principal e carrega o som de fundo
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Head Soccer')
pygame.mixer.music.load('torcida.mpeg')
pygame.mixer.music.set_volume(0.4)
state = INIT
#------ Cria um looping de funcionamento do main, que inicializa a página inicial e a página do jogo
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = game_screen(window)
    
    else:
        state = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados