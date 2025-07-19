
import pygame

class Car:
    def __init__(self):
        self.image = pygame.Surface((60, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(100, 300))

    def update(self, keys):
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

    def draw(self, surface):
        surface.blit(self.image, self.rect)
