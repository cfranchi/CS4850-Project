from csvScanner import csvScanner
from csvTree import csvTree
from csvParser import csvParser


#   So far, this program can read in a CSV file and sort it into a customizable tree structure.
#   For example, we can sort by precinct, sector, beat, priority, and finally call type, or swap call type and
#   priority to visualize alternative groupings of data.
#   The hierarchy list is used to rearrange the order in which data is sorted.
#   Each attribute type is numbered by the order in which it was scanned from the CSV file.
#   The printAttributeNames function will show an ordered list of each attribute.
#   Attribute 0 is CAD Event Number and should probably be left at the end of the hierarchy for any given sort.
#   the integer parameter in the createCsv function is the amount of data the scanner will read in.

def main():
    hierarchy = [8, 9, 10, 3, 5, 0]
    scanner = csvScanner()
    scanner.createCsv('/Users/cameron/Downloads/Call_Data_2019 (1).csv', 100000)
    scanner.printAttributeNames()
    tree = csvTree(hierarchy, scanner)
    parser = csvParser(hierarchy, scanner)
    parser.sortToHierarchy()
    parser.printHierarchy()
    parser.parse(tree)
    tree.printTree(tree.rootNode)
    print("exit")


main()
