import pygame, time

SIZE = 40


class Apple:
    def __init__(self, screen):
        self.apple = pygame.image.load('resources/apple.jpg').convert()
        self.screen = screen
        self.x = SIZE * 3
        self.y = SIZE * 3

    def draw(self):
        self.screen.blit(self.apple, (self.x, self.y))
        pygame.display.flip()


class Snake:
    def __init__(self, screen, length):
        # Defining block image
        self.block = pygame.image.load('resources/block.jpg').convert()
        self.length = length
        self.block_x = [SIZE] * self.length
        self.block_y = [SIZE] * self.length
        self.screen = screen
        self.direction = 'right'

    def draw(self):
        self.screen.fill((110, 110, 5))
        for i in range(self.length):
            self.screen.blit(self.block, (self.block_x[i], self.block_y[i]))
        pygame.display.flip()

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        for i in range(self.length - 1, 0, -1):
            self.block_x[i] = self.block_x[i - 1]
            self.block_y[i] = self.block_y[i - 1]

        if self.direction == 'right':
            self.block_x[0] += SIZE
        elif self.direction == 'left':
            self.block_x[0] -= SIZE
        elif self.direction == 'down':
            self.block_y[0] += SIZE
        elif self.direction == 'up':
            self.block_y[0] -= SIZE
        self.draw()


class Game:
    def __init__(self):
        pygame.init()
        # Defining Screen
        self.screen = pygame.display.set_mode((1200, 700))
        self.screen.fill((110, 110, 5))
        self.snake = Snake(self.screen, 4)
        self.snake.draw()
        self.apple = Apple(self.screen)
        self.apple.draw()
    def play(self):
        self.snake.walk()
        self.apple.draw()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_RIGHT:
                        self.snake.move_right()
                    if event.key == pygame.K_LEFT:
                        self.snake.move_left()
                    if event.key == pygame.K_UP:
                        self.snake.move_up()
                    if event.key == pygame.K_DOWN:
                        self.snake.move_down()
            self.play()
            time.sleep(0.3)

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
