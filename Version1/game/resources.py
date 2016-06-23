<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Fri March 18 11:12:58 2016

@author: Tom
"""

import pyglet
from pyglet.image import Animation, AnimationFrame
from pyglet.resource import image
from res.images.info import Info
from .play_sound import Sounds


def create_effect_animation(image_name, columns, rows):
    """  Animate a sprite  """
    effect_seq = pyglet.image.ImageGrid(image_name, rows, columns)
    effect_frames = []
    for row in range(rows, 0, -1):
        end = row * columns
        start = end - (columns -1) -1
        for effect_frame in effect_seq[start:end:1]:
            effect_frames.append(AnimationFrame(effect_frame, 0.1))

    effect_frames[(rows * columns) -1].duration = None
    return Animation(effect_frames)

pyglet.resource.path = ["../res/images", "../res/images/Asteroids",
                        "../res/images/Spaceships -KaaR", "../res/sounds"]
pyglet.resource.reindex()
player_ship = pyglet.image.ImageGrid(image('double_ship.png'),1 , 2)
# DB of game sprites
# Info ( center, size, radius = 0, lifespan = None, animated = False )
sprites = {'nebula': (Info((400, 300), (800, 600)),
                      image('nebula_blue.f2014.png')),
           'debris': (Info((320, 240), (640, 480)),
                        image('debris2_blue.png')),
           'splash': (Info((200, 150), (400, 300)), image('splash.png')),
           'missile': (Info((5, 5), (10, 10), 2, 76), image('shot2.png')),
           'enemy_missile':(Info((5, 5), (10, 10), 2, 76), image('shot1.png')),
           'two_ship': (Info((45, 45), (90, 90), 35),
                        image('double_ship.png')),
           'engine_thrust': (Info((45, 45), (90, 90), 35), player_ship[1]),
           'engine_stop': (Info((45, 45), (90, 90), 35), player_ship[0]),
           'asteroid1': (Info((45, 45), (90, 90), 40),
                        image('asteroid_blue.png')),
           'asteroid2': (Info((45, 45), (90, 90), 40),
                         image('asteroid_blend.png')),
           'asteroid3': (Info((45, 45), (90, 90), 40),
                        image('asteroid_brown.png')),
           'explosion': (Info((64, 64), (128, 128), 17, 24, True),
                         image('explosion_alpha.png')),
           'explosion_blue': (Info((64, 64), (128, 128), 17, 24, True),
                            image('explosion_blue.png')),
           'explosion_blue2': (Info((64, 64), (128, 128), 17, 24, True),
                               image('explosion_blue2.png')),
           'explosion_orange': (Info((64, 64), (128, 128), 17, 24, True),
                                image('explosion_orange.png')),
           'background': (Info((400, 300), (800, 600)),
                            image('background_image.png'))}
# Enemy Space ship
enemy_ship = {
    'enemy'      : (Info((50, 43), (99, 85), 40), image('mine-1.png')),
    'enemy_right': (Info((51, 43), (101, 85), 40), image('mine-2.png')),
    'enemy_up'   : (Info((50, 44), (99, 88), 40), image('mine-3.png')),
    'enemy_left' : (Info((51, 43), (101, 85), 40), image('mine-4.png')),
    'enemy_down' : (Info((50, 44), (99, 88), 40), image('mine-5.png'))
}

# Dictionary of sounds
# Sounds ( 'track', volume = 0.8, streaming = False)
sounds  = {
    'soundtrack'        : Sounds('../res/sounds/wav/soundtrack.wav'),
    'missile_sound'     : Sounds('../res/sounds/wav/Laser_Shoot6.wav', volume=0.2),
    'thrust_sound'      : Sounds('../res/sounds/wav/space-engine-thrust.wav'),
    'explosion_sound'   : Sounds('../res/sounds/wav/explosion.wav')
    }

# Asteroid sprites list
roids = ['asteroid1', 'asteroid2', 'asteroid3']

# Animated sprites
effect_anims = [create_effect_animation(sprites['explosion'][1], 24, 1),
                create_effect_animation(sprites['explosion_orange'][1], 24, 1),
                create_effect_animation(sprites['explosion_blue2'][1], 24, 1),
                create_effect_animation(sprites['explosion_blue'][1], 24, 1)]

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2

for key in enemy_ship:
    center_image(enemy_ship[key][1])

center_image(sprites['missile'][1])
center_image(sprites['asteroid1'][1])
center_image(sprites['asteroid2'][1])
center_image(sprites['asteroid3'][1])
center_image(sprites['engine_thrust'][1])
center_image(sprites['engine_stop'][1])

def get_image(img):
    return sprites[img][1]

def get_info(img):
    return sprites[img][0]

def get_sound(track):
    return sounds[track]

=======
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 13:12:58 2016

@author: Tom
"""

import pyglet

pyglet.resource.path = ["../res/images"]
pyglet.resource.reindex()

nebula =        pyglet.resource.image('nebula_blue.f2014.png')
debris =        pyglet.resource.image('debris2_blue.png')
splash =        pyglet.resource.image('splash.png')
missile =       pyglet.resource.image('shot2.png')
double_ship =   pyglet.resource.image('double_ship.png')
asteroid =      pyglet.resource.image('asteroid_blue.png')
explosion =     pyglet.resource.image('explosion_alpha.png')
background =    pyglet.resource.image('background_image.png')

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2


center_image(missile)
center_image(asteroid)
ship = pyglet.image.ImageGrid(double_ship, 1, 2)
ship_go = ship[1]
ship_stop = ship[0]
center_image(ship_go)
center_image(ship_stop)

    



>>>>>>> origin/master
