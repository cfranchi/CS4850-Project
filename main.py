from csvScanner import csvScanner


def main():
    scanner = csvScanner()
    scanner.createCsv('/Users/cameron/Downloads/Call_Data_2019 (1).csv', 100)
    scanner.printAttributeNames()
    print('-----------------------------------------------------------------------------')
    scanner.printAttributes()
    print('exit')


main()
