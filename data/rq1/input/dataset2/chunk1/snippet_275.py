#Source: https://stackoverflow.com/questions/34777773/typeerror-object-takes-no-parameters-after-defining-new
class Personne:
    def __init__(self, nom, prenom):
        print("Appel de la méthode __init__")
        self.nom = nom
        self.prenom = prenom

    def __new__(cls, nom, prenom):
        print("Appel de la méthode __new__ de la classe {}".format(cls))
        return object.__new__(cls, nom, prenom)

personne = Personne("Doe", "John")