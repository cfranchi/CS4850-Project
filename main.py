from TreeBuilder.treeBuilder import treeBuilder
from treeAnalyzer import treeAnalyzer


#   So far, this program can read in a CSV file and sort it into a customizable tree structure.
#   For example, we can sort by precinct, sector, beat, priority, and finally call type, or we can
#   swap call type and priority to visualize alternative groupings of data.
#   The hierarchy list is used to rearrange the order in which data is sorted.
#   Each attribute type is numbered by the order in which it was scanned from the CSV file.
#   The printAttributeNames function will show an ordered list of each attribute.
#   Attribute 0 is CAD Event Number and should probably be left at the end of the hierarchy for any given sort.
#   the integer parameter in the createCsv function is the amount of data the scanner will read in.

def main():
    hierarchy = [8, 9, 10, 5, 0]
    keywords = {
        "ASSAULT": 0,
        "FIRE": 0,
        "ROBBERY": 0,
    }
    fileLocation = '/Users/cameron/Downloads/Call_Data_2019 (1).csv'
    dataSetSize = 100000
    builder = treeBuilder(hierarchy, fileLocation, dataSetSize)
    builder.build()
    analyzer = treeAnalyzer(hierarchy, builder.tree, keywords)
    analyzer.traverse(builder.tree.rootNode, 9, hierarchy[len(hierarchy) - 1])
    print("exit")


main()
