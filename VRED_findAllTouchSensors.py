'''
DISCLAIMER:
---------------------------------
In any case, all binaries, configuration code, templates and snippets of this solution are of "work in progress" character.
This also applies to GitHub "Release" versions.
Neither Simon Nagel, nor Autodesk represents that these samples are reliable, accurate, complete, or otherwise valid. 
Accordingly, those configuration samples are provided “as is” with no warranty of any kind and you use the applications at your own risk.
'''

#get all Nodes in the Scenegraph
allNodes = getAllNodes()

#create an empty list and delete it (in case you use the scripts more than once)
allNodesList = []
del allNodesList[:]

#check for every node, if there is an attachment called "TouchSensorAttachment"
for i in range(0,len(allNodes)):
    node = allNodes[i]
    if node.hasAttachment("TouchSensorAttachment") == 1:
        allNodesList.append(node)


# here all the nodes with a touchsensor are selected.
selectNodes(allNodesList)
