import pygame


def draw_block():
    screen.fill((110, 110, 5))
    screen.blit(block, (block_x, block_y))
    pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    # Defining Screen
    screen = pygame.display.set_mode((500, 500))
    screen.fill((110, 110, 5))
    # Defining block image
    block = pygame.image.load('resources/block.jpg').convert()
    block_x = 100
    block_y = 100
    screen.blit(block, (block_x, block_y))

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_RIGHT:
                    block_x += 10
                    draw_block()
                if event.key == pygame.K_LEFT:
                    block_x -= 10
                    draw_block()
                if event.key == pygame.K_UP:
                    block_y -= 10
                    draw_block()
                if event.key == pygame.K_DOWN:
                    block_y += 10
                    draw_block()
    pygame.quit()
