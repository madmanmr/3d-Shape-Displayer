from os import access

import pygame as pg
import numpy as np


class Object:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.acc = 0
        self.vx = 0
        self.vy = 0
        self.vz = 0
        self.d = 1

    def update(self):
        self.x += self.vx * self.d
        self.y += self.vy * self.d

        xbase = self.x - 500
        ybase = self.y - 500

        self.z = 500 + np.sqrt(250 ** 2 - xbase ** 2 - ybase ** 2) * self.d

    def draw(self, screen):
        radius = max(1, (500 - self.z) / 15)
        c = min(255, int(abs(self.z - 500) + 5))
        pg.draw.circle(screen, (c,c,c), (int(self.x), int(self.y)), int(radius))