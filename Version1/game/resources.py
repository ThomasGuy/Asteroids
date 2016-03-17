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

    



