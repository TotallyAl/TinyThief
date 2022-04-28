import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos: float) -> None:
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)

        #Player movement
        self.direction = pygame.Vector2(0, 0)
        self.speed = 2
        self.pos = (0, 0)

    def get_input(self):
        mouse_event = pygame.mouse.get_pressed()
        if mouse_event[0] == True:
            self.pos = pygame.mouse.get_pos()
            if self.rect.x != self.pos[0]:
                if self.rect.x < self.pos[0]:
                    print("go right")
                    self.direction.x = 1
                
                if self.rect.x > self.pos[0]:
                    print("go left")
                    self.direction.x = -1

    def update(self) -> None:
        self.get_input()

        # Right
        if self.direction.x == 1:
            if self.rect.x > self.pos[0]:
                self.direction.x = 0
            elif self.rect.x < self.pos[0]:
                self.rect.x += self.direction.x * self.speed
        
        # Left
        elif self.direction.x == -1:
            if self.rect.x < self.pos[0]:
                self.direction.x = 0
            elif self.rect.x > self.pos[0]:
                self.rect.x += self.direction.x * self.speed
