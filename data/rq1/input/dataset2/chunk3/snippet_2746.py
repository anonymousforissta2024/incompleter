#Source: https://stackoverflow.com/questions/53198653/super-new-cls-args-kwargs-reports-an-error-typeerror-object-take
class Personne:
    def __init__(self, nom, prenom):
        print("Appel de la méthode __init__")
        self.nom = nom
        self.prenom = prenom

    def __new__(cls, nom, prenom):
        print("Appel de la méthode __new__ de la classe {}".format(cls))
        return object.__new__(cls, nom, prenom)

personne = Personne("Doe", "John")