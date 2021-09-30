# reproduza um Arquivo .mp3
import pygame
pygame.init()
pygame.mixer.music.load('exercicio021.mp3')
pygame.mixer.music.play()
pygame.event.wait()