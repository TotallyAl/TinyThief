import pygame

class KeyEvent():

    def key_event(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            
            if event.type == pygame.QUIT:
                pygame.quit()
