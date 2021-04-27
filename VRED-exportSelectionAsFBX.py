def exportSelectionAsFBX():
    name = getSelectedNode().getName()
    filepath = ("c:/temp/")
    saveSelectedGeometry(filepath+name+".fbx",0)
    
    
keyQc = vrKey(Key_Q, ControlButton)
keyQc.connect("exportSelectionAsFBX()")
