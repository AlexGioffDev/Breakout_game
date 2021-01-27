import pygame
import time
import random

from Block import Block
from Player import Player
from Ball import Ball

pygame.init()

screen_w = 800
screen_h = 600

white = (255, 255, 255)
black = (0, 0, 0)

game_screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('Breakout Game!')


def random_color():
    r = random.randint(0, 245)
    g = random.randint(0, 245)
    b = random.randint(0, 245)
    return r, g, b


def life_text(life):
    font = pygame.font.SysFont(None, 25)
    text = font.render(f"Life:  {life}", True, black)
    game_screen.blit(text, (5, 5))


class Game:
    def __init__(self):
        self.all_sprites_list = pygame.sprite.Group()
        self.player = Player(black, 150, 20)
        self.ball = Ball(20, 20)
        self.player.rect.x = 350
        self.player.rect.y = 588
        self.ball.start()
        self.all_sprites_list.add(self.player)
        self.all_sprites_list.add(self.ball)
        self.blocks = []

    def wall(self):
        y_start = 40
        for _ in range(5):
            x_start = 0
            for _ in range((screen_w//50)):
                block = Block(random_color(), 50, 20)
                block.rect.x = x_start
                block.rect.y = y_start
                self.all_sprites_list.add(block)
                x_start += 50
                self.blocks.append(block)
            y_start += 20

    def game_over(self):
        while True:
            game_screen.fill(white)
            font = pygame.font.SysFont(None, 25)
            text = font.render("GAME OVER", True, black)
            info_text = font.render("Press Space Bar to play again or Q to quit", True, black)
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.ball.start()
                    self.player.restart()
                    self.player.relive()
                    self.start_game()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
            text_rect = text.get_rect(center=(screen_w/2, 250))
            info_rect = info_text.get_rect(center=(screen_w/2, 280))
            game_screen.blit(text, text_rect)
            game_screen.blit(info_text, info_rect)
            pygame.display.update()

    def win(self):
        while True:
            game_screen.fill(white)
            font = pygame.font.SysFont(None, 25)
            text = font.render("You Win", True, black)
            info_text = font.render("Press Space Bar to play again or Q to quit", True, black)
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.ball.start()
                    self.player.restart()
                    self.player.relive()
                    self.start_game()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
            text_rect = text.get_rect(center=(screen_w/2, 250))
            info_rect = info_text.get_rect(center=(screen_w/2, 280))
            game_screen.blit(text, text_rect)
            game_screen.blit(info_text, info_rect)
            pygame.display.update()

    def menu(self):
        while True:
            game_screen.fill(white)
            font_title = pygame.font.SysFont(None, 53)
            font_menu = pygame.font.SysFont(None, 32)
            text = font_title.render(f"BREAKOUT!", True, black)
            start_text = font_menu.render('Start Game', True, black)
            quit_text = font_menu.render("Quit", True, black)
            info_text = font_menu.render("Press Space to Play, Q to quit", True, black)
            text_rect = text.get_rect(center=(screen_w/2, 200))
            start_rect = start_text.get_rect(center=(screen_w/2, 260))
            quit_rect = quit_text.get_rect(center=(screen_w/2, 300))
            info_rect = info_text.get_rect(center=(screen_w/2, 588))
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.start_game()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    mx, my = pygame.mouse.get_pos()
                    if start_rect.collidepoint(mx, my):
                        self.start_game()
                    if quit_rect.collidepoint(mx, my):
                        pygame.quit()
                        quit()
            game_screen.blit(text, text_rect)
            game_screen.blit(start_text, start_rect)
            game_screen.blit(quit_text, quit_rect)
            game_screen.blit(info_text, info_rect)
            pygame.display.update()

    def start_game(self):
        self.wall()
        time.sleep(0.5)
        while self.player.life > 0:
            keys = pygame.key.get_pressed()
            event = pygame.event.poll()
            self.ball.move()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            self.player.move(keys)
            if self.ball.over:
                self.ball.start()
                self.player.restart()
                self.player.life -= 1
                time.sleep(0.3)
            self.ball.collision_player(self.player)
            for block in self.blocks:
                if self.ball.rect.colliderect(block):
                    self.ball.collision_wall(block)
                    self.all_sprites_list.remove(block)
                    self.blocks.remove(block)
            if len(self.blocks) == 0:
                break
            self.all_sprites_list.update()
            game_screen.fill(white)
            life_text(self.player.life)
            self.all_sprites_list.draw(game_screen)
            pygame.display.update()
        
        if self.player.life == 0:
            self.game_over()
        else:
            self.win()


if __name__ == '__main__':
    game = Game()
    game.menu()
