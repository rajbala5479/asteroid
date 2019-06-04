import math

class Renderer:

    # Convenience methods
    def drawCircle( self, radius = 10, res = 30):
        pass


class FilledPolygon():
    def __init__():
        pass
    
    def render(self):
        if len

class PolyLine():
    def __init__():
        pass

def make_circle(radius = 10, res = 20, filled = True):
    points = []
    for i in range(res):
        ang = 2*math.pi * i / res
        points.append((math.cos(ang) * radius, math.sin(ang) * radius) )
    if filled:
        return FilledPolygon(points)
    else:
        return PolyLine(points, True)