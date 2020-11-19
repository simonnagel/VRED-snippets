#press W,A,S,D to move camera
#press Q and E to rotate
#use mouse for change view

# know bugs
# cannot press Q,E at the same time as W,A,S,D
# if pressed W too long and going "upwards" camera goes back on ground

import math
import time
from datetime import datetime


class RenderAction(vrInteraction):
    def __init__(self):
        vrInteraction.__init__(self)
        self.addRender()
    def preRender(self):               
        

        
        isKeyPressed()
        

render = RenderAction()
setNavigationSpeedMode(0)
import keyboard
from math import sqrt
cam = getActiveCameraNode()
speed = 0.1


def isKeyPressed():
    global cam
    global speed
    setNavigationSpeedMode(2)
    x = 0
    y = 0
    speedForward = speed
    speedSideward = speedForward*2000
    setPanningSpeed(1)
    setDollySpeed(1)
    active = 0   
    
    camPos = cam.getTranslation()
    camPosWorld = cam.getWorldTransform()

    #get the distance to ground
    rayOrigin = Pnt3f(camPos[0],camPos[1],camPos[2])
    rayDirection = Vec3f(0,0,-1)
    intersection = getSceneIntersection(-1, rayOrigin, rayDirection)
    interPos = intersection[1]
    bestInterPos = interPos.z() 
    collisionDistanceF = calcCollisionDistance(rayOrigin,camPos,camPosWorld,0,0,-1)
    collisionDistanceR = calcCollisionDistance(rayOrigin,camPos,camPosWorld,1,0,0)
    collisionDistanceL = calcCollisionDistance(rayOrigin,camPos,camPosWorld,-1,0,0)
    #print collisionDistanceL
    cam.setTranslation(camPos[0],camPos[1],bestInterPos+1800)   
            
    if keyboard.is_pressed('q'):
        camRotFunc(5)
        active = 0
    if keyboard.is_pressed('e'):
        camRotFunc(-5)
        active = 0     
    if keyboard.is_pressed('w'):
        if collisionDistanceF > 500:
            setCameraZoom(-speedForward)
            y = 1
            active = 1
    if keyboard.is_pressed('s'):

        setCameraZoom(speedForward)
        y = -1
        active = 1
    if keyboard.is_pressed('a'):
        if collisionDistanceL > 500:
            setCameraPanning(speedSideward, 0)
            x = 1
            active = 1
    if keyboard.is_pressed('d'):
        if collisionDistanceR > 500:
            setCameraPanning(-speedSideward, 0)
            x =-1
            active = 1
    if keyboard.is_pressed('x'):  
        setCameraZoom(-10)  
        
    if keyboard.is_pressed('m'):
        adjustSpeed(1)
    if keyboard.is_pressed('n'):
        adjustSpeed(-1)            
               
    if active == 1:
        setNavMode(3)
        setAllNavigationsEnabled(0)
        
    else:
        setNavMode(4)
        setAllNavigationsEnabled(1)


def adjustSpeed(factor):
    global speed
    
    speed = speed + 0.01* factor
    if speed <0:
        speed = 0
    #print speed


def getRayAverage():

  '''
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

def calcCollisionDistance(rayOriginF,camPos,camPosWorld,vx,vy,vz):

    x = (camPos[0], camPos[1], camPos[2])  
      
    #get the distance to front
    v = Vec3f(vx,vy,vz)
    rayDirectionF = Vec3f(camPosWorld[0] * v.x() + camPosWorld[1] * v.y() + camPosWorld[2] * v.z() , camPosWorld[4] * v.x() + camPosWorld[5] * v.y() + camPosWorld[6] * v.z() ,camPosWorld[8] * v.x() + camPosWorld[9] * v.y() + camPosWorld[10] * v.z())
    intersectionF = getSceneIntersection(-1, rayOriginF, rayDirectionF)
    
    interPosCollisionF = intersectionF[1]
    y = (interPosCollisionF.x(), interPosCollisionF.y(), interPosCollisionF.z())
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
    

    

def mostFrequent(List): 
    return max(set(List), key = List.count) 



def camRotFunc(rotDirection):
    global cam
    camRot = cam.getRotation()
    cam.setRotation(camRot[0],camRot[1],camRot[2]+rotDirection)
        
 
