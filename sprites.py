from email.mime import base
from turtle import speed
from config import WIDTH, HEIGHT, pulo
import pygame
import random
 
pygame.mixer.init()
gol_sound = pygame.mixer.Sound('gol2.mpeg')

class Bola(pygame.sprite.Sprite):
    """Classe da Bola"""
    def __init__(self, img):
        """Caracteísticas iniciais da bola"""
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH / 2)
        self.rect.y = 0
        self.speedy = 0
        self.speedx = 0
        self.tocando = False
        
        # Mantem dentro da tela
        if self.rect.right > WIDTH - 140 :
            self.rect.right = WIDTH - 140
        if self.rect.left < 140:
            self.rect.left = 140
        if self.rect.y < 249:
            self.speedy = 0
        

    def update(self):
        """Função que atualiza a bola"""
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        if self.rect.right > WIDTH - 65 :
            self.rect.right = WIDTH - 65
        if self.rect.left < 65:
            self.rect.left = 65
        if self.rect.y < 249:
            self.speedy += 10
        if self.rect.x < 100 or self.rect.x > 1150:
            self.rect = self.image.get_rect()
            self.rect.centerx = (WIDTH / 2)
            self.rect.y = 0
            self.speedy = 0
            self.speedx = 0
        if self.rect.y < 390:
            self.speedy += 2
        elif self.rect.y > 384:
            #self.speedy = - 0.25*self.speedy
            #self.speedx = 0.8*self.speedx
            self.rect.y = 390
        
    def reset(self):        
        """Função que reseta a bola para a posição inicial"""
        self.rect.centerx = (WIDTH / 2)
        self.rect.bottom = HEIGHT -75
        self.speedx = 0
        self.speedy = 0

    def tocar(self):
        """Função que toca o som de gol"""
        if not self.tocando:
            self.gol_sound = gol_sound
            gol_sound.play()
            self.tocando = True
        else:
            self.tocando = False
        
       
        





class Skin(pygame.sprite.Sprite ):
    """Classe do Personagem"""
    def __init__(self, img, sent1, sent2):
        """Função que define as características iniciais de um personagem"""
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = sent1
        self.rect.bottom = sent2
        self.speedx = 0
        self.speedy = 0
        self.pulando = False
        
    def update(self):
        """Função que atualiza o personagem"""
        # Atualização do personagem
        self.rect.x += self.speedx
        
        self.rect.y += self.speedy
            
        # gravidade no personagem
        if self.rect.y < 359:
            
            self.rect.y += 10
            
            
        # Mantem dentro da tela
        if self.rect.right > WIDTH - 150:
            self.rect.right = WIDTH - 150
        if self.rect.left < 150:
            self.rect.left = 150
        if self.rect.y < 249:
            self.speedy = 0

        # estabelece condições de pulo     
        if self.rect.y >= 349:
            self.pulando = False

    # estabelece função para pular
    def pular(self):
        """Função para o personagem pular"""
        if not self.pulando:
            self.speedy -= pulo
            self.pulando = True

    # Estabelece função para resetar a posição dos players
    def reset(self, sent1, sent2):
        """Função que reseta a posição do personagem"""
        self.rect.centerx = sent1
        self.rect.bottom = sent2
        self.pulando = False  


# Cria a classe chão
class Chao(pygame.sprite.Sprite):
    """Classe do chão"""
    def __init__(self, img):
        """Função que dá os parâmetros do chão"""
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 1
        self.rect.y = 423

# Cria a classe placar
class Placar(pygame.sprite.Sprite):
    """Classe do placar"""
    def __init__(self, img):
        """Função que dá os parâmetros do placar"""
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 445
        self.rect.y = 20
        
