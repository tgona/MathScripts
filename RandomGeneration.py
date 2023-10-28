import random
import math

def random_point_in_circle(radius):
    # Generate a random angle in radians
    theta = random.uniform(0, 2 * math.pi)
    
    # Generate a random radius within the given circle's radius
    r = math.sqrt(random.uniform(0, 1)) * radius
    
    # Convert polar coordinates to Cartesian coordinates
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    
    return (x, y)
def getDistance(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5
# Example usage:
r = 1.0
count = 0
steps = 100000
for i in range(steps):
    tmp1 = random_point_in_circle(r)
    tmp2 = random_point_in_circle(r)
    if getDistance(tmp1[0],tmp1[1],0,0) <= getDistance(tmp2[0]+1,tmp2[1],0,0):
        count += 1
print(count/steps)
