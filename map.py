import pygame as pg
from settings import *
_ = False
template = [
    [_,_,_,_,_,_,_,_,1,_,_,_,_,_,_,_],
    [_,_,_,_,_,1,1,_,1,1,_,_,_,_,_,_],
    [_,_,_,_,_,1,_,_,_,1,_,_,_,_,_,_],
    [_,_,1,_,_,_,_,_,_,_,_,_,_,1,_,_],
    [_,_,_,_,_,1,_,_,_,1,_,_,_,_,_,_],
    [_,_,1,_,_,1,1,_,1,1,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,_,_,_,_,1,_,_,_],
       ]


class Map:
    def __init__(self, game):
        self._ = False
        self.game = game
        self.template = template
        self.main_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.template):
            for i, value in enumerate(row):
                if value:
                    self.main_map[(i, j)] = value

    def destroy_wall(self,index1,index2):
        self.template[index1][index2] = self._

    def create_wall(self,index1,index2):
        self.template[index1][index2] = 1


    # def draw(self): draw map for debuging
    #     [pg.draw.rect(self.game.screen, "red", (pos[0] * 100, pos[1] * 100,100,100), 5)
    #     for pos in self.main_map]