#########################################################
# Groupe LDDBI 6
# Clémence GERMETTE
# Sofia TERKI
# Erwan MAIRE
# Adam JACCOU
#########################################################

# Librairies
import tkinter as tk

# Constantes
NOMBRE_LIGNE = 6
NOMBRE_COLONNE = 7
DIAMETRE_JETON = 100

# Variables globals
configuration = []
jeuton = []
joueur = 1

# Fonctions

def configuration_initiale():
    """
    Création d'une grille vide
    """
    global configuration
    if configuration != []:
        configuration = []
    for i in range(NOMBRE_LIGNE):
            configuration.append([0 for j in range(NOMBRE_COLONNE)])
    return configuration


def affichage_jeuton():
    """
    Fonction qui associe à chaque valeur de la configuration le jeuton de couleur corespondante
    """
    canvas.delete('all')
    del jeuton[:]
    for i in range(NOMBRE_LIGNE):
        for j in range(NOMBRE_COLONNE):
            if configuration[i][j] == 0:
                color = "white"
            elif configuration[i][j] == 1:
                color = "red"
            elif configuration[i][j] == 2:
                color = "yellow"
            jeuton.append(canvas.create_oval(j*(DIAMETRE_JETON)+10, i*(DIAMETRE_JETON)+10,
             (j+1)*(DIAMETRE_JETON)-10, (i+1)*(DIAMETRE_JETON)-10,fill = color, outline = color))

            
def mouvement_jeton(event):
    """Fonction qui permet de faire tomber le jeton dans la
    grille jusqu'à toucher le fond ou un autre jeton"""
    global joueur, configuration
    x = event.x
    ligne = -1
    
    #Détermination de la colonne sur laquelle le joueur a cliqué
    if x<100:
        colonne = 0
    if 100<x<200:
        colonne = 1
    if 200<x<300:
        colonne = 2
    if 300<x<400:
        colonne = 3
    if 400<x<500:
        colonne = 4
    if 500<x<600:
        colonne = 5
    if 600<x<700:
        colonne = 6
        
    while configuration[ligne][colonne] != 0:
        ligne -= 1
    if joueur == 1:
        configuration[ligne][colonne] = 1
        joueur = 2
    elif joueur == 2:
        configuration[ligne][colonne] = 2
        joueur = 1
    affichage_jeuton()
    determination_du_gagnant()
    
def determination_du_gagnant():
    """Fonction qui détermine le gagnant en vérifiant si 4 jetons sont alignés"""
    winner = False #variable qui permet de voir s'il y a un gagant
    #vérifie si 4 jetons sont alignés dans une colonne
    for j in range(NOMBRE_COLONNE):
        for i in range (NOMBRE_LIGNE):
            if configuration[-i][j]==1 and configuration[-i+1][j] == 1 and configuration[-i+2][j]==1 and configuration[-i+3][j]== 1:
                print("Joueur 1 is the WINNER!")
                winner = True
            if configuration[-i][j]==2 and configuration[-i+1][j]==2 and configuration[-i+2][j]==2 and configuration[-i+3][j]== 2:
                print("Joueur 2 is the WINNER!")
                winner = True
    #vérifie si 4 jetons sont alignés dans une ligne
    for i in range(NOMBRE_LIGNE):
        for j in range (NOMBRE_COLONNE):
            if configuration[i][-j]==1 and configuration[i][-j+1]==1 and configuration[i][-j+1]==1 and configuration[i][-j+3]== 1:
                print("Joueur 1 is the WINNER!")
                winner = True
            if configuration[i][-j]==2 and configuration[i][-j+1]==2 and configuration[i][-j+2]==2 and configuration[i][-j+3]== 2:
                print("Joueur 2 is the WINNER!")
                winner = True
    #match nul
    if 0 not in configuration and winner == False:
        print("Manche nulle")

    
# Affichage graphique

racine = tk.Tk()
canvas = tk.Canvas(racine, width=DIAMETRE_JETON*NOMBRE_COLONNE, height=DIAMETRE_JETON*NOMBRE_LIGNE, bg="blue")

canvas.grid()

canvas.bind('<Button>', mouvement_jeton )
configuration_initiale()
affichage_jeuton()


racine.mainloop()
