import pygame
pygame.init()
pygame.mixer.music.load('import/Mp3/music.mp3')
pygame.mixer.music.play()
input('Posso tocar? ')
pygame.event.wait()
