class pol_anneau:
    
    def __init__(self,liste_coeff, n, q):
        self.liste_coeff = liste_coeff
        self.dmax = n
        self.coeffmod = q
        
        
        if len(self.liste_coeff)-1 >=self.dmax:
             liste=[]
             liste=[0]*(self.dmax+1)
             for i in range(self.dmax):
                liste[i]= self.liste_coeff[i]%self.coeffmod
             for i in range(self.dmax,len(self.liste_coeff)):
                liste[i%self.dmax] = liste[i%self.dmax] + (-1)**i//self.dmax*self.liste_coeff[i]%self.coeffmod
             self.liste_coeff = liste
            
    def __str__(self) :

            polynome = str( self.liste_coeff[0] % self.coeffmod)
            k=0
            for coef in self.liste_coeff[1:]:
                coef = coef%self.coeffmod
                k += 1 
                if coef == 0:
                    continue
                elif coef > 0:
                    polynome = polynome + '+' + str(coef) + '*X^' + str(k)
                else:
                    polynome = polynome + '-' + str(coef) + '*X^' + str(k)
                
            return polynome


p1 = pol_anneau([6,2,3,0,0,0,5], 4, 5)
print(p1)