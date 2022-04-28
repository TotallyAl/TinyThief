from xmlrpc.client import Boolean
import pygame

class Display:
    def __init__(self, x: int, y: int, title: str) -> None:
        self.screen = pygame.display.set_mode((x, y))
        pygame.display.set_caption(title)