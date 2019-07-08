import pyglet
import random
import math
from . import resources, physicalobject

def distance( point1 = (0,0) , point2= (0,0)):
    """Returns distance between two points"""
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1])**2 )

def asteroids(num_asteroid, player_position, batch = None):
    asteroids = []
    for i in range(num_asteroid):
        asteroid_x, asteroid_y = player_position
        while distance( (asteroid_x, asteroid_y) , player_position) < 100:
            asteroid_x = random.randint(0,640)
            asteroid_y = random.randint(0,480)
        
        new_asteroid = physicalobject.PhysicalObject(img =resources.asteroid_image,
                        x= asteroid_x, y = asteroid_y, batch = batch)
        new_asteroid.rotation = random.randint(0,360)
        new_asteroid.vel_x = random.random() * 40
        new_asteroid.vel_y = random.random() * 40
        asteroids.append(new_asteroid)
    return asteroids

def player_lives( livesCount, batch = None):
    player_lives = []
    for i in range(livesCount):
        player_live = physicalobject.PhysicalObject( img = resources.player_image,
                        x= 575 + i* 25 , y = 450, batch = batch)
        player_live.scale = 0.5
        player_lives.append(player_live)
    return player_lives