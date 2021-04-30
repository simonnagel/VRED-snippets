QColor = PySide2.QtGui.QColor

class RenderAction(vrAEBase):
    def __init__(self):
        vrAEBase.__init__(self)
        self.addLoop()
    def loop(self):
        changeUserLook()
render = RenderAction()

simon = findNode("Simon")
danny = vrNodeService.findNode("Danny")
dan = vrNodeService.findNode("Dan")
robin = vrNodeService.findNode("Robin")

simonMat = findMaterial("Color_Simon")
dannyMat = findMaterial("Color_Danny")
danMat = findMaterial("Color_Dan")
robinMat = findMaterial("Color_Robin")



def changeUserLook():
    global simon
    global danny
    global dan
    global robin
    users = vrSessionService.getUsers()
       
    for u in range(len(users)):
        user = users[u]
        headNode = user.getHeadNode()


        user.setAvatarVisible(0)
        if user.getUserName() == "Simon":
            pos = getTransformNodeTranslation(user.getHeadNode(),True)
            rot = getTransformNodeRotation(user.getHeadNode())
            setTransformNodeTranslation(simon,pos.x(),pos.y(),pos.z(),1)
            setTransformNodeRotation(simon,rot.x(),rot.y(),rot.z())
            userColor = vrdSessionUser.getUserColor(user)
            simonMat.fields().setVec3f("diffuseColor",userColor.redF(), userColor.greenF(), userColor.blueF())
            
         
        elif user.getUserName() == "Danny":
            pos = getTransformNodeTranslation(user.getHeadNode(),True)
            rot = getTransformNodeRotation(user.getHeadNode())
            setTransformNodeTranslation(danny,pos.x(),pos.y(),pos.z(),1)
            setTransformNodeRotation(danny,rot.x(),rot.y(),rot.z())
            userColor = vrdSessionUser.getUserColor(user)
            dannyMat.fields().setVec3f("diffuseColor",userColor.redF(), userColor.greenF(), userColor.blueF())
            
        elif user.getUserName() == "Robin":
            pos = getTransformNodeTranslation(user.getHeadNode(),True)
            rot = getTransformNodeRotation(user.getHeadNode())
            setTransformNodeTranslation(robin,pos.x(),pos.y(),pos.z(),1)
            setTransformNodeRotation(robin,rot.x(),rot.y(),rot.z())
            userColor = vrdSessionUser.getUserColor(user)
            robinMat.fields().setVec3f("diffuseColor",userColor.redF(), userColor.greenF(), userColor.blueF())
            
        elif user.getUserName() == "Dan":
            pos = getTransformNodeTranslation(user.getHeadNode(),True)
            rot = getTransformNodeRotation(user.getHeadNode())
            setTransformNodeTranslation(dan,pos.x(),pos.y(),pos.z(),1)
            setTransformNodeRotation(dan,rot.x(),rot.y(),rot.z())
            userColor = vrdSessionUser.getUserColor(user)
            danMat.fields().setVec3f("diffuseColor",userColor.redF(), userColor.greenF(), userColor.blueF())
            
