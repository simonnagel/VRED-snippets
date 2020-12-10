# Script to Select Parent, Child or sbilings

# use this scipr in VR to select Nodes in your Hierachy

# CAUTION: Keys A S D W are used here. Might cause conflict with other scripts.


def selectButtonUp():
    selectParent()

def selectButtonDown():
    child = getSelectedNode().getChild(0)
    selectNode(child)
    
def selectButtonLeft():
    currentNode = getSelectedNode()
    currentNodename = currentNode.getName()
    parent = currentNode.getParent()
    
    
    for i in range(parent.getNChildren()):
        newNodeName = parent.getChild(i).getName()
        if newNodeName == currentNodename:            
            selectNode(parent.getChild(i-1))
            break

def selectButtonRight():
    currentNode = getSelectedNode()
    currentNodename = currentNode.getName()
    parent = currentNode.getParent()
    
    
    for i in range(parent.getNChildren()):
        newNodeName = parent.getChild(i).getName()
        if newNodeName == currentNodename:            
            selectNode(parent.getChild(i+1))
            break    



keyW = vrKey(Key_W)
keyW.connect(selectButtonUp)

keyS = vrKey(Key_S)
keyS.connect(selectButtonDown)

keyA = vrKey(Key_A)
keyA.connect(selectButtonLeft)

keyD = vrKey(Key_D)
keyD.connect(selectButtonRight)
