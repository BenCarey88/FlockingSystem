import math

#for now I'm just using 2d vectors
class Vector:

    #constructor
    def __init__(self,x,y):
        self.x = x
        self.y = y

    #operator overloading +, -, *, /   
    def __add__(self, v):
        return Vector(self.x+v.x, self.y+v.y)
    def __sub__(self, v):
        return Vector(self.x-v.x, self.y-v.y)
    def __mul__(self,s):
        return Vector(s*self.x, s*self.y)

    #dot product, magnitude, normalize
    def dot(self, v):
        return self.x*v.x + self.y*v.y
    def size(self):
        return math.sqrt(self.x*self.x + self.y*self.y)
    def normalize(self):
        return self*(1/self.size())