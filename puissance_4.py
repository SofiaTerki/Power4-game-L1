#########################################################
# Groupe LDDBI 6
# Clémence GERMETTE
# Sofia TERKI
# Erwan MAIRE
# Adam JACCOU
#########################################################

# Librairies
import tkinter as tk
import random

# Constantes
NOMBRE_LIGNE = 6
NOMBRE_COLONNE = 7
DIAMETRE_JETON = 100
start = True

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
    global joueur, configuration, column
    x = event.x
    ligne = -1
    column =[0, 1, 2, 3, 4, 5, 6]
    #Détermination de la colonne sur laquelle le joueur a cliqué
    if x<100:
        colonne = column[0]
    if 100<x<200:
        colonne = column[1]
    if 200<x<300:
        colonne = column[2]
    if 300<x<400:
        colonne = column[3]
    if 400<x<500:
        colonne = column[4]
    if 500<x<600:
        colonne = column[5]
    if 600<x<700:
        colonne = column[6]
        
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
                #print("Joueur 1 is the WINNER!")
                label = tk.Label(racine, text = "Joueur 1 is the WINNER!", font = "helvetica, 30")
                label.grid(column = 0, row = 2)
                winner = True
            if configuration[-i][j]==2 and configuration[-i+1][j]==2 and configuration[-i+2][j]==2 and configuration[-i+3][j]== 2:
                label = tk.Label(racine, text = "Joueur 2 is the WINNER!", font = "helvetica, 30")
                label.grid(column = 0, row = 2)
                winner = True

    #vérifie si 4 jetons sont alignés dans une ligne
    for i in range(NOMBRE_LIGNE):
        for j in range (NOMBRE_COLONNE):
            if configuration[i][-j]==1 and configuration[i][-j+1]==1 and configuration[i][-j+1]==1 and configuration[i][-j+3]== 1:
                label = tk.Label(racine, text = "Joueur 1 is the WINNER!", font = "helvetica, 30")
                label.grid(column = 0, row = 2)
                winner = True
            if configuration[i][-j]==2 and configuration[i][-j+1]==2 and configuration[i][-j+2]==2 and configuration[i][-j+3]== 2:
                label = tk.Label(racine, text = "Joueur 2 is the WINNER!", font = "helvetica, 30")
                label.grid(column = 0, row = 2)
                winner = True

    #match nul
    if (0 not in configuration) and (winner == False):
        label = tk.Label(racine, text = "Manche nulle!", font = "helvetica, 30")
        label.grid(column = 0, row = 2) ###y a un problème à chaque clique ça affiche manche nulle????

def colonne_bloquee(): #la fonction ne marche pas
    global column
    for i in range (NOMBRE_COLONNE):
        for j in range(NOMBRE_LIGNE):
            if configuration[i][j] !=0:
                del column[j]
    

def sauvegarde():
    nom_fichier = input("Nom du fichier à sauvegarder")
    fichier_sauvegarde = open(nom_fichier+".txt","w")
    for i in configuration:
        for j in i:
            fichier_sauvegarde.write(str(j))
        fichier_sauvegarde.write("\n")
    fichier_sauvegarde.close

def charger():
    global configuration
    nom_fichier = input("Nom du fichier à charger")
    fichier_charger = open(nom_fichier+".txt","r")
    config = []
    for ligne in fichier_charger:
        config.append(list(ligne))
    print(config)
    print(type(config))
    print(type(config[2][3]))
    for i in config:
        del(i[-1])
    for i in range(NOMBRE_LIGNE):
        for j in range(NOMBRE_COLONNE):
            config[i][j]=int(config[i][j])
    print(config)
    print(type(config))
    print(type(config[2][3]))    
    fichier_charger.close
    configuration = config
    affichage_jeuton()

def demarrer():
    configuration_initiale()
    affichage_jeuton()



##############################################################################################################
# Affichage graphique

racine = tk.Tk()
canvas = tk.Canvas(racine, width=DIAMETRE_JETON*NOMBRE_COLONNE, height=DIAMETRE_JETON*NOMBRE_LIGNE, bg="blue")

#création des wigdests
bouton_sauvegarder = tk.Button(racine, text="sauvegarde", command=lambda : sauvegarde())
bouton_charger = tk.Button(racine, text="charge", command=lambda : charger())
bouton_demarrer = tk.Button(racine, text = "démarrer", command = demarrer)

# Placement des widgets
canvas.grid(column=0,row=0, rowspan=2)
bouton_sauvegarder.grid(column=1, row=0)
bouton_charger.grid(column=1, row=1)
bouton_demarrer.grid(column=1, row = 2)


#liaison d'événements 
canvas.bind('<Button>', mouvement_jeton )

# fonctions appliquées avant le démarrage de la fenêtre graphique
#configuration_initiale()
#affichage_jeuton()

# Lancement de l'interface graphique
racine.mainloop()
