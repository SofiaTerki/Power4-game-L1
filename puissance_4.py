#########################################################
# Groupe LDDBI 6
# Clémence GERMETTE
# Sofia TERKI
# Erwan MAIRE
# Adam JACCOU
# https://github.com/uvsq22005047/Projet_puissance_4.git
#########################################################

########## Probleme non résolue

"""
Le label d'affichage du gagnant ou du match nul reste quelque fois
 devant la grille sans qu'on sache pourquoi alors qu'il devrait disparaitre.
"""

########## Librairies
import tkinter as tk
import copy
import random

########## Constantes
NOMBRE_LIGNE = 6
NOMBRE_COLONNE = 7
DIAMETRE_JETON = 70
start = True

########## Variables globals
configuration = []
jeuton = []
joueur = None
list_sauvegarde = []
historique = []
label = None


# création d'un fichier déstiné à contenir le nom des fichier sauvegarder si ce premier n'existe pas
fichier_list_sauvegarde = open("list_nom_sauvegarde.txt","a")
fichier_list_sauvegarde.close

fichier_list_sauvegarde = open("list_nom_sauvegarde.txt","r")
for ligne in fichier_list_sauvegarde:
    list_sauvegarde.append(ligne)
fichier_list_sauvegarde.close

########## Fonctions

def demarrer():
    """
    Fonction qui initialise tous les parametre éssenciel pour le début d'une nouvelle partie.
    """
    global joueur, label, compteur
    
    # Supprime les label si il y en a
    if label == None:
        None
    else:
        label.grid_forget()
    
    # détermination du joueur qui commence en premier
    joueur = random.randint(1,2)

    # Création d'une grille vide
    configuration_initiale()
    
    # Affichage de la grille
    affichage_jeuton()

    #liaison d'événements 
    canvas.bind('<Button>', mouvement_jeton )


def configuration_initiale():
    """
    Fonction qui créé une grille vide.
    """
    global configuration

    if configuration != []:
        configuration = []
    for i in range(NOMBRE_LIGNE):
            configuration.append([0 for j in range(NOMBRE_COLONNE)])
    return configuration


def affichage_jeuton():
    """
    Fonction qui associe à chaque valeur de la configuration l'absence ou la présence
     d'un jeuton de couleur corespondante et l'affiche dans la grille.
    """

    # Supression de l'affichage de la grille
    canvas.delete('all')
    del jeuton[:]
    
    # Création d'un nouvel affichage de la grille
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
    grille jusqu'à toucher le fond ou un autre jeton.
    """
    global joueur, configuration, historique
    
    # Sauvegarde de de la configration afin de faire un retour vers elle si besoin
    historique.append(copy.deepcopy(configuration))
    
    # Détermination de la colonne sur laquelle le joueur a cliqué
    x = event.x
    ligne = -1
    if x<DIAMETRE_JETON:
        colonne = 0
    elif DIAMETRE_JETON<x<DIAMETRE_JETON*2:
        colonne = 1
    elif DIAMETRE_JETON*2<x<DIAMETRE_JETON*3:
        colonne = 2
    elif DIAMETRE_JETON*3<x<DIAMETRE_JETON*4:
        colonne = 3
    elif DIAMETRE_JETON*4<x<DIAMETRE_JETON*5:
        colonne = 4
    elif DIAMETRE_JETON*5<x<DIAMETRE_JETON*6:
        colonne = 5
    elif DIAMETRE_JETON*6<x<DIAMETRE_JETON*7:
        colonne = 6

    # Pas d'action si la colonne est plaine    
    if configuration[0][colonne] != 0:   
        None
    # Chute du jeuton s'il y a encor de la place dans la colonne
    else:
        while configuration[ligne][colonne] != 0:
            ligne -= 1
        if joueur == 1:
            configuration[ligne][colonne] = 1
            joueur = 2
        elif joueur == 2:
            configuration[ligne][colonne] = 2
            joueur = 1
        
        # Mise à jour de l'affichage de la grille 
        affichage_jeuton()
        
        # Vérification des allignement des jeutons
        determination_du_gagnant()


def compte_jeton():
    """
    Fonction qui compte le nombre de jeton dans la grille
    """
    compteur = 0
    for j in range(NOMBRE_COLONNE):
        for i in range (NOMBRE_LIGNE):
            if configuration[i][j] != 0:
                compteur += 1
    return compteur


def affichage_fin_partie(texte_fin_partie):
    """
    Fonction qui affiche le gagnant
    """
    global label
    
    # Affichage gagnant
    label = tk.Label(racine, text = texte_fin_partie , font = "helvetica, 30")
    label.grid(column = 0, row = 1, rowspan =2)

    # Empêche de rajouter un pion
    canvas.unbind('<Button>')


def determination_du_gagnant():
    """
    Fonction qui détermine le gagnant en vérifiant si 4 jetons sont alignés.
    """
    global compteur
    
    # Variable qui determine la fin de la partie
    partie_non_nulle = False 

    # Vérifie si 4 jetons sont alignés dans une colonne
    for j in range(NOMBRE_COLONNE):
        for i in range (NOMBRE_LIGNE):
            if i+2 == NOMBRE_LIGNE-1:
                break
            else:    
                if configuration[i][j] == 1 and configuration[i+1][j] == 1 and configuration[i+2][j] ==1 and configuration[i+3][j] == 1:
                    affichage_fin_partie("Vainqueur:\nJoueur 1")
                    partie_non_nulle = True
            
                if configuration[i][j] == 2 and configuration[i+1][j] == 2 and configuration[i+2][j] ==2 and configuration[i+3][j] == 2:
                    affichage_fin_partie("Vainqueur:\nJoueur 2")
                    partie_non_nulle = True
    
    # Vérifie si 4 jetons sont alignés dans une ligne
    for i in range(NOMBRE_LIGNE):
        for j in range (NOMBRE_COLONNE):
            if j+2 == NOMBRE_COLONNE-1:
                break
            else:
                if configuration[i][j]==1 and configuration[i][j+1]==1 and configuration[i][j+2]==1 and configuration[i][j+3]== 1:
                    affichage_fin_partie("Vainqueur:\nJoueur 1")
                    partie_non_nulle = True

                if configuration[i][j]==2 and configuration[i][j+1]==2 and configuration[i][j+2]==2 and configuration[i][j+3]== 2:
                    affichage_fin_partie("Vainqueur:\nJoueur 2")
                    partie_non_nulle = True
    
    # Vérifie si 4 jetons sont alignés dans une diagonale en haut à gauche vers en bas à droite
    for i in range(NOMBRE_LIGNE):
        if i+2 == NOMBRE_LIGNE-1:
            break
        else:
            for j in range (NOMBRE_COLONNE):
                if j+2 == NOMBRE_COLONNE-1:
                    break
                else:
                    if configuration[i][j]==1 and configuration[i+1][j+1]==1 and configuration[i+2][j+2]==1 and configuration[i+3][j+3]== 1:
                        affichage_fin_partie("Vainqueur:\nJoueur 1")
                        partie_non_nulle = True

                    if configuration[i][j]==2 and configuration[i+1][j+1]==2 and configuration[i+2][j+2]==2 and configuration[i+3][j+3]== 2:
                        affichage_fin_partie("Vainqueur:\nJoueur 2")
                        partie_non_nulle = True
    
    # Vérifie si 4 jetons sont alignés dans une diagonale en haut à droite vers en bas à gauche
    for i in range(NOMBRE_LIGNE):
        if i+2 == NOMBRE_LIGNE-1:
            break
        else:
            for j in range (NOMBRE_COLONNE):
                if -1-(j+2) == -7:
                    break
                else:
                    if configuration[i][-1-(j)]==1 and configuration[i+1][-1-(j+1)]==1 and configuration[i+2][-1-(j+2)]==1 and configuration[i+3][-1-(j+3)]== 1:
                        affichage_fin_partie("Vainqueur:\nJoueur 1")
                        partie_non_nulle = True

                    if configuration[i][-1-(j)]==2 and configuration[i+1][-1-(j+1)]==2 and configuration[i+2][-1-(j+2)]==2 and configuration[i+3][-1-(j+3)]== 2:
                        affichage_fin_partie("Vainqueur:\nJoueur 2")
                        partie_non_nulle = True
                      
    # Vérifie si il y a match nul
    if partie_non_nulle == True:
        None    
    
    else:
        # Vérifie si la grille est rempli
        if compte_jeton() == NOMBRE_LIGNE*NOMBRE_COLONNE:
            # Affiche match nulle
            affichage_fin_partie("Manche nulle")


def sauvegarde():
    """
    Fonction qui enregistre la configuration actuel dans un fichier,
     le nom de ce fichier dans le fichier list_nom_sauvegarde.txt,
      et met à jour l'affichage graphique de la liste des fichier sauvegarder à charger.
    """
    global list_sauvegarde, list_fichier_charge

    # Récupération du nom du fichier à sauvegarder
    nom_fichier = entré_nom_fichier_sauvegarde.get()

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

    # Affichage graphique de la liste de chargement
    del(list_fichier_charge)
    list_fichier_charge = tk.Listbox(frame_charge, bd=0, activestyle='none', fg="white", bg="grey1")
    list_fichier_charge.grid(column=1,row=0)
    for i in list_sauvegarde:
        list_fichier_charge.insert('end', i)


def charger():
    """
    Fonction de chargement des configurations enregistrés.
    """
    global configuration, joueur, label, compteur
    
    # Supression du saut à la ligne dans le nom du fichier sélectionner
    nom_fichier = list_fichier_charge.get(list_fichier_charge.curselection())
    nom_fichier = list(nom_fichier)
    del(nom_fichier[-1])
    nom_fichier = "".join(nom_fichier)
    
    # Chargement de la configuration
    configuration = []
    fichier_charger = open(nom_fichier+".txt","r")
    for ligne in fichier_charger:
        configuration.append(list(ligne))
    # Supression du saut à la ligne
    for i in configuration:
        del(i[-1])
    # Convertion des élémentde la liste en entier
    for i in range(NOMBRE_LIGNE):
        for j in range(NOMBRE_COLONNE):
            configuration[i][j]=int(configuration[i][j])   
    fichier_charger.close
    
    # Mise à jour de l'affichage
    affichage_jeuton()

    # Supprime les label si il y en a
    if label == None:
        None
    else:
        label.grid_forget()
    
    # détermination du joueur qui commence en premier
    joueur = random.randint(1,2)

    #liaison d'événements 
    canvas.bind('<Button>', mouvement_jeton )


def retour():
    """
    Fonction qui annule l'action précedente d'ajout de jeton
    """
    global configuration, historique, joueur
    
    # replace la configuration précedente
    configuration = historique[-1]
    
    # suprime le dernier élément de l'historique
    del(historique[-1])
    
    # Redéfinie corectement le joueur qui doit jouer pour le prochain tour
    if joueur == 1:
        joueur = 2
    elif joueur == 2:
        joueur = 1

    # Supprime les label si il y en a
    if label == None:
        None
    else:
        label.grid_forget()

    #liaison d'événements 
    canvas.bind('<Button>', mouvement_jeton )

    # Mise à jour de l'affichage
    affichage_jeuton()



########## Affichage graphique

racine = tk.Tk()
racine.config(bg="grey1")
racine.title("Puissance 4")
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
bouton_demarrer = tk.Button(racine, text = "démarrer une nouvelle partie", bg="grey1", fg="orange", command = demarrer)

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

# Lancement de l'interface graphique
racine.mainloop()
