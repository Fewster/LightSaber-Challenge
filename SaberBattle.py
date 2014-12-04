#!/usr/bin/env python

import pygame
from pygame.locals import *

import random

# Methods should probably be private
class SaberBattleScene():
    """SaberBattleScene renders the main scene in the game"""

    background = None
    display = None
    FPS = 60
    fpsClock = pygame.time.Clock()
    running = False

    player_one = None
    player_two = None

    player_one_score = 98
    player_two_score = 98

    player_two_string = None
    player_one_string = None

    player_one_font = None
    player_two_font = None

    theme = None

    """
        Initialise pygame and render a window
    """
    def __init__(self, new_display):
        self.display = new_display
        self.display.fill((0, 0, 0), self.display.get_rect())

        self.running = True
        self.player_one_string = pygame.font.SysFont("Arial", 16)
        self.player_two_string = pygame.font.SysFont("Arial", 16)

        self.play_rand_music()


    """
        Draws a surface with an optional rect to a new surface.
    """
    def draw(self, surface, rect = None):

        if rect == None:
            rect = surface.get_rect()

        temp_surface = pygame.Surface((600, 480))
        ck = (0, 0, 0)
        temp_surface.fill(ck)
        temp_surface.set_colorkey(ck)

        temp_surface.blit(surface, rect)
        self.display.blit(temp_surface, temp_surface.get_rect())

    """
        Draws the scores to the screen.
    """
    def draw_score(self):
        self.player_one_font = self.player_one_string.render("Player one score: {}".format(self.player_one_score), True, (255, 255, 255))

        player_one_rect = self.player_one_font.get_rect()
        player_one_rect.center = (80, 450)

        self.player_two_font = self.player_two_string.render("Player two score: {}".format(self.player_two_score), True, (255, 255, 255))
        player_two_rect = self.player_two_font.get_rect()

        player_two_rect.center = (480, 450)

        self.draw(self.player_one_font, player_one_rect)

        self.draw(self.player_two_font, player_two_rect)


    """
        Render items to be drawn
    """
    def render(self):
        # Player one fonts
        self.draw_background()
        self.draw_score()

    """
        Play random track
    """
    def play_rand_music(self):
        num = random.randint(1, 3)

        if num == 1:
            self.theme = pygame.mixer.Sound('music/imperial.wav')
        if num == 2:
            self.theme = pygame.mixer.Sound('music/rebel.wav')
        if num == 3:
            self.theme = pygame.mixer.Sound('music/cantina.wav')

        self.theme.play(loops=-1, fade_ms=500)

    """
        Get events in game for pause, quit and user input etc
    """
    def event_loop(self):
        for event in pygame.event.get(): #any key being pressed DOWN

            if event.type == QUIT:
                self.running = False

            if event.type == MOUSEBUTTONDOWN or event.type == MOUSEBUTTONUP:
                break

            # Key event
            if event.type == KEYDOWN:
                keypress = event.key


                # Player 1
                if keypress == K_SPACE:
                    self.update_score("Player one")

                # Player 2
                if keypress == K_RETURN:
                    self.update_score("Player two")


                # quit
                if keypress == K_q:
                    self.running = False

    """
        Update user's scores and check if they are a winner
    """
    def update_score(self, player):
        # TODO: Font methods
        # TODO: USe star wars font

        if "one" in player.lower():
            self.player_one_score += 1

        elif "two" in player.lower():
            self.player_two_score += 1

        self.check_winner()

    """
        Draw the background
    """
    def draw_background(self):
        #TODO Change redraw logic
        self.background = pygame.image.load('battle/background.png')

        rect = self.display.get_rect()
        self.display.blit(self.background, rect)


    """
        Will be used to check for a winner and ask for a rematch
    """
    def check_winner(self):

        # TODO Change logic so that the dialogue is displayed

        if self.player_one_score >= 100:
            self.running = False
            dialogue = pygame.image.load('battle/playagain.png')


            # loop for event until we get a click
            while True:
                self.draw(dialogue)

                for event in pygame.event.get(): #any key being pressed DOWN
                    if event.type == QUIT:
                        break

                    if event.type == MOUSEBUTTONDOWN or event.type == MOUSEBUTTONUP:
                        mouse_x, mouse_y = event.pos

                        if mouse_x > 301:
                            self.new_game()
                            # Play again
                        else:
                            return

        if self.player_two_score >= 100:
            self.running = False



    """
        Restart the game
    """
    def new_game(self):
        while self.running == True:
            self.render()
            self.event_loop()
            pygame.display.update()
            self.fpsClock.tick(self.FPS)

        self.quit()

    """
        Leaves game scene
    """
    def quit(self):
        self.theme.stop()

