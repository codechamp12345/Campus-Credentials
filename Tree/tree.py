class Tree:
    def __init__(self,data):
        self.nodeValue = data
        self.treeList = []

    def __str__(self,level=0):
        ret = " "* level + str(self.nodeValue) + "\n"
        for child in self.treeList:
            ret += child.__str__(level+1)
        return ret

    def addChildNode(self,value):
        self.treeList.append(value)
    

rootNode = Tree('Drinks') #constructor
Hot = Tree('Cold')
Cold = Tree('Hot')
Tea = Tree("Tea")
Cofee = Tree("Cofee")
Alcoholic = Tree("Alcoholic")
NonAlcoholic = Tree("Non Alcoholic")

rootNode.addChildNode(Hot)
rootNode.addChildNode(Cold)
Hot.addChildNode(Tea)
Hot.addChildNode(Cofee)
Cold.addChildNode(NonAlcoholic)
Cold.addChildNode(Alcoholic)

print(rootNode)
print(Hot)
print(Cold)


