import pygame
import numpy as np

class Creature:
    def __init__(self, n1, n2, color):
        self.n1 = n1
        self.n2 = n2
        self.value = self.n1 * self.n2
        self.color = color
    def multiply(self):
        return self.value
    def reproduce(self):
        return Creature(self.n1 + np.random.uniform(-1.0, 1.0), self.n2 + np.random.uniform(-1.0, 1.0), self.color)
    def draw(self):
        return pygame.draw.circle(window, self.color, (self.n1 + sX//2, self.n2 + sY//2), 1, width= 0)

     
pygame.init()
sX = 800
sY = 800
window = pygame.display.set_mode((sX, sY))
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255,255,255)
creatureAmount = 1000
creatures = [None] * creatureAmount
for i in range(creatureAmount):
    creatures[i] = Creature(np.random.uniform(-10.0, 10.0),np.random.uniform(-10.0, 10.0), np.random.randint(0, 255, 3))

running = True
while running:
    window.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for j in range(creatureAmount):
        creatures[j].draw()
    creatures.sort(key=lambda x: x.value)
    # for i in range(creatureAmount//2):
    #     creatures[i] = creatures[i + creatureAmount//2].reproduce()
    dead = 0
    for i in range(creatureAmount):
        if np.random.uniform(0.0, 100.0) < (creatureAmount - i) * (creatureAmount - i)/100:
            creatures[i].value = -1 * creatures[creatureAmount - 1].value
            dead += 1
    creatures.sort(key=lambda x: x.value)          
    for i in range(dead):
        creatures[i] = creatures[creatureAmount - 1 - i].reproduce()        
    pygame.display.flip()
    clock.tick(60)
pygame.quit()