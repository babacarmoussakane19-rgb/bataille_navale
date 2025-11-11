Projet : Bataille Navale (Python)

Ce projet est une mini-implémentation du jeu **Bataille Navale** en Python.  
Il comprend :

- Une grille de jeu  
-  Une logique pour placer des bateaux  
-  Un système de tirs (touché / manqué / coulé)  
-  Une interface en ligne de commande (CLI) dans `main.py`  
-  Des tests unitaires avec **pytest**
##  Structure du projet

bataille_navale/
│
├── bataille/
│ ├── init.py
│ ├── grille.py # Gestion de la grille
│ ├── jeu.py # Logique du jeu

├── tests/
│ ├── test_jeu.py # Tests unitaires pytest
| |──__init__.py 
│
├── main.py # Programme principal (CLI)
├── requirements.txt # Dépendances (pytest)
└── README.md # Documentation

##  Installation
### 1️ Cloner le projet
```bash
git clone https://github.com/babacarmoussakane19-rgb/bataille_navale
cd bataille_navale
### Copy code
python -m venv .venv
source .venv/Scripts/activate  #
 Lancer le jeu (CLI)
Pour jouer à la bataille navale :

python main.py
Le programme vous demandera d'entrer des positions sous la forme :

ligne,colonne
Exemple :

1,2
 Lancer les tests unitaires
Assurez-vous que l'environnement virtuel est activé, puis :

pytest
Vous devriez obtenir un résultat du type :

3 passed in 0.05s

 ### Explication technique rapide
Le jeu repose sur deux modules :

 grille.py
Gère la grille (5×5 ou autre taille)

Stocke les bateaux et les tirs

Indique si un tir est touché ou manqué

 jeu.py
Gère la logique du jeu

Permet de placer des bateaux

Vérifie si tous les bateaux sont coulés

Renvoie le résultat d’un tir

 main.py
Interface texte pour jouer

  tests/test_jeu.py
Vérifie que la logique du jeu fonctionne :

placement de bateaux

tirs

détection de bateaux coulés

 Auteur
Projet réalisé par Babacar Moussa kane
Répertoire GitHub :
https://github.com/babacarmoussakane19-rgb/bataille_navale


---

# .gitignore

pycache/
*.pyc
.venv/
.env/.vscode/