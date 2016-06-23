<<<<<<< HEAD
# players ship physics

from . import resources, helper, physical_object, missile
from pyglet.window import key
from pyglet.sprite import Sprite
import math


class Player(physical_object.PhysicalObject):
    """
    Here we use a sub sub class of Sprite. We need to make this class an
    event handler in 'Version3'.
    """
    def __init__(self, dimension, *args, **kwargs):
        super().__init__(img=resources.get_image('engine_stop'),
                         info=resources.get_info('engine_stop'),
                         *args, **kwargs)
        self.dimension = dimension
        # Tell the game handler about any event handlers
        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]
        # constants to adjust
        self.thrust = 300.0
        self.rotate_speed = 200.0
        self.friction = 1.0
        # Create a child sprite to show when ship is thrusting
        self.ship_engine = Sprite(img=resources.get_image('engine_thrust'),
                                  *args, **kwargs)
        self.ship_engine.scale = 0.75
        self.ship_engine.visible = False
        # New missiles to add to game_objects
        self.new_missiles = set()
        self.sound = resources.get_sound('thrust_sound')

    def update(self, dt):
        """
        We need to call PhysicalObject‘s update() method and then respond to
        input
        """
        super().update(dt)
        self.velocity_x *= self.friction
        self.velocity_y *= self.friction

        if self.key_handler[key.LEFT] or self.key_handler[key.A]:
            self.rotation -= self.rotate_speed * dt
        if self.key_handler[key.RIGHT]or self.key_handler[key.D]:
            self.rotation += self.rotate_speed * dt
        if self.key_handler[key.UP] or self.key_handler[key.W]:
            vector = helper.angle_to_vector(-math.radians(self.rotation))
            self.velocity_x += vector[0] * self.thrust * dt
            self.velocity_y += vector[1] * self.thrust * dt
            self.ship_engine.rotation = self.rotation
            self.ship_engine.x = self.x
            self.ship_engine.y = self.y
            self.ship_engine.visible = True
            #self.sound.rewind()
            self.sound.play()
        else:
            self.ship_engine.visible = False
            self.sound.stop()

        if self.enemy:
            if self.key_handler[key.SPACE]:
                self.fire()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            self.fire()

    def fire(self):
        vector = helper.angle_to_vector(-math.radians(self.rotation))
        missile_x = self.x + vector[0] * self.radius
        missile_y = self.y + vector[1] * self.radius
        new_missile = missile.Missile(x=missile_x, y=missile_y, batch=self.batch,
                                dimension=self.dimension,
                                img=resources.get_image('missile'),
                                info=resources.get_info('missile'),
                                sound=resources.get_sound('missile_sound')
                              )
        new_missile.velocity_x = (self.velocity_x + vector[0] * new_missile.speed)
        new_missile.velocity_y = (self.velocity_y + vector[1] * new_missile.speed)
        self.new_missiles.add(new_missile)

    def delete(self):
        self.ship_engine.delete()
        super().delete()
=======
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
>>>>>>> origin/master
