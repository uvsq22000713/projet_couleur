######################
#Version 1
#fait par Sami
#####################


import tkinter as tk 


####################################################################
#création de la fenetre principale
racine = tk.Tk()
racine.title("Jeu de couleurs")


#################################################################
#constantes et listes
cpt_temps = 30
cpt_score = 0
liste_couleurs = ["red", "blue", "green", "pink","orange", "yellow", "white"]
liste_mots = ["Rouge", "Bleu", "Vert", "Rose","Orange", "Jaune", "Blanc"]


#################################################################
#fonctions

def temps_restant():
    """ Fait le décompte du temps imparti (30 secondes) """
    global cpt_temps
    bouton_demarrer["state"] = "disabled"  #desactivation du bouton démarrer
    message_temps.configure(text="Temps restant: " + str(cpt_temps-1)s)
    cpt_temps -= 1
    temps_écoulé = racine.after(1000, temps_restant)
    
    if cpt_temps < 0:     # remet le compteur à 30 et réactive le bouton démarrer 
        racine.after_cancel(temps_écoulé)
        cpt_temps = 30
        bouton_demarrer["state"] = "normal"



        




################################################################################################
#création et positionnement des widgets

#messages d'informations
texte1 = tk.Label(text=" Tapez la couleur des mots, pas le texte des mots ! ! !", font=(15))
texte1.grid(row=0, column=0, padx=50, pady=10, columnspan=5)

message_score = tk.Label(text="Score: " + str(cpt_score))
message_score.grid(row=1, column=0, columnspan=5)

message_temps = tk.Label(text="Temps restant: " + str(cpt_temps))
message_temps.grid(row=2, column=0, columnspan=5)

#zone d'affichage des mots
mots = tk.Label(text= "MOTS EN COULEURS",font=50, fg="blue")
mots.grid(row=3, column=0, pady=50, columnspan=5, sticky="we")

#boutons couleurs
bouton_rouge  = tk.Button(text="Rouge", bg="red", bd=0, height=3, width= 15)
bouton_bleu   = tk.Button(text="Bleu", bg="blue", bd=0, height=3, width= 15)
bouton_vert   = tk.Button(text="Vert", bg="green", bd=0, height=3, width= 15)
bouton_rose   = tk.Button(text="Rose", bg="pink", bd=0, height=3, width= 15)
bouton_orange = tk.Button(text="Orange", bg="orange", bd=0, height=3, width= 15)
bouton_jaune  = tk.Button(text="Jaune", bg="yellow", bd=0, height=3, width= 15)
bouton_blanc  = tk.Button(text="Blanc", bg="white", bd=0, height=3, width= 15)

bouton_rouge.grid(row=4 ,column=0, padx=8)
bouton_bleu.grid(row=4 ,column=1, padx=8)
bouton_vert.grid(row=4 ,column=2, padx=8)
bouton_rose.grid(row=4 ,column=3, padx=8)
bouton_orange.grid(row=4 ,column=4, padx=8)
bouton_jaune.grid(row=5 ,column=1,columnspan=2, pady=15)
bouton_blanc.grid(row=5 ,column=2, columnspan=2, pady=15)

#boutons demarrer et reinitialiser
bouton_demarrer   = tk.Button(text=" Démarrer ", bg='light grey', width=20, height=2, command=temps_restant)
bouton_reinitaliser = tk.Button(text=" Réinitialiser ", bg='light grey', width=20, height=2)
bouton_demarrer.grid(row=5, rowspan=2, column=0, pady=50)
bouton_reinitaliser.grid(row=5,rowspan=2, column=4)





###############################################################
#lancement de la fenetre principale
racine.mainloop()