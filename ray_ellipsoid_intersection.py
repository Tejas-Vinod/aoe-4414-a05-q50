# ray_ellipsoid_intersection.py
#
# Usage: python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z c_s_x c_s_y c_s_z r_s
# Parameters:
#  d_l_x: x-coordinate of origin-referenced ray unit vector
#  d_l_y: y-coordinate of origin-referenced ray unit vector
#  d_l_z: z-coordinate of origin-referenced ray unit vector
#  c_l_x: x-coordinate of ray origin vector
#  c_l_y: y-coordinate of ray origin vector
#  c_l_z: z-coordinate of ray origin vector
#  c_s_x: x-coordinate of the ellipsoid origin offset
#  c_s_y: y-coordinate of the ellipsoid origin offset
#  c_s_z: z-coordinate of the ellipsoid origin offset
#  r_s: radius of the ellipsoid
# Output:
#  Print the x y z of 
#
# Written by Tejas Vinod
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.
# Test:
# python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z c_s_x c_s_y c_s_z r_s

# import Python modules
# e.g., import math # math module
import sys # argv
import math # math module

# "constants"
R_E_KM = 6378.137
E_E    = 0.081819221456

# helper functions

## vector magnitude
def mag(v):
    sum_of_squares = 0.0
    for i in range(0,len(v)):
        sum_of_squares += v[i]*v[i]
    return math.sqrt(sum_of_squares)

## scalar multiplication
def smul(s,v):
    sprod = []
    for i in range(0,len(v)):
        sprod.append(s*v[i])
    return sprod

## vector addition
def add(v1,v2):
    if len(v1) != len(v2):
        return None
    else:
        v3 = []
        for i in range(0,len(v1)):
            v3.append(v1[i]+v2[i])
        return v3

## vector subtraction
def sub(v1,v2):
    if len(v1) != len(v2):
        return None
    else:
        v3 = []
        for i in range(0,len(v1)):
            v3.append(v1[i]-v2[i])
        return v3

## dot product
def dot(v1,v2):
    if len(v1) != len(v2):
        return float('nan')
    else:
        dp = 0.0
        for i in range(0,len(v1)):
            dp += v1[i]*v2[i]
        return dp     

# initialize script arguments
d_l_x = float('nan') # x-coordinate of origin-referenced ray unit vector
d_l_y = float('nan') # y-coordinate of origin-referenced ray unit vector
d_l_z = float('nan') # z-coordinate of origin-referenced ray unit vector
c_l_x = float('nan') # x-coordinate of ray origin vector
c_l_y = float('nan') # y-coordinate of ray origin vector
c_l_z = float('nan') # z-coordinate of ray origin vector

# parse script arguments
if len(sys.argv)==7:
    d_l_x = float(sys.arv[1]) # x-coordinate of origin-referenced ray unit vector
    d_l_y = float(sys.arv[2]) # y-coordinate of origin-referenced ray unit vector
    d_l_z = float(sys.arv[3]) # z-coordinate of origin-referenced ray unit vector
    c_l_x = float(sys.arv[4]) # x-coordinate of ray origin vector
    c_l_y = float(sys.arv[5]) # y-coordinate of ray origin vector
    c_l_z = float(sys.arv[6]) # z-coordinate of ray origin vector
else:
  print(\
   'Usage: '\
   'python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z'\
  )
  exit()

# write script below this line
d_l = [d_l_x, d_l_y, d_l_z] # *** MUST be a unit vector
c_l = [c_l_x, c_l_y, c_l_z] 

## discriminant
a = dot(d_l_x,d_l_x) + dot(d_l_y,d_l_y) + dot(d_l_z,d_l_z)/(1-E_E**2)
b = 2.0*(dot(d_l_x,c_l_x) + dot(d_l_y,c_l_y) + dot(d_l_z,c_l_z)/(1-E_E**2))
c = dot(d_l_x,c_l_x) + dot(d_l_y,c_l_y) + dot(d_l_z,c_l_z)/(1-E_E**2)-R_E_KM**2
discr = b*b-4.0*a*c

## solution logic
if discr>=0.0:
    d = (-b-math.sqrt(discr))/(2*a)
    if d<0.0:
        d = (-b+math.sqrt(discr))/(2*a)
    if d>=0.0:
        l_d = add(smul(d,d_l),c_l)
        print(l_d[0])
        print(l_d[1])
        print(l_d[2])