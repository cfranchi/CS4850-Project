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
                self.attributes.append(row)
                if line == maxNumberOfLines:
                    break
                line += 1

    def printAttributeNames(self):
        print("ATTRIBUTE NAMES:\n")
        i = 0
        for attributeName in self.attributeNames:
            print(i.__str__() + " - " + attributeName)
            i += 1
        print("-----------------------------------------------------------------------------")

    def printAttributes(self):
        for attribute in self.attributes:
            print(attribute)
