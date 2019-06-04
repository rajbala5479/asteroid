import pyglet

window = pyglet.window.Window()

label = pyglet.text.Label('Hello , world',
                        font_name='Times New Romab',
                        font_size = 36,
                        x = 0, y = 0,
                        anchor_x='left', anchor_y='baseline')


@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()