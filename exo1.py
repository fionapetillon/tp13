class Node:

    def __init__(self,val,right,left):
        self.__val=val
        self.__right=right
        self.__left=left

    def getVal(self):
        return self.__val

    def getRight(self):
        return self.__right

    def getLeft(self):
        return self.__left

    def setRight(self,right):
        self.__right=right

    def setLeft(self,left):
        self.__left=left

    def __str__(self):
        return "La valeur du noeud est :"+str(self.__val)

o=Node(12,None,None)
print(o)


