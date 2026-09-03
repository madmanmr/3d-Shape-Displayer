import pygame as pg
import numpy as np


class Object:

	def __init__(self,x,y,z,pos):
		self.x = x
		self.y = y
		self.z = z
		self.pos = pos

	def draw(self, screen):
		radius = self.z
		pg.draw.circle (screen, (255,255,255), (self.x, self.y), radius)