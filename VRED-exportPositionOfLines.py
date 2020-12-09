group = findNode("D_Lines")
filepath = "c:/temp/"
filename = "Line_Positions.txt"

newText = []

for i in range(group.getNChildren()):
    
    name =  group.getChild(i).getName()
    positions =  group.getChild(i).getPositions()
    print "\n"    
    newText.append(name)
    newText.append(positions)
    
    joinedScript = ''.join(str(newText))
    
fi = open(filepath+filename, 'wt')
fi.writelines(joinedScript)
fi.close()
