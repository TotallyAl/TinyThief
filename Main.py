#!/usr/bin/env python
import pygame
from Engine import Display, Level, KeyEvent
from Config import Settings

BLACK = (0, 0, 0)

class Game:
    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        display = Display.Display(1200, 800, "DeckedOut")
        keyevent = KeyEvent.KeyEvent()

        level = Level.Level(Settings.level_map, display.screen)

        while True:
            display.screen.fill(BLACK)

            level.run()

            pygame.display.update()
            clock.tick(60)

            keyevent.key_event()



game = Game()
game.run()