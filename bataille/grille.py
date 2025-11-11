class Grille:
    def __init__(self, taille=5):
        self.taille = taille
        # 0 = vide, 1 = bateau, 2 = touché, 3 = raté
        self.cases = [[0] * taille for _ in range(taille)]

    def _dans_limites(self, ligne, col):
        """Vérifie si les coordonnées sont valides."""
        return 0 <= ligne < self.taille and 0 <= col < self.taille

    def placer_bateau(self, debut, fin):
        """Place un bateau d'une case à une autre (horizontal ou vertical)."""
        l1, c1 = debut
        l2, c2 = fin

        if not (self._dans_limites(l1, c1) and self._dans_limites(l2, c2)):
            return False

        # Seulement horizontal ou vertical
        if l1 != l2 and c1 != c2:
            return False

        # Vérifier que la place est libre
        if l1 == l2:
            pas = 1 if c1 <= c2 else -1
            for c in range(c1, c2 + pas, pas):
                if self.cases[l1][c] != 0:
                    return False
            for c in range(c1, c2 + pas, pas):
                self.cases[l1][c] = 1
        else:
            pas = 1 if l1 <= l2 else -1
            for l in range(l1, l2 + pas, pas):
                if self.cases[l][c1] != 0:
                    return False
            for l in range(l1, l2 + pas, pas):
                self.cases[l][c1] = 1
        return True

    def recevoir_tir(self, position):
        """Gère un tir à une position donnée. Renvoie 'touché', 'raté' ou 'déjà tiré'."""
        l, c = position
        if not self._dans_limites(l, c):
            raise ValueError("Position hors limites !")

        if self.cases[l][c] == 1:
            self.cases[l][c] = 2
            return "touché"
        elif self.cases[l][c] == 0:
            self.cases[l][c] = 3
            return "raté"
        else:
            return "déjà tiré"

    def tous_coules(self):
        """Vérifie si tous les bateaux ont été coulés."""
        for ligne in self.cases:
            if 1 in ligne:
                return False
        return True
