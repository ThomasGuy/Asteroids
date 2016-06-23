__author__ = 'Tom Guy'

from . import resources, physical_object
import random


class Explosion(physical_object.PhysicalObject):
    def __init__(self, *args, **kwargs):
        boom = random.choice([0, 1, 2, 3])
        super().__init__(img=resources.effect_anims[boom],
                         info=resources.get_info('explosion'), *args, **kwargs)
        self.sound = resources.get_sound('explosion_sound')
        self.x -= self.center[0]
        self.y -= self.center [1]
        self.sound.play()

    def on_animation_end(self):
        self.delete()
        self.sound.stop()
