# programa em Python que abre e reproduz um arquivo Mp3

# no terminal execuar: pip3 install pygame

# minha solução com o playsound, instalar ele primeiro: pip3 install playsound
from playsound import playsound


import pygame
pygame.init ()
pygame.mixer.music.load ('exercicio21_audio.mp3')
# pygame.mixer.music.play () o som começa e para muito rapido



playsound('exercicio21_audio.mp3')

pygame.event.wait ()






