from os import access

import pygame as pg
import numpy as np


class Object:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.theta = np.arctan2(z - 500, x - 500)
        self.phi = np.arccos((y - 500)/ 250)
        self.vx = 0
        self.vy = 0
        self.vz = 0
        self.radius = 0

    def update(self):
        self.x -= 500
        self.y -= 500
        self.z -= 500 #for calcs

        horz = self.vx * 0.01
        vert = self.vy * 0.01
        diag = self.vz * 0.01

        x = self.x
        z = self.z

        #y axis
        self.x = x * np.cos(horz) - z * np.sin(horz)
        self.z = x * np.sin(horz) + z * np.cos(horz)

        y = self.y
        z = self.z

        #x axis
        self.y = y * np.cos(vert) - z * np.sin(vert)
        self.z = y * np.sin(vert) + z * np.cos(vert)

        x = self.x
        y = self.y

        #z axis
        self.x = x * np.cos(diag) - y * np.sin(diag)
        self.y = x * np.sin(diag) + y * np.cos(diag)

        self.x += 500
        self.y += 500
        self.z += 500
        z = self.z - 500
        self.radius = max(1,(z / 90) + 10) #should probnabaly change cause far back is too small

    def draw(self, screen):
        z = self.z - 500
        c = int((z / 5) + 155)
        pg.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius)