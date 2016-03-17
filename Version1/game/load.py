# load asteroids

import pyglet, random, math
from game import resources
from pyglet.sprite import Sprite
from game.physical_object import PhysicalObject

def rocks(num_asteroids, player_position, batch=None):
    count = 0
    asteroids = []
    while count < num_asteroids:
        asteroid_pos = (random.randint(0, 800), random.randint(0, 600))
        if distance(player_position, asteroid_pos) > 200:
            new_asteroid = PhysicalObject(img=resources.asteroid,
                                          x=asteroid_pos[0],
                                          y=asteroid_pos[1], batch=batch)
            new_asteroid.rotation = random.randint(0, 360)
            new_asteroid.velocity_x = (random.random()*2 -1)*40
            new_asteroid.velocity_y = (random.random()*2 -1)*40
            asteroids.append(new_asteroid)
            count += 1
    return asteroids

def distance(point_1=(0, 0), point_2=(0, 0)):
    """Returns the duatance between 2 points"""
    return math.sqrt((point_1[0] - point_2[0]) ** 2 +
                     (point_1[1] - point_2[1]) ** 2)

def players_lives(num_icons, batch=None):
    lives_left = []
    for idx in range(num_icons):
        new_sprite = Sprite(img=resources.ship_stop, x=785-idx*30, y=585,
                            batch=batch)
        new_sprite.scale = 0.3
        lives_left.append(new_sprite)
    return lives_left
