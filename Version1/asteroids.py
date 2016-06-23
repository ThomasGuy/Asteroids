# Temp res test

import pyglet
import pyglet.image as image
from game import load, player, resources

game_window = pyglet.window.Window(800, 600)
main_batch = pyglet.graphics.Batch()
num_lives = 3
score_label = pyglet.text.Label(text="Score: 0", x=10, y=575, batch=main_batch)
level_label = pyglet.text.Label(text="Version 1: Static Graphics",
                                x=400, y=575, anchor_x = 'center',
                                batch=main_batch)
player_ship = player.Player(x=400, y=300, batch=main_batch)
asteroids = load.rocks(5, player_ship.position, main_batch)

lives_left = load.players_lives(num_lives, main_batch)
game_objects =  asteroids + [player_ship]
game_window.push_handlers(player_ship)

@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()

def update(dt):
    for obj in game_objects:
        obj.update(dt)


if __name__=='__main__':
    pyglet.clock.schedule_interval(update, 1/120.0)
    #pyglet.clock.schedule_interval(on_draw, 1/120.0)
    pyglet.app.run()
