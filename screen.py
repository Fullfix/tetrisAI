import pygame
import config

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

clock = pygame.time.Clock()
win = pygame.display.set_mode(config.WIN_SIZE)
pygame.display.set_caption('Tetris')

def draw(game):
    if (game.game_over):
        pygame.display.set_caption(f'GAME OVER. SCORE: {game.score}')
    else:
        pygame.display.set_caption(f'SCORE {game.score}')
    win.fill(BLACK)
    for i in range(config.HEIGHT):
        for j in range(config.WIDTH):
            if game.field[i][j]:
                pygame.draw.rect(win, game.field[i][j], [
                    j * config.BLOCK_SIZE + (j + 1) * config.LINE_WIDTH, 
                    i * config.BLOCK_SIZE + (i + 1) * config.LINE_WIDTH,
                    config.BLOCK_SIZE, config.BLOCK_SIZE
                ])
    field = game.figure.get_field()
    for i in range(game.figure.grid_size):
        for j in range(game.figure.grid_size):
            if field[i][j]:
                X = game.figure.x + j
                Y = game.figure.y + i
                pygame.draw.rect(win, field[i][j], [
                    X * config.BLOCK_SIZE + (X + 1) * config.LINE_WIDTH,
                    Y * config.BLOCK_SIZE + (Y + 1) * config.LINE_WIDTH,
                    config.BLOCK_SIZE, config.BLOCK_SIZE
                ])
    pygame.display.flip()
    clock.tick(config.FPS)