class csvParser:

    def __init__(self, hierarchy, scanner):
        self.hierarchy = hierarchy
        self.attributes = scanner.attributes
        self.attributeNames = scanner.attributeNames

    def sortToHierarchy(self):
        print("sorting by hierarchy...")
        for i in range(0, len(self.attributes)):
            count = 0
            temp = self.attributes[i][:]
            self.attributes[i] = self.attributes[i][: len(self.hierarchy)]
            for j in self.hierarchy:
                for k in range(count, len(self.attributes[i])):
                    self.attributes[i][k] = temp[j]
                    count += 1
                    break
        print("sorting compete")
        print("-----------------------------------------------------------------------------")

    def printHierarchy(self):
        print("HIERARCHY:\n")
        for rank in self.hierarchy:
            print(rank.__str__() + " - " + self.attributeNames[rank].__str__())
        print("-----------------------------------------------------------------------------")

    def parse(self, tree):
        print("parsing...")
        for i in range(0, len(self.attributes)):
            for j in range(0, len(self.hierarchy)):
                tree.addNode(self.attributes[i][j], self.hierarchy[j])
            tree.updateParentNode(tree.rootNode)
        print("parse complete")
        print("-----------------------------------------------------------------------------")
