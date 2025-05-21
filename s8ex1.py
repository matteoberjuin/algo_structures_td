import struct
import numpy as np

def extraire_samples_wav(audio):
    with open(audio,'rb') as fichier:

        
        fichier.seek(40)
        taille_donnees = struct.unpack('I', fichier.read(4))[0]
        
        echantillons = []
        
        fichier.seek(44)
        donnees = fichier.read(taille_donnees)
        
        for i in range(0, taille_donnees, 4):
            canal_gauche,canal_droit = struct.unpack('hh', donnees[i:i+4])
            echantillons.append((canal_gauche,canal_droit))
        
        return echantillons
    

print(len(extraire_samples_wav("O:/s6python/the_wall.wav")))


def verif(audio,echantillons):
    with open(audio,'rb') as fichier:
        
        
        taille_data=len(echantillons)*4
        taille_fichier=taille_data+44
        

        header = bytearray(fichier.read(44))  # rendre modifiable

    
        header[4:8] = struct.pack('<I', taille_fichier - 8)
        header[40:44] = struct.pack('<I', taille_data)

        copie = "O:/s6python/the_wall_copy.wav"  
        
        with open(copie, 'wb') as fichier_new:
            fichier_new.write(header)
            for gauche, droite in echantillons:
                fichier_new.write(struct.pack('hh', gauche, droite))
    
    return(fichier, fichier_new)


    
    
    
    
    
    
    

