from initialNode import initialNode

class treeAnalyzer:

    def __init__(self, hierarchy, tree, keywords):
        self.hierarchy = hierarchy
        self.tree = tree
        self.keywords = keywords
        self.initialNodes = []

    def traverse(self, currentNode, initialNodeAttributeType, terminalNodeAttributeType):
        for i in range(0, len(currentNode.children)):
            if currentNode.children[i].attributeType == initialNodeAttributeType:
                initNode = initialNode(self.keywords, initialNodeAttributeType, currentNode.children[i].name)
                self.initialNodes.append(initNode)
                self.traverse(currentNode.children[i], initialNodeAttributeType, terminalNodeAttributeType)
            elif currentNode.children[i].attributeType == terminalNodeAttributeType:
                self.linkNodeToKeyWord(currentNode, self.initialNodes[len(self.initialNodes) - 1])
            else:
                self.traverse(currentNode.children[i], initialNodeAttributeType, terminalNodeAttributeType)


#    def traverse(self, currentNode, initialNodeAttributeType, terminalNodeAttributeType):
#        for i in range(0, len(currentNode.children)):
#            if currentNode.children[i].attributeType != terminalNodeAttributeType:
#                self.traverse(currentNode.children[i], initialNodeAttributeType, terminalNodeAttributeType)
#            if currentNode.children[i].attributeType == terminalNodeAttributeType:
#                self.linkNodeToKeyWord(currentNode)

    def linkNodeToKeyWord(self, node, initialNode):
        for word in self.keywords:
            if word in node.name:
                initialNode.keywords[word] = self.keywords[word] + 1
