import pygame as pg
from settings import *
class Weapon():
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.img = pg.image.load("texture/gun.png")
        self.img = pg.transform.scale(self.img,RES)
    def draw(self):
        self.create()
        pg.display.flip()
        pg.display.flip()

    def create (self):
        self.screen.blit(self.img, (0, 0))
        pg.display.flip()
        pg.display.flip()
    def fire (self):
        self.img = pg.image.load("texture/gun2.png")
        self.img = pg.transform.scale(self.img,RES)