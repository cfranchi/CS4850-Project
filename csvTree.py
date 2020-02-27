from node import node


class csvTree:

    def __init__(self, hierarchy, scanner):
        self.nodeCount = 0
        self.rootNode = node('root', -1, self.nodeCount)
        self.nodes = [self.rootNode]
        self.parentNode = self.rootNode
        self.hierarchy = hierarchy
        self.scanner = scanner
        self.attributeCount = 0

    def addNode(self, name, attributeType):
        flag = True
        for child in self.parentNode.children:
            if child.name == name:
                self.parentNode = child
                flag = False
                break
        if flag:
            self.nodeCount += 1
            newNode = node(name, attributeType, self.nodeCount)
            newNode.setParentNode(self.parentNode)
            self.parentNode.addChildNode(newNode)
            self.nodes.append(newNode)
            self.parentNode = newNode

    def updateParentNode(self, node):
        self.parentNode = node

    def printTree(self, parentNode):
        print(parentNode.name)
        print("-----------------------------------------------------------------")
        print("ATTRIBUTE: " + self.scanner.attributeNames[self.hierarchy[self.attributeCount]] + "\n")
        self.attributeCount += 1
        for child in parentNode.children:
            print(child.name)
        print("-----------------------------------------------------------------")
        print("enter child name:")
        nextNode = input()
        for child in parentNode.children:
            if nextNode == child.name:
                self.printTree(child)
                break
