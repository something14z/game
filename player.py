from settings import*
import pygame as pg
import math

class Player:
    def __init__(self,game):
        self.game = game
        self.x , self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.rel = 0
        self.last_mouse_x = pg.mouse.get_pos()[0]

    def movement(self):
        sin1 = math.sin(self.angle)
        cos1 = math.cos(self.angle)
        dx, dy = 0, 0
        speed = P_SPEED * self.game.deltatime
        speed_sin = speed * sin1
        speed_cos = speed * cos1


        key = pg.key.get_pressed()
        self.new_mouse_x = pg.mouse.get_pos()[0]
        delta = abs(self.new_mouse_x - self.last_mouse_x)
        if self.new_mouse_x > self.last_mouse_x:
            self.angle += P_R_SPEED * self.game.deltatime
        if self.new_mouse_x < self.last_mouse_x:
            self.angle -= P_R_SPEED * self.game.deltatime
        pg.mouse.set_pos(WIDTH//2,HEIGHT//2)
        self.last_mouse_x = WIDTH//2
        pg.mouse.set_visible(False)
        if key[pg.K_w]:
            dx += speed_cos
            dy += speed_sin

        if key[pg.K_a]:
            dx += -speed_sin
            dy += -speed_cos

        if key[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin

        if key[pg.K_d]:
            dx += speed_sin
            dy += speed_cos

        self.check_wall_collision(dx,dy)

        if key[pg.K_e]:
            self.angle -= P_R_SPEED * self.game.deltatime
        if key[pg.K_q]:
            self.angle += P_R_SPEED * self.game.deltatime

        self.angle %= math.tau

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.main_map

    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy

    # def draw(self):draw player for debug
    #     pg.draw.line(self.game.screen, "green", (self.x*100,self.y*100),(self.x * 100 + WIDTH * math.cos(self.angle), self.y * 100+ WIDTH * math.sin(self.angle)),2)
    #     pg.draw.circle(self.game.screen, "green",( self.x * 100,self.y * 100 ), 15)
    def update(self):
        self.movement()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)