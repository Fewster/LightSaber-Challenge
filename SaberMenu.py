#!/usr/bin/env python

import pygame
from pygame.locals import *

import sys

from SaberBattle import SaberBattleScene

class SaberMenuScene():
    """Saber battle scene, used for the main game"""

    # Used when blitting to the screen.
    display = None
    display_rect = None

    # Set frames per second (Not really useful but good practice)
    FPS = 60
    fpsClock = pygame.time.Clock()

    # Do we have a running game?
    running = False
    # Theme tune object
    theme_tune = None

    # Menu items
    play_game = None

    # Scenes
    game_scene = None

    """
        Initialise the display, music and windowing properties
    """
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("LightSaber Challenge")
        pygame.display.set_icon(pygame.image.load('menu/icon.png'))
        self.display = pygame.display.set_mode((600, 480), 0, 32)

        self.display_rect = self.display.get_rect()
        self.running = True
        self.play_music()
        self.music_isplaying = True

    """
        render menu, play music and check for events
    """
    def display_menu(self):
        while self.running == True:
            if self.music_isplaying == False:
                self.play_music()
                self.music_isplaying = True

            self.event_loop()
            self.render()
            pygame.display.update()
            self.fpsClock.tick(self.FPS)

        self.quit()


    """
        check for events such as QUIT
    """
    def event_loop(self):
        for event in pygame.event.get(): #any key being pressed
            if event.type == QUIT:
                self.running = False

            # Get images first, then deal with mouse clicks on them
            if event.type == MOUSEBUTTONDOWN or event.type == MOUSEBUTTONUP:
                self.check_mouse(event)

            # Key event
            if event.type == KEYDOWN:
                keypress = event.key

    """
        Will be used for checking which menu item is selected. NOT IMPLEMENTED YET.
    """
    def check_mouse(self, event):
        # Play game clicked
        if self.play_game.get_rect().collidepoint(event.pos):
            self.new_game()

        #if self.credits.get_rect().collidepoint(event.pos):
        #    self.credits()

    """
        Start a new game.
    """
    def new_game(self):
        print "Starting new game..."
        self.theme_tune.stop()
        self.music_isplaying = False

        game_scene = SaberBattleScene(self.display)
        game_scene.new_game()

    """
        Show the credits scene when it is selected on the menu.
    """
    def credits_screen(self):
        pass


    """
        Draw the background
    """
    def draw_background(self):
        # Background
        background = pygame.image.load('menu/background.png')
        background_rect = background.get_rect()
        self.display.blit(background, background_rect)

    """
        Draw menu items on the background
    """
    def draw_menu(self):
         # Menu items
        self.credits = pygame.image.load('menu/credits.png')
        self.title = pygame.image.load('menu/title.png')
        self.play_game = pygame.image.load('menu/start.png')
        self.settings = pygame.image.load('menu/settings.png')

        self.display.blit(self.credits, self.display_rect)
        self.display.blit(self.title, self.display_rect)
        self.display.blit(self.play_game, self.display_rect)
        self.display.blit(self.settings, self.display_rect)


        # Place rects for menu clicks

    """
        Render all items to be drawn
    """
    def render(self):
        self.draw_background()
        self.draw_menu()


        # TODO: Draw transparent rects and check for clicks

    """
        Play theme music on a loop
    """
    def play_music(self):
        self.theme_tune = pygame.mixer.Sound('music/maintheme.wav')
        self.theme_tune.play(loops=-1, fade_ms=500)

    """
        Exit the game
    """
    def quit(self):
        pygame.quit()
        sys.exit()
