import pyglet

game_window = pyglet.window.Window()

@game_window.event
def on_draw():
    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
        [0, 1, 2, 0, 2, 3],
        ('v2i', (100, 100,
                150, 100,
                150, 150,
                100, 150))
    )

if __name__ == "__main__":
    pyglet.app.run()