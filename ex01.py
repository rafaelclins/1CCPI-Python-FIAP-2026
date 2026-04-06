import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("audio1.mp3")
pygame.mixer.music.play()

input("Pressione Enter para sair...")

