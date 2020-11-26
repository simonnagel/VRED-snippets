## This script will make your Background in the opposite color of your scene

## Create a Sphere called "BG" and apply a Material call "BG"
## Change its diffuse and glossy color to black

# Create a switch material an apply to your main object. call it "Carpaint Switch"
#of course you can change names in the switch

timer = vrTimer()

switchmat = findMaterial("Carpaint Switch")
bgMat = findMaterial("BG")

def matchBGColorToPaint():
    global switchmat
    global bgMat
    
    choice = switchmat.fields().getUInt32("choice")
    mat = switchmat.getMaterialByChoice(choice)
    color =  mat.fields().getVec("baseColor",3)
    #print color
    bgMat.fields().setVec("incandescenceColor",(colorCalc(color[0]),colorCalc(color[1]),colorCalc(color[2]),1))

def colorCalc(color):
    factor = 1

    newColor = abs(color-1)
    #print newColor

    if newColor<0.2:
        newColor = 0.2
    elif newColor>0.8:
        newColor = 0.8
    '''
    newColor = color/factor
    if newColor<0.025:
        newColor = 0.025
    elif newColor>0.975:
        newColor = 0.975
    '''
    return newColor

timer.connect(matchBGColorToPaint) 
timer.setActive(1)
