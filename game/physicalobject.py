import pyglet

class PhysicalObject(pyglet.sprite.Sprite):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vel_x , self.vel_y = 0.0 , 0.0

    def update ( self, dt):
        """This method should be called in every frame."""
        self.x += self.vel_x *dt
        self.y += self.vel_y *dt

        # Wrap aroung the screen if it tries to fly away
        self.check_bound()
    
    def check_bound (self):
        if self.x < 0 or self.x > 640:
            self.vel_x = -self.vel_x
        if self.y < 0 or self.y > 480:
            self.vel_y = - self.vel_y