from boid import Boid
from vector import Vector
import random

class FlockingSystem:

    maxForce = 1.0
    maxSpeed = 5.0
    sepRad = 100.0
    aliRad = 100.0
    cohRad = 200.0
    sepWeight = 1.0
    aliWeight = 1.0
    cohWeight = 1.0

    #initialize system by filling up boidList with randomly placed boids with random velocities
    def __init__(self, size, numBoids):
        self.boidList = []
        for i in range(numBoids):
            pos = Vector(size[0]*0.5 + (random.random()-0.5)*size[0]*0.5, size[1]*0.5 + (random.random()-0.5)*size[1]*0.5)
            vel = Vector(random.random()-0.5, random.random()-0.5)*2
            self.boidList.append(Boid(pos, vel, i))

    def separation(self):
        for boid in self.boidList:
            steer = Vector(0.0,0.0)
            count = 0.0
            for neighbour in self.boidList:
                if neighbour != boid and (neighbour.pos-boid.pos).size() < self.sepRad:
                    disp = boid.pos - neighbour.pos
                    dist = disp.size()
                    disp = disp.normalize()*(1.0/dist)
                    steer += disp
                    count += 1.0
            if count > 0.0:
                steer = steer.normalize()*self.maxSpeed
                steer -= boid.vel
                if steer.size() > self.maxForce:
                    steer = steer.normalize()*self.maxForce
                boid.acc += steer*self.sepWeight

    def alignment(self):
        for boid in self.boidList:
            steer = Vector(0.0,0.0)
            heading = Vector(0.0,0.0)
            count = 0.0
            for neighbour in self.boidList:
                if neighbour != boid and (neighbour.pos-boid.pos).size() < self.aliRad:
                    heading += neighbour.vel.normalize()
                    count += 1.0
            if count > 0.0:
                heading = heading.normalize()*self.maxSpeed
                steer = heading - boid.vel
                if steer.size() > self.maxForce:
                    steer = steer.normalize()*self.maxForce
                boid.acc += steer*self.aliWeight

    def cohesion(self):
        for boid in self.boidList:
            centre = Vector(0.0,0.0)
            count = 0.0
            for neighbour in self.boidList:
                if neighbour != boid and (neighbour.pos-boid.pos).size() < self.cohRad:
                    centre += neighbour.pos
                    count += 1.0
            if count > 0:
                centre *= (1/count)
                desired = centre - boid.pos
                desired = desired.normalize()*self.maxSpeed
                steer = desired - boid.vel
                if steer.size() > self.maxForce:
                    steer = steer.normalize()*self.maxForce
                boid.acc += steer*self.cohWeight

    #apply separation, alignment and cohesion, then move the boids
    def update(self):
        self.separation()
        self.alignment()
        self.cohesion()
        for boid in self.boidList:
            boid.updateAngle()
            boid.vel += boid.acc
            boid.pos += boid.vel
            boid.updateVel()
            boid.updatePos()
            boid.acc = Vector(0,0)
