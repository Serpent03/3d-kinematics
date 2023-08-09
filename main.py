class VEC3D:
    x = 0
    y = 0
    z = 0

    def __init__(self, px, py, pz):
        self.x = px
        self.y = py
        self.z = pz

    def add(self, pVEC):
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

    def display(self):
        print(self.x)
        print(self.y)
        print(self.z)


if __name__ == "__main__":
    shell = VEC3D(1, 1, 1)
    gravityVEC = VEC3D(0, 0, -9.8) # z => point down
    shell.display()



# TODO angle, compute angle to vector, extrapolate this vector into future/past positions
# 
# technically speaking, extrapolation into previous timestamp positions should be nothing more than
# just 'reverting' the speed losses one by one. There has to be a near constant jerk or snap value
# acting on the ballistic that is in charge of all the changes in position


