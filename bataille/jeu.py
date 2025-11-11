from .grille import Grille

class Jeu :
    """Classe principale qui gère la logique du jeu de bataille navale."""

    def __init__(self, taille=5):
        self.grille = Grille(taille)

    def placer_bateau(self, debut, fin):
        """Place un bateau sur la grille."""
        return self.grille.placer_bateau(debut, fin)

    def tirer(self, position):
        """Effectue un tir et renvoie le résultat."""
        return self.grille.recevoir_tir(position)

    def tous_les_bateaux_coules(self):
        """Renvoie True si tous les bateaux sont coulés."""
        return self.grille.tous_coules()
