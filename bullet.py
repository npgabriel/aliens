import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage fired bullets"""

    def __init__(self, ai_game):
        """Create bullet at ships location"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        # Create a bullet at (0, 0), then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Bullet position as a decimal
        self.y = float(self.rect.y)
    def update(self):
        """Move the bullet up the screen"""
        # Update decimal position
        self.y -= self.settings.bullet_speed
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
