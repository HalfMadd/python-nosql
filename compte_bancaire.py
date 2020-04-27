class CompteBancaire: 
    def __init__(self, nom, nb) :
        self.nom = nom
        self.solde = nb
        
    def depot(self, somme):
        self.solde += somme
    
    def retrait(self, somme):
        self.solde -= somme
        
    def affiche(self):
        print("Le solde du compte bancaire de "+self.nom+" est de "+str(self.solde)+" euros.") 


x = CompteBancaire('azerty', 1000)
x.depot(150)
x.retrait(100)
x.affiche()