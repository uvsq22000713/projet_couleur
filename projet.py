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


####################################################################
#création de la fenetre principale
racine = tk.Tk()
racine.config(bg='gray84')
racine.title("Jeu de couleurs")

#################################################################  
#constantes et listes
cpt_temps = 30
cpt_score = 0
liste_couleurs = ["red", "blue", "green", "pink","orange", "yellow", "white"]
liste_mots = ["Rouge", "Bleu", "Vert", "Rose","Orange", "Jaune", "Blanc"]
temps_ecoule = ''
mot = tkFont.Font(family='Baskerville Old Face', size=18, weight='bold')
texte = tkFont.Font(family='Baskerville Old Face', size=18)
score_temps = tkFont.Font(family='Baskerville Old Face', size=16)
bouton = tkFont.Font(family='Arial Black', weight='bold', size=9)
demarrer_reinitialiser = tkFont.Font(family='Baskerville Old Face', size=13)

#################################################################
#fonctions

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
    """ Rénitialise le temps et aussi le score du joueur """
    global cpt_temps, cpt_score
    #partie temps
    racine.after_cancel(temps_ecoule)
    bouton_demarrer['state'] = 'normal'
    cpt_temps = 30
    message_temps.configure(text="Temps restant: " + str(cpt_temps) + 's')

    #partie score
    cpt_score = 0
    message_score.config(text="Score: " + str(cpt_score))


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
mots = tk.Label(text= "MOTS EN COULEURS",font=mot, fg="blue", bg='gray84')

#boutons couleurs
bouton_rouge  = tk.Button(text="Rouge", font=bouton, bg="red", bd=0, height=3,
                width= 15, activebackground='red')
bouton_bleu   = tk.Button(text="Bleu", font=bouton, bg="blue", bd=0, height=3,
                width= 15, activebackground='blue')
bouton_vert   = tk.Button(text="Vert", font=bouton, bg="green", bd=0, height=3,
                width= 15, activebackground='green')
bouton_rose   = tk.Button(text="Rose", font=bouton, bg="pink", bd=0, height=3,
                width= 15, activebackground='pink')
bouton_orange = tk.Button(text="Orange", font=bouton, bg="orange", bd=0,
                height=3, width= 15, activebackground='orange')
bouton_jaune  = tk.Button(text="Jaune", font=bouton, bg="yellow", bd=0,
                height=3, width= 15, activebackground='yellow')
bouton_blanc  = tk.Button(text="Blanc", font=bouton, bg="white", bd=0,
                height=3, width= 15)

#boutons demarrer et reinitialiser
bouton_demarrer   = tk.Button(text=" Démarrer ", bg='gray55', width=20,
                height=2, command=temps_restant, font=demarrer_reinitialiser,
                activebackground='gray55')
bouton_reinitaliser = tk.Button(text=" Réinitialiser ", bg='gray55', width=20,
                height=2, command=reinitialiser, font=demarrer_reinitialiser,
                activebackground='gray55')

#positionnement des widgets
texte1.pack()
message_score.pack()
message_temps.pack()

    #zone d'affichage des mots
mots.place(x=285, y=125)

    #boutons couleurs
bouton_rouge.place(x=50, y=250)
bouton_bleu.place(x=200, y=250)
bouton_vert.place(x=350, y=250)
bouton_rose.place(x=500, y=250)
bouton_orange.place(x=650, y=250)
bouton_jaune.place(x=275, y=335)
bouton_blanc.place(x=425,y=335)

    #boutons demarrer et reinitialiser
bouton_demarrer.place(x=10, y=370)
bouton_reinitaliser.place(x=605, y=370)

#messages d'informations







###############################################################
#lancement de la fenetre principale
racine.geometry('825x433')
racine.mainloop()