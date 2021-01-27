import pygame
import random
white = (255, 255, 255)
black = (0, 0, 0)
screen_w = 800
screen_h = 600

class Ball(pygame.sprite.Sprite):
    def __init__(self,width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill((255, 0, 0))
        self.image.set_colorkey((255, 0,0))
        self.speed = 3
        pygame.draw.circle(self.image, black, [10, 10], 10)
        self.over = False

        self.rect = self.image.get_rect()
        self.direction_y = 'down'
        self.direction_x = ''

    def start(self):
        self.over = False
        self.direction_y = 'down'
        self.direction_x = ''
        self.rect.x = 400
        self.rect.y = 400

    def move(self):
        if self.direction_y == 'down':
            self.rect.y += self.speed
            if self.rect.y > 610:
                self.over = True
        else:
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.direction_y = 'down'
        if self.direction_x == 'left':
            self.rect.x -= self.speed
            if self.rect.x < 0:
                self.direction_x = 'right'
        elif self.direction_x == 'right':
            self.rect.x += self.speed
            if self.rect.x > 790:
                self.direction_x = 'left'


    def collision_player(self, player):
        choice = ['left', 'right']
        if self.rect.colliderect(player.rect) and self.rect.y > 576:
            self.direction_y = 'up'
            if self.direction_x == '':
                self.direction_x = random.choice(choice)

    def collision_wall(self, wall):
        choice = ['left', 'right']
        if self.rect.colliderect(wall.rect):
            self.direction_y = 'down'