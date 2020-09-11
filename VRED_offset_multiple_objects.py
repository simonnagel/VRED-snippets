offset = 400.0
nodes = getSelectedNodes()

for i in range(len(nodes)): 
    nodes[i].setTranslation(i*offset,0,0)
