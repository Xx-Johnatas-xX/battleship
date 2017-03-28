# Game file

# Initialisation des variables
eau = "O"
tir = "X"
touche = "#"
taille_carte = 10
batteaux = [2, 3, 3, 4, 5]
carte_nao = [] # Celle ou il y a les bateaux de Nao et les endroits ou le joueur a touche
carte_joueur = [] # Celle ou Nao marque ou il tire/touche (celle ou il y a les probas)
vie_nao = sum(batteaux)
vie_joueur = sum(batteaux)
tir_nao = 0
tir_joueur = 0
position_bateaux = []
