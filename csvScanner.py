import csv


class csvScanner:

    def __init__(self):
        self.attributeNames = []
        self.attributes = []

    def createCsv(self, fileName, maxNumberOfLines):
        line = 0
        with open(fileName, newline='') as csvFile:
            csvReader = csv.reader(csvFile)
            self.attributeNames = next(csvReader)
            for row in csvReader:
                self.attributes = self.attributes + row
                if line == maxNumberOfLines:
                    break
                line = line + 1

    def printAttributeNames(self):
        for attributeName in self.attributeNames:
            print(attributeName)

    def printAttributes(self):
        for attribute in self.attributes:
            print(attribute)
