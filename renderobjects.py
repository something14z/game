import pygame as pg
from settings import *


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()

    def draw2(self):

        self.render_game_obj()
    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
    def render_game_obj(self):
        self.screen.fill((255,255,255))
        object_list = self.game.raycast.objects_to_render
        for depth,image,pos in object_list:
            self.screen.blit(image,pos)
        pg.display.flip()

    def load_wall_textures(self):
        return {
            1: self.get_texture('texture/1.png'),

        }