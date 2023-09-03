import pygame 

width = 1300
height = 700

FPS = 60

window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

pygame.display.set_caption("Гра Пінг Понг. Автор: Стас")

# background = pygame.transform.scale(
#                     pygame.image.load("..."), 
#                     (width, height)
#             )


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, x,y, speed, size):
        super().__init__()
        self.image = pygame.transform.scale(
                            pygame.image.load(image),
                            size
        )
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))





class Player(GameSprite):
    def update_r(self):
        ...

    def update_l(self):
        ...


game_over = False
finish = False

while not game_over:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game_over = True




    pygame.display.update()
    clock.tick(FPS)