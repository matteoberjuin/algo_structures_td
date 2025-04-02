class Polynomial: 

    def __init__(self,liste_coeff):
        self.liste_coeff = liste_coeff


    def __str__(self):
       
        polynome = str(self.liste_coeff[0])
        k = 0

        for coef in self.liste_coeff[1:]:
            k += 1
            if coef == 0:
                continue
          
            elif coef > 0:
                polynome = polynome + '+' + str(coef) + '*X^' + str(k)
            else:
                polynome = polynome + '-' + str(coef) + '*X^' + str(k)
        return polynome
    

    def add(self, other):
        n = len(self.liste_coeff)
        k = len(other.liste_coeff)
        
        liste = [0] * max(n,k)

        if n == k:
            for i in range(n):
                liste[i] = self.liste_coeff[i] + other.liste_coeff[i]

        elif n > k:
            for i in range(k):
                liste[i] = self.liste_coeff[i] + other.liste_coeff[i]
            for i in range(k,n):
                liste[i] = self.liste_coeff[i]
        
        else: 
            for i in range(n):
                liste[i] = self.liste_coeff[i] + other.liste_coeff[i]
            for i in range(n,k):
                liste[i] = other.liste_coeff[i]
    
        return Polynomial(liste)


p1 = Polynomial([1,2,3])
p2 = Polynomial([3,0,4])
print(p1)
print(p1.add(p2)) 


   def scalar(self, c):
       liste=c*self.liste_coeff
       return polynomial(liste)
   
        self.scalaire = c
