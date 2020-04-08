from exo1 import*

class BinaryTree:


    def __init__(self,root):
        self.__root=root

    def getROOT(self):
        return self.__root


arbre = BinaryTree(Node(12,None,None)) #creer le noeud de depart12
arbre.getROOT().setLeft(Node(5,None,None)) #ajoute noeud 5 a gauche
arbre.getROOT().getLeft().setLeft(Node(4,None,None))
arbre.getROOT().getLeft().setRight(Node(6,None,None))
arbre.getROOT().getLeft().getLeft().setLeft(Node(3,None,None))
arbre.getROOT().setRight(Node(17,None,None)) #ajoute noeud 17 a droite
arbre.getROOT().getRight().setRight(Node(19,None,None))
arbre.getROOT().getRight().getRight().setLeft(Node(18,None,None))
arbre.getROOT().getRight().getRight().setRight(Node(21,None,None))




