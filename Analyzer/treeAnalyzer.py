from Analyzer.initialNode import initialNode

class treeAnalyzer:

    def __init__(self, hierarchy, tree, keywords):
        self.hierarchy = hierarchy
        self.tree = tree
        self.keywords = keywords
        self.keywordTotals = keywords.copy()
        self.initialNodes = []

    def start(self, currentNode, initialNodeAttributeType, terminalNodeAttributeType):
        print("analyzing data...")
        self.traverse(currentNode, initialNodeAttributeType, terminalNodeAttributeType)
        print("analysis compete")
        print("-----------------------------------------------------------------------------")

    def traverse(self, currentNode, initialNodeAttributeType, terminalNodeAttributeType):
        for i in range(0, len(currentNode.children)):
            if currentNode.children[i].attributeType == initialNodeAttributeType:
                initNode = initialNode(self.keywords, initialNodeAttributeType, currentNode.children[i].name)
                self.initialNodes.append(initNode)
                self.traverse(currentNode.children[i], initialNodeAttributeType, terminalNodeAttributeType)
            elif currentNode.children[i].attributeType == terminalNodeAttributeType:
                self.linkNodeToKeyWord(currentNode, self.initialNodes[len(self.initialNodes) - 1])
                break;
            else:
                self.traverse(currentNode.children[i], initialNodeAttributeType, terminalNodeAttributeType)

    def linkNodeToKeyWord(self, node, initialNode):
        for word in self.keywords:
            if word in node.name:
                tempNodeValue = initialNode.keywords[word]
                tempTotalsValue = self.keywordTotals[word]
                for i in range(0, len(node.children)):
                    tempNodeValue = tempNodeValue + 1
                    initialNode.keywords[word] = tempNodeValue
                    tempTotalsValue = tempTotalsValue + 1
                    self.keywordTotals[word] = tempTotalsValue


    def printData(self):
        for node in self.initialNodes:
            print(node.name + ":")
            for word in node.keywords:
                print("\t" + word + "- " + str(node.keywords[word]))
            print()
        print("TOTALS:")
        for word in self.keywordTotals:
            print("\t" + word + "- " + str(self.keywordTotals[word]))
