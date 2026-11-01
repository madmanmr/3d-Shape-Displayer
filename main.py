import pygame as pg
import numpy as np
from Object_Class import Object

pg.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.time.Clock()

objects = []

shapeName = {
	"circle": "Circle",
	"square": "Square",
}



running = True

def createCircle():
	radius = 250
	xbase = np.random.uniform(-radius, radius)
	ybase = np.random.uniform(np.sqrt(radius**2 - xbase**2) *  -1, np.sqrt(radius**2 - xbase**2))
	zmax = np.sqrt(radius ** 2 - xbase ** 2 - ybase ** 2)
	zbase = np.random.choice([-zmax, zmax])
	x = xbase + 500
	y = ybase + 500
	z = zbase + 500
	#print(x,y,z)

	object = Object(x,y,z)
	objects.append(object)

def createSquare():
	halfWidth = 250
	xbase = np.random.uniform(-halfWidth, halfWidth)
	ybase = np.random.uniform(-halfWidth, halfWidth)
	zbase = np.random.choice([-halfWidth, halfWidth])
	x = xbase + 500
	y = ybase + 500
	z = zbase + 500

	object = Object(x, y, z)
	objects.append(object)

for amount in range(1000):
	createCircle()

def drawObjects(screen):
	for each in objects:
		each.draw(screen)

def run():
	screen.fill((0, 0, 0))
	keys = pg.key.get_pressed()

	for each in objects:
		each.vx = 0
		each.vy = 0
		each.vz = 0

		if keys[pg.K_w] or keys[pg.K_UP]:
			each.vy = -1
		if keys[pg.K_s] or keys[pg.K_DOWN]:
			each.vy = 1
		if keys[pg.K_a] or keys[pg.K_LEFT]:
			each.vx = -1
		if keys[pg.K_d] or keys[pg.K_RIGHT]:
			each.vx = 1
		if keys[pg.K_q]:
			each.vz = -1
		if keys[pg.K_e]:
			each.vz = 1

		each.update()

	drawObjects(screen)
while running:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False
			pg.quit()

	run()
	pg.display.flip()