from email.mime import base
from turtle import speed
from config import WIDTH, HEIGHT, pulo
import pygame
import random




class Bola(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH / 2)
        self.rect.y = 0
        self.speedy = 0
        self.speedx = 0
        
        # Mantem dentro da tela
        if self.rect.right > WIDTH - 140 :
            self.rect.right = WIDTH - 140
        if self.rect.left < 140:
            self.rect.left = 140
        if self.rect.y < 249:
            self.speedy = 0
        #if self.rect.y < 100:
        #   self.speedy += 2

    def update(self):
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
            self.speedy += 5
        elif self.rect.y > 384:
            #self.speedy = - 0.25*self.speedy
            #self.speedx = 0.8*self.speedx
            self.rect.y = 390
        
    def reset(self):        

        self.rect.centerx = (WIDTH / 2)
        self.rect.bottom = HEIGHT -75
        self.speedx = 0
        self.speedy = 0
        
       
        





class Skin(pygame.sprite.Sprite ):
    def __init__(self, img, sent1, sent2):
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
        
        # Atualização da posição da nave
        self.rect.x += self.speedx
        
        self.rect.y += self.speedy
            
        if self.rect.y < 359:
            
            self.rect.y += 10
            
            
        # Mantem dentro da tela
        if self.rect.right > WIDTH - 150:
            self.rect.right = WIDTH - 150
        if self.rect.left < 150:
            self.rect.left = 150
        if self.rect.y < 249:
            self.speedy = 0
             
        if self.rect.y >= 349:
            self.pulando = False

    def pular(self):
        if not self.pulando:
            self.speedy -= pulo
            self.pulando = True

class Chao(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 1
        self.rect.y = 423

class Placar(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 445
        self.rect.y = 20
        
        


        
    