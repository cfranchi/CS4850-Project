class initialNode:

    def __init__(self, keywords, attributeType, name):
        self.keywords = {}
        self.attributeType = attributeType
        self.name = name
        for word in keywords:
            self.keywords.update({word: keywords[word]})
