import pygame
white = (255, 255, 255)
black = (0, 0, 0)
screen_w = 800
screen_h = 600

class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(white)
        self.image.set_colorkey(white)
        self.life = 3
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

    def move(self, e):
        if e[pygame.K_RIGHT]:
            self.rect.x += 3
            if self.rect.x > 650:
                self.rect.x = 650
        if e[pygame.K_LEFT]:
            self.rect.x -= 3
            if self.rect.x < 0:
                self.rect.x = 0

    def restart(self):
        self.rect.x = 350
        self.rect.y = 588

    def relive(self):
        self.life = 3