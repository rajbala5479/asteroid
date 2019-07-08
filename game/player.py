from . import physicalobject, resources
import math
from pyglet.window import key

class Player(physicalobject.PhysicalObject):
    def __init__(self, *args, **kwargs):
        super().__init__(img=resources.player_image, *args, **kwargs)
        self.thrust = 300.0
        self.rotate_speed = 200.0
        self.keys = dict(left=False, right=False, up=False)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.keys['up'] = True
        elif symbol == key.LEFT:
            self.keys['left'] = True
        elif symbol == key.RIGHT:
            self.keys['right'] = True

    def on_key_release(self, symbol, modifiers):
        if symbol == key.UP:
            self.keys['up'] = False
        elif symbol == key.LEFT:
            self.keys['left'] = False
        elif symbol == key.RIGHT:
            self.keys['right'] = False

    def update(self, dt):
        super(Player, self).update(dt)
        if self.keys['left']:
            print(self.rotate_speed * dt)
            self.rotation -= self.rotate_speed * dt
            print("Rotation is now set to {}".format(self.rotation))
        if self.keys['right']:
            self.rotation += self.rotate_speed * dt
        if self.keys['up']:
            angle_radians = -math.radians(self.rotation)
            vel_x = math.cos(angle_radians) * self.thrust *dt
            vel_y = math.sin(angle_radians) * self.thrust *dt
            self.vel_x += vel_x
            self.vel_y += vel_y 