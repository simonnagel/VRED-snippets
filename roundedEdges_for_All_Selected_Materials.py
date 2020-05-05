'''
DISCLAIMER:
---------------------------------
In any case, all binaries, configuration code, templates and snippets of this solution are of "work in progress" character.
This also applies to GitHub "Release" versions.
Neither Simon Nagel, nor Autodesk represents that these samples are reliable, accurate, complete, or otherwise valid. 
Accordingly, those configuration samples are provided “as is” with no warranty of any kind and you use the applications at your own risk.
'''

#All selected Materials will have a rounded edges radius that will be visible in RT
#Select Materials, adjust value of radius and execute Script
radius = 3

mats = getSelectedMaterials()

for i in range(0, len(mats)):
    mat = mats[i]
    container1 = vrFieldAccess(mat.fields().getFieldContainer("colorComponentData"))
    container2 = vrFieldAccess(container1.getFieldContainer("roundedEdgeSettings"))
    #container3 = vrFieldAccess(container2.getFieldContainer("planarProjection"))   
    #container3.setVec3f("translation",pos[0],pos[1],pos[2])    
    container2.setUInt32("mode",2)  
    container2.setReal32("radius",radius )  
    
updateMaterials()