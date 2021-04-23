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
texte = tkFont.Font(family='Baskerville Old Face', size=15)
score_temps = tkFont.Font(family='Baskerville Old Face', size=14)
bouton = tkFont.Font(family='Arial Black', weight='bold', size=9)

#################################################################
#fonctions

def temps_restant():
    """ Fait le décompte du temps imparti (30 secondes) """
    global cpt_temps, temps_ecoule
    bouton_demarrer["state"] = "disabled"  #desactivation du bouton démarrer
    message_temps.configure(text="Temps restant: " + str(cpt_temps-1))
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
    message_temps.configure(text="Temps restant: " + str(cpt_temps))

    #partie score
    cpt_score = 0
    message_score.config(text="Score: " + str(cpt_score))


################################################################################################
#création et positionnement des widgets

#messages d'informations
texte1 = tk.Label(text=" Tapez la couleur des mots, pas le texte des mots ! ! !", font=texte, bg='gray84')
texte1.grid(row=0, column=0, padx=50, pady=10, columnspan=5)

message_score = tk.Label(text="Score: " + str(cpt_score), font=score_temps, bg='gray84')
message_score.grid(row=1, column=0, columnspan=5)

message_temps = tk.Label(text="Temps restant: " + str(cpt_temps), font=score_temps, bg='gray84')
message_temps.grid(row=2, column=0, columnspan=5)

#zone d'affichage des mots
mots = tk.Label(text= "MOTS EN COULEURS",font=mot, fg="blue", bg='gray84')
mots.grid(row=3, column=0, pady=30, columnspan=5, sticky="we")

#boutons couleurs
bouton_rouge  = tk.Button(text="Rouge", font=bouton, bg="red", bd=0, height=3, width= 15)
bouton_bleu   = tk.Button(text="Bleu", font=bouton, bg="blue", bd=0, height=3, width= 15)
bouton_vert   = tk.Button(text="Vert", font=bouton, bg="green", bd=0, height=3, width= 15)
bouton_rose   = tk.Button(text="Rose", font=bouton, bg="pink", bd=0, height=3, width= 15)
bouton_orange = tk.Button(text="Orange", font=bouton, bg="orange", bd=0, height=3, width= 15)
bouton_jaune  = tk.Button(text="Jaune", font=bouton, bg="yellow", bd=0, height=3, width= 15)
bouton_blanc  = tk.Button(text="Blanc", font=bouton, bg="white", bd=0, height=3, width= 15)

bouton_rouge.grid(row=4 ,column=0, padx=8)
bouton_bleu.grid(row=4 ,column=1, padx=8)
bouton_vert.grid(row=4 ,column=2, padx=8)
bouton_rose.grid(row=4 ,column=3, padx=8)
bouton_orange.grid(row=4 ,column=4, padx=8)
bouton_jaune.grid(row=5 ,column=1,columnspan=2, pady=15)
bouton_blanc.grid(row=5 ,column=2, columnspan=2, pady=15)

#boutons demarrer et reinitialiser
bouton_demarrer   = tk.Button(text=" Démarrer ", bg='gray55', width=20, height=2, command=temps_restant)
bouton_reinitaliser = tk.Button(text=" Réinitialiser ", bg='gray55', width=20, height=2, command=reinitialiser)
bouton_demarrer.grid(row=5, rowspan=2, column=0, pady=50)
bouton_reinitaliser.grid(row=5, rowspan=2, column=4)






###############################################################
#lancement de la fenetre principale

racine.mainloop()