import pyglet
from game import load,resources

game_window = pyglet.window.Window()
upper_margin = game_window.height - 30
score_label = pyglet.text.Label(text="Score: 0", x=10, y=upper_margin)
level_label = pyglet.text.Label(text="My Amazing Game",
                                x=game_window.width/2, y=upper_margin, anchor_x='center')
window_size_label = pyglet.text.Label(text="{}x{}".format(game_window.width, game_window.height),
                                x=0, y = 0)

player_ship = pyglet.sprite.Sprite(img=resources.player_image, x= game_window.width/2, y = game_window.height/2)
player_ship.rotation = 45
asteroids = load.asteroids(100, player_ship.position)


@game_window.event
def on_draw():
    game_window.clear()

    player_ship.draw()
    for asteroid in asteroids:
        asteroid.draw()
    level_label.draw()
    score_label.draw()
    window_size_label.draw()

if __name__ == "__main__":
    pyglet.app.run()