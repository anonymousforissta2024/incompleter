#Source: https://stackoverflow.com/questions/76595047/typeerror-guerrier-init-missing-1-required-positional-argument-armure
class Personnage:
    def __init__(self, nom, sexe, couleur, pdv, experience):
        self.nom = nom
        self.sexe = sexe
        self.couleur = couleur
        self.pdv = pdv
        self.experience = experience

    def attaquer(self):
        print(f"{self.nom} attaque l'ennemi.")

    def seDefendre(self):
        print(f"{self.nom} se defend contre l'attaque ennemie.")


class Guerrier(Personnage):
    def __init__(self, nom, sexe, couleur, pdv, experience, force, armure):
        super().__init__(nom, sexe, couleur, pdv, experience)
        self.force = force
        self.armure = armure

    def attaquer(self):
        print(f"{self.nom} assene un puissant coup avec sa force de {self.force}.")

    def seDefendre(self):
        print(f"{self.nom} se protege avec son armure de {self.armure}.")


class Mage(Personnage):
    def __init__(self, nom, sexe, couleur, pdv, experience, intelligence, sorts):
        super().__init__(nom, sexe, couleur, pdv, experience)
        self.intelligence = intelligence
        self.sorts = sorts

    def lancer_sort(self):
        print(f"{self.nom} lance un sort puissant avec son intelligence.")

class GuerrierMage(Guerrier, Mage):
    def __init__(self, nom, sexe, couleur, pdv, experience, force, armure):
        Guerrier.__init__( nom, sexe, couleur, pdv, experience, force, armure)
        Mage.__init__( nom, sexe, couleur, pdv, experience,intelligence,sorts)


# Creation d'une instance de la classe GuerrierMage
guerriermage1 = GuerrierMage("GuerrierMage1", "masculin", "rouge", 100, 10, 8, "arrmure")