from math import sqrt
from time import time

class VEC3:
    def __init__(self, px, py, pz):
        self.x = px
        self.y = py
        self.z = pz

    def add(self, pVEC, mult = 2):
        self.x += pVEC.x
        self.y += pVEC.y
        self.z += pVEC.z

    def sub(self, pVEC):
        self.x -= pVEC.x
        self.y -= pVEC.y
        self.z -= pVEC.z
    
    def differentiate(self, pOLDVEC, dt):
        self.x = (self.x + pOLDVEC.x) / dt
        self.y = (self.y + pOLDVEC.y) / dt
        self.z = (self.z + pOLDVEC.z) / dt

    def MAG(self):
        return (self.x**2 + self.y**2 + self.z**2) ** 1/2 

    def display(self):
        print(self.x)
        print(self.y)
        print(self.z)

class VEC2:
    ''' px -> left/right
        py -> up/down
    '''
    def __init__(self, px, py):
        self.x = px
        self.y = py
    
    def add(self, pVEC, mult = 1):
        self.x += pVEC.x * mult
        self.y += pVEC.y * mult
    
    def sub(self, pVEC):
        self.x -= pVEC.x
        self.y -= pVEC.y

    def differentiate(self, pOLDVEC, dt):
        self.x = (self.x + pOLDVEC.x) / dt
        self.y = (self.y + pOLDVEC.y) / dt

    def MAG(self):
        return sqrt(self.x**2 + self.y**2)
    
    def display(self):
        print(self.x, self.y)

class STAVEC2:
    def __init__(self, gy = -9.81, tx = 0, ty = 0):
        self.g = VEC2(0, gy)
        self.thrust = VEC2(tx, ty)

        self.a = VEC2(tx, ty - gy)
        self.v = VEC2(0, 0)
        self.p = VEC2(0, 0)
        self.start = time()
        self.t = time()
        self.dt = time() - self.t

    def CHANGE_A(self, gx, gy, tx, ty):
        self.a = VEC2(tx, gy - ty)

    def integrate(self):
        self.dt = time() - self.t
        self.v.add(self.a, self.dt)
        self.p.add(self.v, self.dt)
        self.t = time()

    def display(self):
        print("A")
        self.a.display()
        print("V")
        self.v.display()
        print("P")
        self.p.display()
        print(self.t - self.start)