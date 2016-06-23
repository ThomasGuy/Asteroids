# spawn asteroids

import random
from pyglet.sprite import Sprite
from . import resources, helper, Asteroid


def rocks(num_asteroids, player_position, batch=None):
    count = 0
    asteroids = set()
    while count < num_asteroids:
        asteroid_pos = (random.randint(0, 800), random.randint(0, 600))
        if helper.distance(player_position, asteroid_pos) > 100:
            rock = random.choice(resources.roids)
            new_asteroid = Asteroid(img=resources.get_image(rock),
                                             info=resources.get_info(rock),
                                             x=asteroid_pos[0],
                                             y=asteroid_pos[1], batch=batch)
            asteroids.add(new_asteroid)
            count += 1
    return asteroids

def players_lives(num_icons, batch=None):
    lives_left = []
    for idx in range(num_icons):
        new_sprite = Sprite(img=resources.get_image('engine_stop'),
                            x=785-idx*30, y=585, batch=batch)
        new_sprite.scale = 0.3
        lives_left.append(new_sprite)
    return lives_left
