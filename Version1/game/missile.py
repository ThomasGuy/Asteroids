# Missile class

import pyglet
from . import physical_object


class Missile(physical_object.PhysicalObject):
    """
     Missiles fired by player
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.speed = 700.0
        pyglet.clock.schedule_once(self.die, 1.1)
        self.sound.play()

    def die(self, dt):
        self.dead = True
        self.sound.stop()
