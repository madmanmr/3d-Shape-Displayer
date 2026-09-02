import pygame as pg
import numpy as np
from Object_Class import Object

pg.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.time.Clock()

objects = []

running = True

def createObject():
	x = np.random.randint(0,SCREEN_WIDTH)
	y = np.random.randint(0,SCREEN_HEIGHT)
	z = np.random.randint(1, 10)

	object = Object(x,y,z)
	objects.append(object)

for amount in range(100):
	createObject()

def drawObjects(screen):
		for each in objects:
			each.draw(screen)



while running:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False
			pg.quit()
	screen.fill((0,0,0))
	drawObjects(screen)