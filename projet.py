##################################################
# groupe 5 MPCI TD 07
# Sami BENIZID-MONNIER
# Dihia HAMMADI
# Mohand-Hedi KASHI
# Ibrahima Ndene NDIAYE
# Sam Khong Lucas RASAMIZANANY
# Mohamed-Amine ZEHAR
#https://github.com/uvsq22000713/projet_couleur
##################################################


import tkinter as tk
import tkinter.font as tkFont
import random as rd


####################################################################
#création de la fenetre principale
racine = tk.Tk()
racine.config(bg='gray84')
racine.title("Jeu de couleurs")
racine.geometry('825x433')
racine.maxsize(width=825, height=433)

#################################################################  
#constantes et listes
cpt_temps = 30
cpt_score = 0
liste_couleurs = ["red", "blue", "green", "pink","orange", "yellow", "white"]
liste_mots = ["Rouge", "Bleu", "Vert", "Rose","Orange", "Jaune", "Blanc"]
temps_ecoule = ''

#police d'écriture
mot = tkFont.Font(family='Baskerville Old Face', size=18, weight='bold')
texte = tkFont.Font(family='Baskerville Old Face', size=18)
score_temps = tkFont.Font(family='Baskerville Old Face', size=16)
texte = tkFont.Font(family='Baskerville Old Face', size=15)
score_temps = tkFont.Font(family='Baskerville Old Face', size=14)
bouton = tkFont.Font(family='Arial Black', weight='bold', size=9)
demarrer_reinitialiser = tkFont.Font(family='Baskerville Old Face', size=13)

#################################################################
#fonctions
def demarrer():
    """ Fonction qui lance 2 autres fonctions à partir du bouton démarrer """
    generateur_mots()
    temps_restant()

def temps_restant():
    """ Fait le décompte du temps imparti (30 secondes) """
    global cpt_temps, temps_ecoule
    bouton_demarrer["state"] = "disabled"  #desactivation du bouton démarrer
    message_temps.configure(text="Temps restant: " + str(cpt_temps-1) + 's')
    cpt_temps -= 1
    temps_ecoule = racine.after(1000, temps_restant)
    
    if cpt_temps == 0:     # remet le compteur à 30 et réactive le bouton démarrer 
        racine.after_cancel(temps_ecoule)
        cpt_temps = 30
        bouton_demarrer["state"] = "normal"

def reinitialiser():
    """ Rénitialise le temps et le score du joueur """
    global cpt_temps, cpt_score
    #partie temps
    racine.after_cancel(temps_ecoule)
    bouton_demarrer['state'] = 'normal'
    cpt_temps = 30
    message_temps.configure(text="Temps restant: " + str(cpt_temps) + 's')

    #partie score
    cpt_score = 0
    message_score.config(text="Score: " + str(cpt_score))

    #partie mots
    mots.configure(text="")

def generateur_mots():
    """ Génére un mot (une couleur) écrit avec une couleur aléatoire """
    global liste_couleurs, liste_mots, couleur
    mot = liste_mots[rd.randint(0,6)]
    couleur = liste_couleurs[rd.randint(0,6)]
    mots.configure(text=mot, fg=couleur)
    if str(couleur):
        pass

def Couleur(COULEUR):
    """ Fonction liés à chaque boutons de couleur """
    global cpt_score, couleur   
    if COULEUR == str(couleur):
        cpt_score += 1
        message_score.config(text="Score: " + str(cpt_score))
        generateur_mots()

    
    


################################################################################################
#création et positionnement des widgets
#création des widgets

texte1 = tk.Label(text=" Tapez la couleur des mots, pas le texte des mots ! ! !",
                font=texte, bg='gray84')
message_score = tk.Label(text="Score: " + str(cpt_score), font=score_temps,
                bg='gray84')
message_temps = tk.Label(text="Temps restant: " + str(cpt_temps) + 's',
                font=score_temps, bg='gray84')

#zone d'affichage des mots
mots = tk.Label(text= "",font=mot, bg='gray84')

#boutons couleurs
bouton_rouge  = tk.Button(text="Rouge", font=bouton, bg=liste_couleurs[0],
                bd=0, height=3, width= 15, activebackground='red',
                command=lambda: Couleur('red'))
bouton_bleu   = tk.Button(text="Bleu", font=bouton, bg=liste_couleurs[1],
                bd=0, height=3, width= 15, activebackground='blue',
                command=lambda: Couleur('blue'))
bouton_vert   = tk.Button(text="Vert", font=bouton, bg=liste_couleurs[2],
                bd=0, height=3, width= 15, activebackground='green',
                command=lambda: Couleur('green'))
bouton_rose   = tk.Button(text="Rose", font=bouton, bg=liste_couleurs[3],
                bd=0, height=3, width= 15, activebackground='pink',
                command=lambda: Couleur('pink'))
bouton_orange = tk.Button(text="Orange", font=bouton, bg=liste_couleurs[4],
                bd=0, height=3, width= 15, activebackground='orange',
                command=lambda: Couleur('orange'))
bouton_jaune  = tk.Button(text="Jaune", font=bouton, bg=liste_couleurs[5],
                bd=0, height=3, width= 15, activebackground='yellow',
                command=lambda: Couleur('yellow'))
bouton_blanc  = tk.Button(text="Blanc", font=bouton, bg=liste_couleurs[6],
                bd=0, height=3, width= 15, command=lambda: Couleur('white'))

#boutons demarrer et reinitialiser
bouton_demarrer   = tk.Button(text=" Démarrer ", bg='gray55', width=20,
                height=2, command=demarrer, font=demarrer_reinitialiser,
                activebackground='gray55')
bouton_reinitaliser = tk.Button(text=" Réinitialiser ", bg='gray55', width=20,
                height=2, command=reinitialiser, font=demarrer_reinitialiser,
                activebackground='gray55')

#positionnement des messages d'informations
texte1.pack()
message_score.pack()
message_temps.pack()

#zone d'affichage des mots
mots.pack(pady=50)

#position boutons couleurs
bouton_rouge.place(x=50, y=250)
bouton_bleu.place(x=200, y=250)
bouton_vert.place(x=350, y=250)
bouton_rose.place(x=500, y=250)
bouton_orange.place(x=650, y=250)
bouton_jaune.place(x=275, y=335)
bouton_blanc.place(x=425,y=335)

#position boutons demarrer et reinitialiser
bouton_demarrer.place(x=10, y=370)
bouton_reinitaliser.place(x=605, y=370)








###############################################################
#lancement de la fenetre principale
racine.mainloop()