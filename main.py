import pygame as pg
from settings import *
import sys
from map import *
from player import *
from raycasting import *
from renderobjects import *
from gun import *
BROWN = (49,23,23)
class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.deltatime = 1
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.objects = ObjectRenderer(self)
        self.raycast = Raycast(self)
        self.gun = Weapon(self)

    def update (self):
        self.player.update()
        self.raycast.update()
        pg.display.flip()
        pg.display.flip()
        self.deltatime = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')




    def check_events (self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit

    def draw (self):

        ground = pg.image.load("texture/ground.png")
        ground = pg.transform.scale(ground, (WIDTH, HEIGHT))
        self.screen.blit(ground, pg.Rect(0,0, WIDTH, HEIGHT))
        sky = pg.image.load("texture/sky.png")
        sky = pg.transform.scale(sky,(WIDTH, HALF_HEIGHT))
        self.screen.blit(sky, pg.Rect(0,0, WIDTH, HALF_HEIGHT))
        self.objects.draw2()
        self.gun.draw()

    def run (self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()