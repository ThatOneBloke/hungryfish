import pygame
import random
pygame.init()
score = 0
playerhealth = 10
screenwidth = 500
screenheight = 500
screen = pygame.display.set_mode((screenwidth, screenheight))
counter = 0

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


poisonblockgroup = pygame.sprite.Group()
blockgroup = pygame.sprite.Group()
allspritelist = pygame.sprite.Group()

for i in range(50):
    food = Block("orange", 20, 15)
    food.rect.x = random.randrange(screenwidth)
    food.rect.y = random.randrange(screenheight)
    blockgroup.add(food)
    allspritelist.add(food)

for i in range(5):
    poisonousfood = Block("red", 20, 15)
    food.rect.x = random.randrange(screenwidth)
    food.rect.y = random.randrange(screenheight)
    poisonblockgroup.add(poisonousfood)
    blockgroup.add(poisonousfood)
    allspritelist.add(poisonousfood)

fishwidth = 25
fishheight = 20
fish = Block("blue", fishwidth, fishheight)
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
    text1 = font.render("score = " + str(score), True, "black")
    text2 = font.render("player health = " + str(playerhealth), True, "black")
    screen.blit(text2, (50, 60))
    screen.blit(text1, (50, 50))
    blockhitlist = pygame.sprite.spritecollide(fish, blockgroup, False)
    poisonhitlist = pygame.sprite.spritecollide(fish, poisonblockgroup, False)
    for i in blockhitlist:
        score += 1
        i.resetposition()
        fishwidth = fish.rect.width + 1
        fishheight = fish.rect.height + 1
        fish.image = pygame.Surface([fishwidth, fishheight])
        fish.image.fill("blue")
        fish.rect = fish.image.get_rect()
    for i in poisonhitlist:
        score -= 1
        playerhealth -= 1
        i.resetposition()
        fishwidth = fish.rect.width - 1
        fishheight = fish.rect.height - 1
        fish.image = pygame.Surface([fishwidth, fishheight])
        fish.image.fill("blue")
        fish.rect = fish.image.get_rect()
    if playerhealth <= 0:
            run = False
    allspritelist.draw(screen)
    pygame.display.update()