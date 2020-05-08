from exo1 import*

class BinaryTree:


    def __init__(self,root):
        self.__root=root

    def getROOT(self):
        return self.__root

    def isRoot(self, node):
        if node == self.__root : #si le noeud racine = node alors oui c le noeud racine
            return True
        else :
            return False


    def size(self, node):
        if node is None:
            return 0
        else:
            return self.size(node.getLeft()) + 1 + self.size(node.getRight())

    def printValues(self, node):
        if node is None:
            return ""
        else:
            return self.printValues(node.getLeft()) + self.printValues(node.getRight()) + " " + str(node.getVal())

    def sumValues(self,node):
        if node is None:
            return 0
        else:
             return self.sumValues(node.getLeft())+ node.getVal() + self.sumValues(node.getRight())

    def numberLeaves(self,node):
        if node is None:
            return 0
        elif node.getLeft()==None and node.getRight()==None:
            return 1
        else :
            return self.numberLeaves(node.getLeft())+self.numberLeaves(node.getRight())

    def numberInternalNodes(self,node):
        if node is None:
            return 0
        elif node.getLeft()==None and node.getRight()==None:
            return 0
        else:
            return self.numberInternalNodes(node.getLeft())+ 1 +self.numberInternalNodes(node.getRight())


    def height(self,node):
        if node is None:
            return 0
        else:
            return 1 + max(str(self.height(node.getLeft())) + str(self.height(node.getRight())))

    def belongs(self,node,val):
        if node is None:
            return False
        elif node.getVal()==val:
            return True
        else:
            return  self.belongs(node.getLeft(),val) or self.belongs(node.getRight(),val)








arbre = BinaryTree(Node(12,None,None)) #creer le noeud de depart12
arbre.getROOT().setLeft(Node(5,None,None)) #ajoute noeud 5 a gauche
arbre.getROOT().getLeft().setLeft(Node(4,None,None))
arbre.getROOT().getLeft().setRight(Node(6,None,None))
arbre.getROOT().getLeft().getLeft().setLeft(Node(3,None,None))
arbre.getROOT().setRight(Node(17,None,None)) #ajoute noeud 17 a droite
arbre.getROOT().getRight().setRight(Node(19,None,None))
arbre.getROOT().getRight().getRight().setLeft(Node(18,None,None))
arbre.getROOT().getRight().getRight().setRight(Node(21,None,None))

print(arbre.size(arbre.getROOT()))
print(arbre.height(arbre.getROOT()))
print(arbre.sumValues(arbre.getROOT()))
print(arbre.numberLeaves(arbre.getROOT()))
print(arbre.numberInternalNodes(arbre.getROOT()))
print(arbre.height(arbre.getROOT()))





