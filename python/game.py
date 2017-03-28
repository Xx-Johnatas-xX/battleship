# Game file

from random import randint
from classes import CaseJoueur, CaseNao

# Initialisation des variables
bateaux = [2, 3, 3, 4, 5]
carte_nao = [[0 for x in range(9)] for y in range(9)] # Celle ou il y a les bateaux de Nao et les endroits ou le joueur a touche
carte_joueur = [[0 for x in range(9)] for y in range(9)] # Celle ou Nao marque ou il tire/touche (celle ou il y a les probas)
vie_nao = sum(bateaux)
vie_joueur = sum(bateaux)
tir_nao = 0
tir_joueur = 0

# Initialisation de la carte joueur
for i in range(0, 9):
    for j in range(0, 9):
        carte_joueur[i][j] = CaseJoueur("inconnu", float(vie_joueur)/(100-tir_joueur))

# Initialisation de la carte Nao
for i in range(0, 9):
    for j in range(0, 9):
        carte_nao[i][j] = CaseNao("rien", "eau")

# Placement des bateaux
abs_random = randint(0, 9)
ord_random = randint(0, 9)
direction_random = randint(0, 1)

if direction_random == 0:
    if (abs_random < 6) and carte_nao[abs_random][ord_random].bateau == "rien" and carte_nao[abs_random + 1][ord_random].bateau == "rien" and carte_nao[abs_random + 2][ord_random].bateau == "rien" and carte_nao[abs_random + 3][ord_random].bateau == "rien" and carte_nao[abs_random + 4][ord_random].bateau == "rien":
        for k in range(0, 4):
            carte_nao[abs_random + k][ord_random].bateau = "Porte Avion"

if direction_random == 1:
    if (ord_random < 6) and carte_nao[abs_random][ord_random].bateau == "rien" and carte_nao[abs_random][ord_random + 1].bateau == "rien" and carte_nao[abs_random][ord_random + 2].bateau == "rien" and carte_nao[abs_random][ord_random + 3].bateau == "rien" and carte_nao[abs_random][ord_random + 4].bateau == "rien":
        for k in range(0, 4):
            carte_nao[abs_random][ord_random + k].bateau = "Porte Avion"

