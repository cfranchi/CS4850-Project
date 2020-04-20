class node:

    def __init__(self, name, attributeType, number):
        self.name = name
        self.attributeType = attributeType
        self.children = []
        self.childNames = []
        self.number = number
        self.parent = None

    def addChildNode(self, childNode):
        self.children.append(childNode)
        self.childNames.append(childNode.name)

    def setParentNode(self, parentNode):
        self.parent = parentNode

