import pygame
import random
from pygame.math import Vector2

# todo make start game page

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(-1,0)
        self.new_block = False

    def draw_snake(self):
        #create rectangle
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size, cell_size)

            #draw rectangle
            pygame.draw.rect(screen,(183,150,185),block_rect)

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

class FOOD:
    def __init__(self):
        self.randomize()

    def draw_food(self):
        # create rectangle
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)

        # draw rectangle
        pygame.draw.rect(screen,(126,166,114),fruit_rect)

    def randomize(self):
        self.x = random.randint(0,cell_num - 1)
        self.y = random.randint(0,cell_num - 1)
        self.pos = Vector2(self.x,self.y)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FOOD()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_food()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            # reposition food
            self.fruit.randomize()

            # add another block to snake
            self.snake.add_block()

    def check_fail(self):
        # check if snake is outside of the screen
        if not 0 <= self.snake.body[0].x < cell_num or not 0 <= self.snake.body[0].y < cell_num:
            self.game_over()

        # check if snake bits it self
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()

# initialize pygame GUI with width and height
pygame.init()

cell_size = 40
cell_num = 20

screen = pygame.display.set_mode((cell_num * cell_size,cell_num * cell_size))
done = False

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,100)

main_game = MAIN()

while not done:
    for event in pygame.event.get():
        # for pygame to stay open
        if event.type == pygame.QUIT:
            done = True
        # for moving snake
        if event.type == SCREEN_UPDATE:
            main_game.update()
            # TODO # MAKE STATEMENT FOR SNAKE TO NOT BITE IT SELF
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1,0)

    screen.fill(pygame.Color('gray'))
    main_game.draw_elements()
    pygame.display.flip()


