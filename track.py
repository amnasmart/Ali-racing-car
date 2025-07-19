
import pygame

class Track:
    def draw(self, surface):
        pygame.draw.rect(surface, (0, 128, 0), pygame.Rect(0, 250, 800, 100))  # simple green track
