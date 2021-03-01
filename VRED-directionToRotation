import math

print "------"

def cross(a, b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]
    return c

def length(c):
    return math.sqrt(c[0]*c[0] + c[1]*c[1] + c[2]*c[2])

def normalize(c):
    l = length(c)
    c[0] /= l
    c[1] /= l
    c[2] /= l

def dot(a, b):
    return (a[0] * b[0] + a[1]*b[1] + a[2]*b[2])

# x-axis
x1 = 1
y1 = 0
z1 = 0
v1 = [x1, y1, z1]

# direction vector
x2 = -0.721401
y2 = -0.684584
z2 = 0.104528
v2 = [x2, y2, z2]
#print length(v2)

# calculate rotation from x-axis to direction vector

# c is a vector that is perpendicular to v1 and v2
c = cross(v1, v2)
normalize(c)

#print length(c)
#print "c: ", c

# calculate angle between v1 and v2

cosAlpha = dot(v1, v2)
alphaRad = math.acos(cosAlpha)
alphaDeg = alphaRad / math.pi * 180.0
print "angle: ", alphaDeg

# rotate around c
n = findNode("Group")
n.setAxisRotation(0,0,0, c[0], c[1], c[2], alphaDeg)
print "euler angles: ", n.getRotation()

# euler angles:  [14.967100143432617, -5.999963283538818, -136.50003051757812]
