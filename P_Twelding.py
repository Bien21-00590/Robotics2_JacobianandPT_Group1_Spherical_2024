import roboticstoolbox as rtb
import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH
from roboticstoolbox.backends.PyPlot import PyPlot
import math
import spatialmath
from spatialmath import SE3


## SPHERICAL MANIPULATOR MODEL

# link lengths in mm
a1 = float(input("a1 = "))## 40
a2 = float(input("a2 = "))## 10
a3 = float(input("a3 = "))## 15



## CREATE LINKS
## Robot_variable = DHRobot([RevoluteDH(d,r,alpha,offset=theta,qlim)])
## Robot_variable = DHRobot([PrismaticDH(d=0,r,alpha,offset=d,qlim)])


Spherical = DHRobot([
RevoluteDH(a1/100,0,(90/180)*np.pi,(0/180)*np.pi,qlim=[(-90/180)*np.pi/2,(90/180)*np.pi/2]),
RevoluteDH(0,0,(90/180)*np.pi,(90/180)*np.pi,qlim=[(-90/180)*np.pi/2,(90/180)*np.pi/2]),
PrismaticDH(0,0,(0/180)*np.pi,(a3+a2)/100,qlim=[0,10]),
], name="Spherical") 

print(Spherical)

## path and trajectory planning
## q paths
## Spherical Joint Variable = T1, T2, d3

## degrees to radian

def deg_rad(T):
    return (T/180)*np.pi


q0 = np.array([0,0,0]) ## origin of mechanical manipulator

q1 = np.array([deg_rad(float(-60)),
               deg_rad(float(-25)),
               (float(2.5))/100])

q2 = np.array([deg_rad(float(60)),
               deg_rad(float(-25)),
               (float(2.5))/100])

q3 = np.array([deg_rad(float(60)),
               deg_rad(float(25)),
               (float(10))/100])

q4 = np.array([deg_rad(float(-60)),
               deg_rad(float(25)),
               (float(10))/100])


## trajectory commands

traj1 = rtb.jtraj(q0,q1, 25)
traj2 = rtb.jtraj(q1,q2, 25)
traj3 = rtb.jtraj(q2,q3, 25)
traj4 = rtb.jtraj(q3,q4, 25)

Spherical.plot(traj1.q, limits=[-.7,.7,-.7,.7,0,.7])
Spherical.plot(traj2.q, limits=[-.7,.7,-.7,.7,0,.7])
Spherical.plot(traj3.q, limits=[-.7,.7,-.7,.7,0,.7])
Spherical.plot(traj4.q, limits=[-.7,.7,-.7,.7,0,.7],block=True,)



