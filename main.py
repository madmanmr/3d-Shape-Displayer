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
	ybase = np.random.uniform(np.sqrt(radius**2 - xbase**2) *  -1, np.sqrt(radius**2 - xbase**2))
	x = xbase + 500
	y = ybase + 500
	d = np.sqrt((xbase)**2 + (ybase)**2)
	rand = np.random.choice([ (- 250 / d) + 1,0])
	z = 8 -  d / 60 + rand
	if rand > 0 :
		pos = 0
	else:
		pos = 1


	object = Object(x,y,z,pos)
	objects.append(object)

for amount in range(500):
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