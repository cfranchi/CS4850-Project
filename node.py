class node:

    def __init__(self, name, attributeType, number):
        self.name = name
        self.attributeType = attributeType
        self.children = []
        self.childNames = []
        self.number = number
        self.parent = None

    def addChildNode(self, node):
        self.children.append(node)
        self.childNames.append(node.name)

    def setParentNode(self, node):
        self.parent = node
