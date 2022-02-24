import random
import pygame, time
from pygame import mixer

SIZE = 40
BACKGROUND_COLOR = (110, 110, 5)


class Apple:
    def __init__(self, screen):
        self.apple = pygame.image.load('resources/apple.jpg').convert()
        self.screen = screen
        self.x = SIZE * 3
        self.y = SIZE * 3

    def draw(self):
        self.screen.blit(self.apple, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 29) * SIZE
        self.y = random.randint(1, 19) * SIZE
        self.draw()


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
        # self.screen.fill(BACKGROUND_COLOR)
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

    def increase_length(self):
        self.length += 1
        self.block_x.append(-1)
        self.block_y.append(-1)


class Game:
    def __init__(self):
        pygame.init()
        # Defining Screen
        self.screen = pygame.display.set_mode((1200, 800))
        # self.screen.fill(BACKGROUND_COLOR)

        # Background Music
        mixer.music.load('resources/bg_music_1.mp3')
        mixer.music.play(-1)

        # Defining Icon and Title
        pygame.display.set_caption("Hey Snake")
        icon = pygame.image.load('resources/icon.bmp')
        pygame.display.set_icon(icon)

        self.snake = Snake(self.screen, 1)
        self.snake.draw()
        self.apple = Apple(self.screen)
        self.apple.draw()

    def play(self):
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.show_score()
        pygame.display.flip()
        # snake colliding with apple
        if self.is_collision(self.snake.block_x[0], self.snake.block_y[0], self.apple.x, self.apple.y):
            self.apple.move()
            self.snake.increase_length()
            self.play_music('resources/ding.mp3')
        # snake colliding with itself
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.block_x[0], self.snake.block_y[0], self.snake.block_x[i],
                                 self.snake.block_y[i]):
                self.play_music('resources/crash.mp3')
                raise "Game Over"

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def show_score(self):
        font = pygame.font.Font('resources/samuf.ttf', 32)
        score = font.render("Score : " + str(self.snake.length - 1), True, (255, 255, 255))
        self.screen.blit(score, (1100, 5))

    def game_over(self):
        # self.render_background()
        font = pygame.font.Font('resources/samuf.ttf', 32)
        line1 = font.render("Your Game is Over. Score is : " + str(self.snake.length - 1), True, (255, 255, 255))
        self.screen.blit(line1, (100, 400))
        line2 = font.render("To play again hit Enter or ESC to exit ", True, (255, 255, 255))
        self.screen.blit(line2, (100, 500))
        pygame.display.flip()

    def reset(self):
        self.snake = Snake(self.screen, 1)
        self.apple = Apple(self.screen)

    def play_music(self, source):
        music = mixer.Sound(source)
        music.play()

    def render_background(self):
        BACKGROUND = pygame.image.load('resources/background.jpg')
        self.screen.blit(BACKGROUND, (0, 0))

    def run(self):
        running = True
        pause = False
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pause = False
                        # Unpausing the music when Enter hitted
                        pygame.mixer.music.unpause()
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    # If game is paused , I won't allow any keystroke
                    if not pause:
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
            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.game_over()
                pause = True
                self.reset()
                # Pausing the music when snake is crashed
                pygame.mixer.music.pause()

            time.sleep(0.3)

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
