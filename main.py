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
	radius = 250
	xbase = np.random.uniform(-radius, radius)
	ybase = np.random.uniform(np.sqrt(radius**2 - xbase**2) *  -1, np.sqrt(radius**2 - xbase**2))#np.random.uniform(250, 750)
	z = np.random.randint(1, 5)
	x = xbase + 500
	y = ybase + 500

	object = Object(x,y,z)
	objects.append(object)

for amount in range(300):
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
	pg.display.flip()