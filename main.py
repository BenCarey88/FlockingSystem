import pygame, sys
from flockingSystem import FlockingSystem
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((800, 800), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
boidImg = pygame.image.load('boid.png')

system = FlockingSystem([800,800],100)

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    for boid in system.boidList:
        boidImgRot = pygame.transform.rotate(boidImg,boid.angle)
        DISPLAYSURF.blit(boidImgRot, (boid.x, boid.y))
    
    system.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    fpsClock.tick(FPS) 