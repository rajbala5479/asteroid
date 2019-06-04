from Box2D import (b2PolygonShape, b2World)

# Default gravity is (0,-10) and do Sleep is True
world = b2World()

groundBody = world.CreateStaticBody(
    position = (0,-10),
    shapes = b2PolygonShape(box= (50,10))
)

# Create a dynamic body at (0,4)
body = world.CreateDynamicBody(position=(0,4))

box = body.CreatePolygonFixture( box=(1,1) , density=1, friction=0.3)

timeStep = 1.0/60

vel_iters, pos_iters = 6,2

# Our game loop
for i in range(100):
    world.Step( timeStep, vel_iters, pos_iters)

    world.ClearForces()

    print(body.position, body.angle)