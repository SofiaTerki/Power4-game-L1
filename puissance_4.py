#########################################################
# Groupe LDDBI 6
# Clémence GERMETTE
# Sofia TERKI
# Erwan MAIRE
# Adam JACCOU
# https://github.com/uvsq22005047/Projet_puissance_4.git
#########################################################

########## Librairies
import tkinter as tk
import random
import copy

########## Constantes
NOMBRE_LIGNE = 6
NOMBRE_COLONNE = 7
DIAMETRE_JETON = 100
start = True

########## Variables globals
configuration = []
jeuton = []
joueur = 1
list_sauvegarde = []
historique = []

# création d'un fichier déstiné à contenir le nom des fichier sauvegarder si ce premier n'existe pas
fichier_list_sauvegarde = open("list_nom_sauvegarde.txt","a")
fichier_list_sauvegarde.close

fichier_list_sauvegarde = open("list_nom_sauvegarde.txt","r")
for ligne in fichier_list_sauvegarde:
    list_sauvegarde.append(ligne)
fichier_list_sauvegarde.close

########## Fonctions

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
     et l'affiche dans la grille
    """
    canvas.delete('all')
    del jeuton[:]
    for i in range(NOMBRE_LIGNE):
        for j in range(NOMBRE_COLONNE):
            if configuration[i][j] == 0:
                color = "black"
            elif configuration[i][j] == 1:
                color = "red"
            elif configuration[i][j] == 2:
                color = "yellow"
            jeuton.append(canvas.create_oval(j*(DIAMETRE_JETON)+10, i*(DIAMETRE_JETON)+10,
             (j+1)*(DIAMETRE_JETON)-10, (i+1)*(DIAMETRE_JETON)-10,fill = color, outline = color))
            
def mouvement_jeton(event):
    """
    Fonction qui permet de faire tomber le jeton dans la
    grille jusqu'à toucher le fond ou un autre jeton
    """
    global joueur, configuration, column, historique
    config = copy.deepcopy(configuration)
    historique.append(config)
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
        
   if configuration[0][colonne] != 0:   
        None
    else:
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
            if configuration[-i][j]==1 and configuration[-(i+1)][j] == 1 and configuration[-(i+2)][j]==1 and configuration[-(i+3)][j]== 1:
                #print("Joueur 1 is the WINNER!")
                label = tk.Label(racine, text = "Joueur 1 is the WINNER!", font = "helvetica, 30")
                label.grid(column = 0, row = 2)
                winner = True
            if configuration[-i][j]==2 and configuration[-(i+1)][j]==2 and configuration[-(i+2)][j]==2 and configuration[-(i+3)][j]== 2:
                label = tk.Label(racine, text = "Joueur 2 is the WINNER!", font = "helvetica, 30")
                label.grid(column = 0, row = 2)
                winner = True

    #vérifie si 4 jetons sont alignés dans une ligne
    for i in range(NOMBRE_LIGNE):
        for j in range (NOMBRE_COLONNE):
            if configuration[i][-j]==1 and configuration[i][-(j+1)]==1 and configuration[i][-(j+2)]==1 and configuration[i][-(j+3)]== 1:
                label = tk.Label(racine, text = "Joueur 1 is the WINNER!", font = "helvetica, 30")
                label.grid(column = 0, row = 2)
                winner = True
            if configuration[i][-j]==2 and configuration[i][-(j+1)]==2 and configuration[i][-(j+2)]==2 and configuration[i][-(j+3)]== 2:
                label = tk.Label(racine, text = "Joueur 2 is the WINNER!", font = "helvetica, 30")
                label.grid(column = 0, row = 2)
                winner = True

    #match nul
    """if (0 not in configuration) and (winner == False):
        label = tk.Label(racine, text = "Manche nulle!", font = "helvetica, 30")
        label.grid(column = 0, row = 2) ###y a un problème à chaque clique ça affiche manche nulle????"""

def colonne_bloquee(): #la fonction ne marche pas
    global column
    for i in range (NOMBRE_COLONNE):
        for j in range(NOMBRE_LIGNE):
            if configuration[i][j] !=0:
                del column[j]

def sauvegarde():
    """
    Fonction qui enregistre la configuration actuel dans un fichier
     et le nom de ce fichier dans list_nom_sauvegarde.txt
    """
    global list_sauvegarde, list_fichier_charge

    nom_fichier = entré_nom_fichier_sauvegarde.get()
    
    list_sauvegarde.append(nom_fichier)

    # Ajout du nom du fichier à la liste des fichier sauvegarder dans le fichier "list_nom_sauvegarde.txt"
    fichier_list_sauvegarde = open("list_nom_sauvegarde.txt","a")
    fichier_list_sauvegarde.write(nom_fichier+"\n")
    fichier_list_sauvegarde.close
    
    # Création du fichier contenant la configuration à sauvegarder
    fichier_sauvegarde = open(nom_fichier+".txt","w")
    for i in configuration:
        for j in i:
            fichier_sauvegarde.write(str(j))
        fichier_sauvegarde.write("\n")
    fichier_sauvegarde.close
    
    # Ajout du fichier à la liste de chargement
    list_sauvegarde = []
    fichier_list_sauvegarde = open("list_nom_sauvegarde.txt","r")
    for ligne in fichier_list_sauvegarde:
        list_sauvegarde.append(ligne)
    fichier_list_sauvegarde.close

    del(list_fichier_charge)
    list_fichier_charge = tk.Listbox(frame_charge, bd=0, activestyle='none', fg="white", bg="grey1")
    list_fichier_charge.grid(column=1,row=0)
    for i in list_sauvegarde:
        list_fichier_charge.insert('end', i)

def charger():
    """
    Fonction de chargement des configuration enregistrer
    """
    global configuration
    
    nom_fichier = list_fichier_charge.get(list_fichier_charge.curselection())
    nom_fichier = list(nom_fichier)
    del(nom_fichier[-1])
    nom_fichier = "".join(nom_fichier)
    
    config = []

    fichier_charger = open(nom_fichier+".txt","r")
    for ligne in fichier_charger:
        config.append(list(ligne))
    # Supression du saut à la ligne
    for i in config:
        del(i[-1])
    # Convertion des élémentde la liste en entier
    for i in range(NOMBRE_LIGNE):
        for j in range(NOMBRE_COLONNE):
            config[i][j]=int(config[i][j])   
    fichier_charger.close

    configuration = config
    
    affichage_jeuton()

def demarrer():
    configuration_initiale()
    affichage_jeuton()

def retour():
    global configuration, historique, joueur
    configuration = historique[-1]
    del(historique[-1])
    if joueur == 1:
        joueur = 2
    elif joueur == 2:
        joueur = 1
    affichage_jeuton()

########## Affichage graphique

racine = tk.Tk()
racine.config(bg="grey1")
canvas = tk.Canvas(racine, width=DIAMETRE_JETON*NOMBRE_COLONNE, height=DIAMETRE_JETON*NOMBRE_LIGNE, bg="indigo")

### Création des wigdests

# Widget de sauvegarde
frame_sauvegarde = tk.LabelFrame(racine,text="nommez votre fichier à sauvegarder", bd=0, fg="grey", bg="grey1")
entré_nom_fichier_sauvegarde = tk.Entry(frame_sauvegarde, fg="white", bg="grey1")
bouton_sauvegarder = tk.Button(frame_sauvegarde, text="sauvegarde", bg="grey1", fg="orange", command=lambda : sauvegarde())
# Widget de chargement
frame_charge = tk.LabelFrame(racine,text="Choisisser une sauvegarde", bd=0, fg="grey", bg="grey1")
list_fichier_charge = tk.Listbox(frame_charge, bd=0, activestyle='none', fg="white", bg="grey1")
for i in list_sauvegarde:
    list_fichier_charge.insert('end', i)
bouton_charger = tk.Button(frame_charge, text="charge", bg="grey1", fg="orange", command=lambda : charger())
# widdet d'annulation
bouton_retour = tk.Button(racine, text="annuler", bg="grey1", fg="orange", command = lambda : retour())
bouton_demarrer = tk.Button(racine, text = "démarrer", bg="grey1", fg="orange", command = demarrer)

### Placement des widgets
canvas.grid(column=0,row=0, rowspan=4)
# Widdets de sauvegarde
frame_sauvegarde.grid(column=1, row=0)
entré_nom_fichier_sauvegarde.grid(column=0, row=0)
bouton_sauvegarder.grid(column=1, row=0)
# widdets de chargement
frame_charge.grid(column=1, row=1)
list_fichier_charge.grid(column=1,row=0)
bouton_charger.grid(column=1, row=1)
# widget d'annulation
bouton_retour.grid(column=1, row=3)
bouton_demarrer.grid(column=1, row = 2)

#liaison d'événements 
canvas.bind('<Button>', mouvement_jeton )



# Lancement de l'interface graphique
racine.mainloop()
