import pyglet
import random
import math
from . import resources

def distance( point1 = (0,0) , point2= (0,0)):
    """Returns distance between two points"""
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1])**2 )

def asteroids(num_asteroid, player_position):
    asteroids = []
    for i in range(num_asteroid):
        asteroid_x, asteroid_y = player_position
        while distance( (asteroid_x, asteroid_y) , player_position) < 100:
            asteroid_x = random.randint(0,640)
            asteroid_y = random.randint(0,480)
        
        new_asteroid = pyglet.sprite.Sprite(img =resources.asteroid_image,
                        x= asteroid_x, y = asteroid_y)
        new_asteroid.rotation = random.randint(0,360)
        asteroids.append(new_asteroid)
    return asteroids