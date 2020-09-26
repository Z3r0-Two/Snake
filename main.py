import pygame
import sys

size = width, height = 800, 600  # Размеры экрана


def main():
    global size, width, height
    pygame.init()
    screen = pygame.display.set_mode(size)
    caption = pygame.display.set_caption('Hungry snake')
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('Just a test, do not worry')
                game_over = True
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode(size)
        pygame.display.flip()
        pygame.time.wait(100)
    sys.exit()


if __name__ == "__main__" :
    main()




