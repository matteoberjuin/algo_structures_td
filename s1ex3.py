

with open("frenchssaccent.dic",'r') as fichier:
    lexique = [ligne.strip() for ligne in fichier.readlines()]
        

        
points ={'a': 1, 'e': 1, 'i': 1, 'l': 1, 'n': 1, 'o': 1, 'r': 1, 's': 1, 't': 1, 'u': 1,
    'd': 2, 'g': 2, 'm': 2,
    'b': 3, 'c': 3, 'p': 3,
    'f': 4, 'h': 4, 'v': 4,
    'j': 8, 'q': 8,
    'k': 10, 'w': 10, 'x': 10, 'y': 10, 'z': 10}

def score(mot):
    somme=0
    for lettre in mot:
        somme = somme + points[lettre.lower()]
    return(somme)




tirage = ['a', 'r', 'b', 'g', 'e', 's', 'c', 'j']
n = len(tirage)
total = 0

for mot in lexique:

    k = len(mot)

    for lettre in mot:
        if lettre not in tirage:
            break
        break


    #à partir de cette ligne, on ne regarde que les mots dont toutes les lettres sont dans le tirage, il faut donc vérifier
    #qu'elles sont présentes dans les bonnes quantités

    tirage2 = tirage.copy()
    for lettre in mot:
        if lettre in tirage2:
            tirage2.remove(lettre)

    #à ce stade, si notre tirage2 est de longueur supérieure strice à n-k, cela veut dire qu'on a pas enlevé toutes les 
    #lettres présentes dans mot, donc que ce dernier contient une ou plusieurs lettres en trop grand nombre et donc que le mot
    #n'est pas valide

    if len(tirage2) <= n-k:
        if score(mot) > total:
            total = score(mot)
            mot_long = mot

print(mot_long, score(mot_long))
