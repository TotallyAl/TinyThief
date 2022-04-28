import pygame
from Engine import Tile, Player
from Config import Settings

class Level:
    def __init__(self, level_data, surface) -> None:
        self.surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
    
    def setup_level(self, layout) -> None:
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                x = col_index * Settings.tile_size
                y = row_index * Settings.tile_size
                if col == "X":
                    tile = Tile.Tile((x, y), Settings.tile_size)
                    self.tiles.add(tile)
                if col == "P":
                    player = Player.Player((x, y))
                    self.player.add(player)

    def update_shift_x(self, x_shift) -> None:
        self.rect.x += x_shift

    def run(self) -> None:
        #Tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.surface)

        #Player
        self.player.update()
        self.player.draw(self.surface)