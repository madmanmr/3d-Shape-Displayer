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
	zmax = np.sqrt(radius ** 2 - xbase ** 2 - ybase ** 2)
	zbase = np.random.choice([-zmax, zmax])
	x = xbase + 500
	y = ybase + 500
	z = zbase + 500
	print(x,y,z)

	object = Object(x,y,z)
	objects.append(object)

for amount in range(500):
	createObject()

def drawObjects(screen):
		for each in objects:
			each.update()
			each.draw(screen)
			if each.z < 250:
				each.d = -1
			else:
				each.d = 1
			if np.sqrt((each.x - 500) ** 2 + (each.y - 500) ** 2) > 249.9:
				each.d *= -1

def run():
	screen.fill((0, 0, 0))
	keys = pg.key.get_pressed()
	for each in objects:
		if keys[pg.K_UP]:
			each.vy = -5
		elif keys[pg.K_DOWN]:
			each.vy = 5
		else:
			each.vy = 0
		if keys[pg.K_LEFT]:
			each.vx = -5
		elif keys[pg.K_RIGHT]:
			each.vx = 5
		else:
			each.vx = 0
		each.update()

	drawObjects(screen)

while running:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False
			pg.quit()

	run()
	pg.display.flip()