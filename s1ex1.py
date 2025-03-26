lexique = [ 
            'sacrement',
           'aber', 'gare', 'sage', 'gars', 'rase', 'arec', 'acre', 'jars', 
           'case', 'base', 'cage', 'rage', 'jase', 'bras', 'race', 'ars', 
           'sac', 'arc', 'are', 'jar', 'jas', 'bar', 'bas', 'ace', 'cas', 
           'car', 'age', 'bac', 'cab', 'as', 'ra', 'sa', 'a', 'sacre']

tirage = ['a', 'r', 'b', 'g', 'e', 's', 'c', 'j']

n = len(tirage)
mot_long = ''

for mot in lexique:
    k = len(mot)
    for lettre in ( mot[0:k-1] ):
        if lettre not in tirage:
            continue
            
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
        if k > len(mot_long):
            mot_long = mot

print(mot_long)