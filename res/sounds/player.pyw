# Play Sounds

import pygame as pg

class Sounds:
    def __init__(self, track):
        self.sound = track
        self.mixer = pg.mixer.init()
        
    def play_music(self, volume=0.8):
        '''
        stream music with mixer.music module in a blocking manner
        this will stream the sound from disk while playing
        '''
        # set up the mixer
        freq = 44100     # audio CD quality
        bitsize = -16    # unsigned 16 bit
        channels = 2     # 1 is mono, 2 is stereo
        buffer = 2048    # number of samples (experiment to get best sound)
        pg.mixer.init(freq, bitsize, channels, buffer)
        pg.mixer.music.set_volume(volume)    # volume value 0.0 to 1.0
        clock = pg.time.Clock()
        try:
            pg.mixer.music.load(self.sound)
            print("Music file {} loaded!".format(self.sound))
        except pg.error:
            print("File {} not found! ({})".format(self.sound, pg.get_error()))
            return
        pg.mixer.music.play()
        
        while pg.mixer.music.get_busy():
            # check if playback has finished
            clock.tick(30)
        

    def play(self, volume=0.8):
        pg.mixer_music.load(self.sound)
        pg.mixer_music.set_volume(volume)
        pg.mixer_music.play()

    def stop(self):
        pg.mixer_music.stop()

    def rewind(self):
        pg.mixer_music.rewind()
        
    
if __name__=='__main__':
    sound = file='missile.mp3'
    Sounds.play(sound)
    
