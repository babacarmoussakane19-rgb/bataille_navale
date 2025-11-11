# Projet : Bataille Navale (Python)

Ce projet est une mini-implémentation du jeu Bataille Navale en Python.  
Il inclut :

- Une grille de jeu
- La gestion des bateaux (placement horizontal/vertical)
- Un système de tirs (touché, manqué, coulé)
- Une interface en ligne de commande via main.py
- Des tests unitaires avec pytest

------------------------------------

## Structure du projet

bataille_navale/
│
├── bataille/
│   ├── __init__.py
│   ├── grille.py        # Gestion de la grille
│   ├── jeu.py           # Logique du jeu
│
├── tests/
│   ├── __init__.py
│   ├── test_jeu.py      # Tests unitaires
│
├── main.py              # Programme principal
├── requirements.txt     # Dépendances
└── README.md            # Documentation du projet

------------------------------------

## Installation

1. Cloner le projet :

```bash
git clone https://github.com/babacarmoussakane19-rgb/bataille_navale
cd bataille_navale
Créer et activer un environnement virtuel :

Sous Windows :

python -m venv .venv
.venv\Scripts\activate
Sous Linux / Mac :

python3 -m venv .venv
source .venv/bin/activate
Installer les dépendances :

pip install -r requirements.txt
Lancer le jeu

python main.py
Le programme vous demande des positions sous la forme :
ligne,colonne
Exemple :
1,2
Exécuter les tests unitaires
pytest
Résultat attendu (exemple) :
3 passed in 0.05s
Description technique
grille.py
Représente la grille (taille configurable).

Stocke les bateaux et les tirs.

Indique si un tir est touché ou manqué.

jeu.py
Contient la logique du jeu.

Gère le placement des bateaux.

Vérifie si tous les bateaux sont coulés.

main.py
Interface en ligne de commande pour jouer.

tests/test_jeu.py
Vérifie :

le placement des bateaux

la validité des tirs

la détection des bateaux coulés

Lien du dépôt GitHub :
https://github.com/babacarmoussakane19-rgb/bataille_navale

.gitignore
__pycache__/
*.pyc
.venv/
.env/
.vscode/