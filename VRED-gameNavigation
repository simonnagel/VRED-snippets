#press W,A,S,D to move camera
#press Q and E to rotate
#use mouse for change view

# know bugs
# cannot press Q,E at the same time as W,A,S,D
# if pressed W too long and going "upwards" camera goes back on ground

import math
import time
from datetime import datetime

# this example demonstrates how to force screen updates all the time

# define class that calls a render update every frame


class RenderAction(vrInteraction):
    def __init__(self):
        vrInteraction.__init__(self)
        self.addRender()
    def preRender(self):               
        
        setHumanHeight()
        
        isKeyPressed()
        
        #printTime()

# create and activate render update object
render = RenderAction()
setNavigationSpeedMode(0)
import keyboard
from math import sqrt
cam = getActiveCameraNode()

#dummy = findNode("dummy")

def isKeyPressed():
    global cam
    global camPos
    global collisionDistanceFront
    #print collisionDistanceFront
    global collisionDistanceBack
    global collisionDistanceRight
    global collisionDistanceLeft
    setNavigationSpeedMode(2)
    x = 0
    y = 0
    speedForward = 0.1
    speedSideward = 100
    setPanningSpeed(1)
    setDollySpeed(1)
    active = 0    
   
    
    if keyboard.is_pressed('q'):
        camRotFunc(5)
        active = 0
    if keyboard.is_pressed('e'):
        camRotFunc(-5)
        active = 0     
    if keyboard.is_pressed('w'):
        if collisionDistanceFront> 500:
            setCameraZoom(-speedForward)
            y = 1
            active = 1
    if keyboard.is_pressed('s'):
        if collisionDistanceBack> 500:
            setCameraZoom(speedForward)
            y = -1
            active = 1
    if keyboard.is_pressed('a'):
        if collisionDistanceLeft> 500:
            setCameraPanning(speedSideward, 0)
            x = 1
            active = 1
    if keyboard.is_pressed('d'):
        if collisionDistanceRight> 500:
            setCameraPanning(-speedSideward, 0)
            x =-1
            active = 1
    if keyboard.is_pressed('x'):  
        setCameraZoom(-10)    
    if active == 1:
        setNavMode(3)
        setAllNavigationsEnabled(0)
        
    else:
        setNavMode(4)
        setAllNavigationsEnabled(1)


def setHumanHeight():
    global camPos
    camPos = cam.getTranslation()
    camPosWorld = cam.getWorldTransform
    global collisionDistanceFront
    global collisionDistanceBack   
    global collisionDistanceRight
    global collisionDistanceLeft
    #get the distance to ground
    rayOrigin = Pnt3f(camPos[0],camPos[1],camPos[2])
    rayDirection = Vec3f(0,0,-1)
    intersection = getSceneIntersection(-1, rayOrigin, rayDirection)
    interPos = intersection[1]
    bestInterPos = interPos.z()
    '''
    x = (camPos[0], camPos[1], camPos[2])  
      
    #get the distance to front
    v = Vec3f(0,0,-1)
    rayDirectionFront = Vec3f(camPosWorld[0] * v.x() + camPosWorld[1] * v.y() + camPosWorld[2] * v.z() , camPosWorld[4] * v.x() + camPosWorld[5] * v.y() + camPosWorld[6] * v.z() ,camPosWorld[8] * v.x() + camPosWorld[9] * v.y() + camPosWorld[10] * v.z())
    intersectionFront = getSceneIntersection(-1, rayOrigin, rayDirectionFront)
    
    interPosCollisionFront = intersectionFront[1]
    y = (interPosCollisionFront.x(), interPosCollisionFront.y(), interPosCollisionFront.z())
    collisionDistanceFront = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))

    #get the distance to back
    rayDirectionBack = Vec3f(1,0,0)
    intersectionBack = getSceneIntersection(-1, rayOrigin, rayDirectionBack)
    interPosCollisionBack = intersectionBack[1]
    y = (interPosCollisionBack.x(), interPosCollisionBack.y(), interPosCollisionBack.z())
    collisionDistanceBack = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))     

    rayDirectionLeft = Vec3f(0,1,0)
    intersectionLeft = getSceneIntersection(-1, rayOrigin, rayDirectionLeft)
    interPosCollisionLeft = intersectionLeft[1]
    y = (interPosCollisionLeft.x(), interPosCollisionLeft.y(), interPosCollisionLeft.z())
    collisionDistanceLeft = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))    

    rayDirectionRight = Vec3f(0,-1,0)
    intersectionRight = getSceneIntersection(-1, rayOrigin, rayDirectionRight)
    interPosCollisionRight = intersectionRight[1]
    y = (interPosCollisionRight.x(), interPosCollisionRight.y(), interPosCollisionRight.z())
    collisionDistanceRight = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))        
            
    print collisionDistanceFront
    

    interPosList = []
    for i in range(7):
        rayDirection = Vec3f(-(i-3)*0.1,0,-1)
        intersection = getSceneIntersection(-1, rayOrigin, rayDirection)
        interPos = intersection[1]
        bestInterPos =interPos.z()
        interPosList.insert(i,interPos.z())

    listCheckDuplicate = [x for x in interPosList if interPosList.count(x) > 1]
    if len(listCheckDuplicate) == 0:
        #print("the floor is not even")
        pass
    else:
        #print("the floor is  even")   
        bestInterPos =  mostFrequent(interPosList) 
        
    print mostFrequent(interPosList)
    '''
    cam.setTranslation(camPos[0],camPos[1],bestInterPos+1800)


def mostFrequent(List): 
    return max(set(List), key = List.count) 



def camRotFunc(rotDirection):
    global cam
    camRot = cam.getRotation()
    cam.setRotation(camRot[0],camRot[1],camRot[2]+rotDirection)
        
 
def printTime():
    dt = datetime.now()
    #print dt.second
    #print dt.microsecond
