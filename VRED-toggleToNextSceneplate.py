### functions to click pgdw and pgup to toggle to next Sceneplate Switch child

textSwitch = vrSceneplateService.findNode("TextSwitch")
textChoice = 0
textSwitch.setChoice(textChoice)

def nextText():
    global textChoice
    global textSwitch
    textChoice +=1
    if textChoice < textSwitch.getChildCount():        
        textSwitch.setChoice(textChoice)
    else:
        textChoice = 0
        textSwitch.setChoice(textChoice)
    #print(textChoice)
    
    
def previousText():
    global textChoice
    global textSwitch
    textChoice -=1
    if textChoice < 0: 
        textChoice = textSwitch.getChildCount()-1       
        textSwitch.setChoice(textChoice)
    else:
        
        textSwitch.setChoice(textChoice)
    #print(textChoice)    
    
    
keyNextText = vrKey(16777239)
keyNextText.connect(nextText)    

keyPreviewText = vrKey(16777238)
keyPreviewText.connect(previousText) 
