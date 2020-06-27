from Tetris import Tetris
import screen
import pygame

pygame.init()

game = Tetris()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    move = 'D'
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            move = 'U'
        if event.key == pygame.K_LEFT:
            move = 'L'
        if event.key == pygame.K_RIGHT:
            move = 'R'
    game.iteration(move)
    game.get_state()
    screen.draw(game)