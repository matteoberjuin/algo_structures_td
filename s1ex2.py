try:
    with open("frenchssaccent.dic",'r') as fichier:
        lexique = [ligne.strip() for ligne in fichier.readlines()]
except FileNotFoundError:
    print("Le fichier n'a pas été trouvé")
    lexique = []

tirage = ['a', 'r', 'b', 'g', 'e', 's', 'c', 'j']

n = len(tirage)
mot_long = ''

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
        if k > len(mot_long):
            mot_long = mot

print(mot_long)

