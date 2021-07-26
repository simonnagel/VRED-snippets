
'''
DISCLAIMER:
---------------------------------
In any case, all binaries, configuration code, templates and snippets of this solution are of "work in progress" character.
This also applies to GitHub "Release" versions.
Neither Simon Nagel, nor Autodesk represents that these samples are reliable, accurate, complete, or otherwise valid. 
Accordingly, those configuration samples are provided ?as is? with no warranty of any kind and you use the applications at your own risk.
Scripted by Simon Nagel

How to use:

Select all NOdes that should move over time.

Unshare Subtree
Flush Transformation

Execute Script

Scroll through timeline.

'''

nodes = getSelectedNodes()
print(nodes)

BBCenterList = []

def setPositionToPivot():
    for i in range(len(nodes)):  
        flushTransformations(nodes[i]) 
        #pivot = getTransformNodeRotatePivot(nodes[i],1)  
        BBCenter = getBoundingBoxCenter(nodes[i],1)
        BBCenterList.append(BBCenter)
        setTransformNodeTranslation(nodes[i],-BBCenter.x(),-BBCenter.y(),-BBCenter.z(),1)
        flushTransformations(nodes[i])
        setTransformNodeTranslation(nodes[i],BBCenter.x(),BBCenter.y(),BBCenter.z(),1)    

setPositionToPivot()

arrayoftime=[0,0]

def animation():
    time = getCurrentFrame()/100
    arrayoftime.append(time)
    #print arrayoftime
    if len(arrayoftime)>0:
        if arrayoftime[0]!=arrayoftime[1]:
            #print("there is a new frame")
            #print(time)

            for i in range(len(nodes)):           
                
                setTransformNodeTranslation(nodes[i],BBCenterList[i].x()*time,BBCenterList[i].y()*time,BBCenterList[i].z()*time,1)
                
        
        
    arrayoftime.pop(1)
    
    
timer = vrTimer()

timer.connect(animation)

timer.setActive(1)

#animation()


