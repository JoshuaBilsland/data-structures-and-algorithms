class TreeNode:
    def __init__(self, data):
        self.__data = data
        self.__childNodes = []
    
    
    def getData(self):
        return self.__data
    
    
    def getChildNodes(self):
        return self.__childNodes
    
    
    def addChildNode(self, childData):
        self.__childNodes.append(TreeNode(childData))