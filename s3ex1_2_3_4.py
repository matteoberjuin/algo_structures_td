class Tree:

    def __init__(self, label:'str', *children:'Tree'):
        self.label = label
        self.children = children

    def __label__(self):
        return self.label
    
    def __children__(self):
        return self.children
    
    def __nb_children__(self):
        return len( self.children )

    def __childk__(self,k):
        return self.children[k]

    def __isleaf__(self):
        if len(self.children) == 0:
            return True
        else: 
            return False
        
        
        
    def __str__(self)   :
        if self.__isleaf__():
            return str(self.label)
        return self.__label__() + '(' + ','.join(str(child) for child in self.__children__())  + ')' 
    
    
    
    
  
    def __eq__(self, other):
        if self.__nb_children__() != other.__nb_children__():
            return False
        if self.__label__() != other.__label__():
            return False
        else :
            for i in range(len(self.__children__())):
                if self.children[i] != other.children[i]:
                    return False
        return True
  
    
  
    
    def __depth__(self):
        if self.__isleaf__():
            return 0
        else :
            return 1 + max(child.__depth__() for child in self.children)
    
    
feuille = Tree('x')
feuille2 = Tree('y')
arbre_simple = Tree('a', Tree('x'), Tree('y'))
arbre2 = Tree('a', Tree('x'), Tree('y', Tree('b'), Tree('z')))


# Test des accesseurs
assert feuille.__label__() == 'x'
assert feuille.__isleaf__() == True
assert feuille.__nb_children__() == 0
assert arbre_simple.__nb_children__() == 2
assert arbre_simple.__childk__(0).__label__() == 'x'
print(arbre_simple.__children__())
print(arbre2.__depth__(),arbre_simple.__depth__())
print(str(arbre2))
print(arbre2.__eq__(arbre_simple))
print(feuille == feuille2)