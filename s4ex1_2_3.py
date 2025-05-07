import matplotlib.pyplot as plt
from time import perf_counter

class Hashtable:

    def __init__(self, size = 10, fonction = None):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.items = 0
        self.fonction = fonction if fonction else self.__naive_fct__

    def __naive_fct__(self, key):
        return sum(ord(c) for c in key)
    
    def __put__(self, key, value):
        index = self.fonction(key) % self.size
        self.table[index].append((key,value))
        self.items += 1
        if self.items >= 1.2*self.size:
            self.__resize__()
    
    def __get__(self,key):
        index = self.fonction(key) % self.size
        if self.table[index] is None:
            return None
        else:
            for couple in self.table[index]:
                if couple[0] == key:
                    return couple[1]
        
    def __repartition__(self):
        y = []
        for collisions in self.table:
            y.append(len(collisions))
        N = len(y)
        x = range(N)
        width = 1/1.5
        plt.bar(x, y, width, color="blue")
        plt.show()

    def __resize__(self):
        new_size = 2*self.size
        new_table = [[] for _ in range (new_size)]

        for bucket in self.table:
            for (key,value) in bucket:
                index = self.fonction(key) % new_size
                new_table[index].append((key,value))

        self.size = new_size
        self.table = new_table

    

try:
    with open('/Users/marwanesersouri/Documents/cours info S6/séance TD 4/frenchssaccent.dic','r') as fichier:
        lexique = [ligne.strip() for ligne in fichier.readlines()]
except FileNotFoundError:
    print("Le fichier n'a pas été trouvé")
    lexique = []


#exercice 5 : création d'une table de hashage à partir de frenchssaccent et visualisation du nombre de collisions en utilisant
#la fonction de hashage naive
#map = Hashtable(10000,None)

#for mot in lexique:
 #  map.__put__(mot,map.fonction(mot))

#map.__repartition__()

#on fait la même chose mais en utilisant la fonction de hachage de Jenkins

def jenkins_hash(key):
    hash_value = 0
    for char in key:
        hash_value += ord(char)                 #on calcule hash_v = hash_v + ord(char)
        hash_value += (hash_value << 10)        # on ajoute à hash_v hash_v mais décalé de 10 bits vers la droite (on multiplie par 2^10)
        hash_value ^= (hash_value>>6)           # on ajoute à hash_v ""             ""     6 bits vers la gauche

    # Final mixing
    hash_value += (hash_value << 3)
    hash_value ^= (hash_value >> 11)
    hash_value += (hash_value << 15)
    
    return hash_value

map = Hashtable(50000, jenkins_hash)
for mot in lexique:
   map.__put__(mot,map.fonction(mot))


#exercice 7 : vérification du temps des opérations put et get

t1_start = perf_counter()

map.__get__("aboutir")

t1_end = perf_counter()

print (t1_end - t1_start)  #on trouve quelque chose de l'odre de 10^-6

L = [2,3,4]
t1_start = perf_counter()

L[0]

t1_end = perf_counter()
print (t1_end - t1_start)

#le temps d'insertion et de recherche se fait en temps constant avec une table de hachage.
#récupérer un élément dans une liste se fait en environ 10^-6 secondes (qui lui
# est en temps constant) tandis que ces opérations dans une table de hachage se fait en 
# (environ) 8*10^-5 secondes.
