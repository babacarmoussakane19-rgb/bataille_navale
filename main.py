from bataille.jeu import Jeu

def jouer_demo():
    jeu = Jeu(taille=5)
    # Exemples de bateaux
    jeu.placer_bateau((0, 0), (0, 1))
    jeu.placer_bateau((2, 2), (4, 2))

    print(" Bienvenue dans la Bataille Navale ! ")

    while not jeu.tous_les_bateaux_coules():
        tir = input("Entrez une position (ligne,colonne) ex: 1,2 → ")
        try:
            l, c = map(int, tir.split(","))
        except Exception:
            print(" Format invalide, réessayez.")
            continue

        resultat = jeu.tirer((l, c))
        print(f"Résultat du tir : {resultat}")

    print(" Tous les bateaux ont été coulés ! Bravo !")

if __name__ == "__main__":
    jouer_demo()