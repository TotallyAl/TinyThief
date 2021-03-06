import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size) -> None:
        super().__init__()
        self.image = pygame.Surface([size, size])
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft = pos)
    
    def update(self, shift_x) -> None:
        self.rect.x += shift_x
        
