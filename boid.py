import math
from vector import Vector

class Boid:
    
    #acceleration of the boid
    acc = Vector(0,0)
    #angle of the boid from the x-axis
    angle = 0

    #initialize boid with position and velocity values
    def __init__(self, pos, vel, id):
        self.pos = pos
        self.x = pos.x
        self.y = pos.y
        self.vel = vel
        self.u = vel.x
        self.v = vel.y
        self.id = id

    #operator overload ==, !=
    def __eq__(self, flockmate):
        return self.id == flockmate.id
    def __ne__(self, flockmate):
        return self.id != flockmate.id

    #updates the x and y components of boid after the vector pos is changed
    def updatePos(self):
        self.x = self.pos.x
        self.y = self.pos.y
    #updates the u and v components of boid after the vector vel is changed
    def updateVel(self):
        self.u = self.vel.x
        self.v = self.vel.y
    #updates the boid angle so that the boid points along its velocity
    def updateAngle(self):
        self.angle = math.degrees(-math.atan2(self.v,self.u))