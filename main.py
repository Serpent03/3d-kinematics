import matplotlib.pyplot as plt
from VEC import VEC2, STAVEC2, VEC3
from time import sleep

shell = STAVEC2(-9.81, 20, 5)


while (shell.t - shell.start) <= 5:
    shell.integrate()
    sleep(0.01)

shell.display() 



# TODO angle, compute angle to vector, extrapolate this vector into future/past positions
# 
# technically speaking, extrapolation into previous timestamp positions should be nothing more than
# just 'reverting' the speed losses one by one. There has to be a near constant jerk or snap value
# acting on the ballistic that is in charge of all the changes in position


