import pyglet
from game import load, player

main_batch = pyglet.graphics.Batch()

game_window = pyglet.window.Window()
upper_margin = game_window.height - 30

score_label = pyglet.text.Label(text="Score: 0", x=10, y=upper_margin, batch = main_batch)
level_label = pyglet.text.Label(text="My Amazing Game",
                                x=game_window.width/2, y=upper_margin, anchor_x='center', batch=main_batch)
window_size_label = pyglet.text.Label(text="{}x{}".format(game_window.width, game_window.height),
                                x=0, y = 0, batch = main_batch)

player_ship = player.Player(x= game_window.width/2, y = game_window.height/2, batch = main_batch)
player_ship.rotation = 0
asteroids = load.asteroids(3, player_ship.position, batch = main_batch)
player_lives = load.player_lives(3, main_batch)

game_objects = [player_ship] + asteroids


def update(dt):
    for obj in game_objects:
        obj.update(dt)

def print_frame_rate(dt):
    print("{0} is the fram rate".format(pyglet.clock.get_fps()))

@game_window.event
def on_draw():
    game_window.clear()
    game_window.push_handlers(player_ship)
    main_batch.draw()
    #print("{0} seconds elapsed".format(pyglet.clock.tick()))

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1/120.0)
    #pyglet.clock.schedule_interval(print_frame_rate,1)
    pyglet.app.run()