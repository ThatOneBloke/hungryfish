import pygame
import random
import time
pygame.init()
score = 0
screenwidth = 500
screenheight = 500
screen = pygame.display.set_mode((screenwidth, screenheight))

class Block(pygame.sprite.Sprite):
    def __init__ (self, colour, width, height):
        super().__init__()
        #you are calling the init function of the parent class
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
    def resetposition(self):
        self.rect.y = random.randrange(0, screenheight)
        self.rect.x = random.randrange(0, screenwidth)
    def update(self):
        self.rect.y += 1
        if self.rect.y > 490:
            self.resetposition()

blockgroup = pygame.sprite.Group()
allspritelist = pygame.sprite.Group()

for i in range(50):
    food = Block("orange", 20, 15)
    food.rect.x = random.randrange(screenwidth)
    food.rect.y = random.randrange(screenheight)
    blockgroup.add(food)
    allspritelist.add(food)

fish = Block("blue", 25, 20)
allspritelist.add(fish)
fish.rect.x = 250
fish.rect.y = 250

run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    screen.fill("white")
    allspritelist.update()
    pos = pygame.mouse.get_pos()
    fish.rect.x = pos[0]
    fish.rect.y = pos[1]
    font = pygame.font.SysFont("Ariel", 20)
    text = font.render("score = " + str(score), True, "black")
    screen.blit(text, (50, 50))
    blockhitlist = pygame.sprite.spritecollide(fish, blockgroup, False)
    for i in blockhitlist:
        score += 1
        i.resetposition()
    allspritelist.draw(screen)
    pygame.display.update()