# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:31:27 2016

@author: Tom
"""

import pyglet
pyglet.lib.load_library('avbin64')
pyglet.have_avbin=True

class Sounds:
    def __init__(self, track, stream=False):
        self.stream = stream
        self.sound = pyglet.media.load(track, streaming=self.stream)
        self.player = pyglet.media.Player()
        
    def play(self, volume=0.8):
        self.player.queue(self.sound)
        #self.player.volume(self.volume)
        self.player.play()
        
    def pause(self):
        self.player.pause()
        
    def rewind(self):
        self.player.seek(0)
        self.player.pause()
        
if __name__=='__main__':
    _track = Sounds('missile.mp3')
    _track.play()
    _track.rewind()
    _track.pause()