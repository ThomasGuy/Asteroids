# players ship physics

#from game.physical_object import PhysicalObject
import math
from game import physical_object, resources
from pyglet.window import key
import pyglet

class Player(physical_object.PhysicalObject):
    """
    Here we use a sub sub class of Sprite. We need to make this class an
    event handler in 'asteroids'.
    """
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img=resources.ship_stop, *args, **kwargs)
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
        """
        we need to call PhysicalObject‘s update() method and then respond to
        input
        """
        super(Player, self).update(dt)

        if self.keys['left']:
            self.rotation -= self.rotate_speed * dt
        if self.keys['right']:
            self.rotation += self.rotate_speed * dt
        '''
        Note that Sprite object's rotation attributes are in degrees, with
        clockwise as the positive direction. This means that you need to call
        math.degrees() or math.radians() and make the result negative whenever
        you use Python’s built-in math functions with the Sprite class, since
        those functions use radians instead of degrees, and their positive
        direction is counter-clockwise.
        '''
        if self.keys['up']:
            angle_radians = -math.radians(self.rotation)
            force_x = math.cos(angle_radians) * self.thrust * dt
            force_y = math.sin(angle_radians) * self.thrust * dt
            self.velocity_x += force_x
            self.velocity_y += force_y
