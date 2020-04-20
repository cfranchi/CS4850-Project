from .csvScanner import csvScanner
from .csvParser import csvParser
from .csvTree import csvTree


class treeBuilder:

    def __init__(self, hierarchy, csvFile, dataSetSize):
        self.hierarchy = hierarchy
        self.csvFile = csvFile
        self.dataSetSize = dataSetSize
        self.tree = None

    def build(self):
        scanner = csvScanner()
        scanner.createCsv(self.csvFile, self.dataSetSize)
        scanner.printAttributeNames()
        self.tree = csvTree(self.hierarchy, scanner)
        parser = csvParser(self.hierarchy, scanner)
        parser.sortToHierarchy()
        parser.printHierarchy()
        parser.parse(self.tree)
        #self.tree.printTree(self.tree.rootNode)
