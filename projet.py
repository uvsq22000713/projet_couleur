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


from os import truncate
import tkinter as tk
import tkinter.font as tkFont
import random as rd
from tkinter.constants import LEFT, TRUE

####################################################################


#création de la fenetre principale
racine = tk.Tk()
racine.geometry('825x433')
racine.config(bg='gray84')
racine.title("Jeu de couleurs")
racine.iconbitmap('D:\Lucas\L1MPCI\S2\LSIN200\Projets\Couleurs\projet_couleur-1\icone.ico')


#################################################################  
#constantes et listes

    #listes
liste_couleurs = ["red", "blue", "green", "pink","orange", "yellow", "white"]
liste_mots = ["Rouge", "Bleu", "Vert", "Rose","Orange", "Jaune", "Blanc"]
liste_1, liste_2= [], []
listeIntermediaire = []

    #variables
minus_score, minus_temps, bonus_score, bonus_temps = 0, 0, 1, 0
cpt_temps, cpt_score = 30, 0
temps_ecoule = ''
difficulte = "normal"
compteur = 0

    #bool
verif_temps = True




cpt = 0
mini_liste=[]
liste_verif = []

#police d'écriture
mot = tkFont.Font(family='Baskerville Old Face', size=30, weight='bold')
texte = tkFont.Font(family='Baskerville Old Face', size=16)
score_temps = tkFont.Font(family='Baskerville Old Face', size=16)
texte_1 = tkFont.Font(family='Baskerville Old Face', size=19, weight='bold')
diff = tkFont.Font(family='Baskerville Old Face', size=14)
bouton = tkFont.Font(family='Arial Black', weight='bold', size=9)
demarrer_reinitialiser = tkFont.Font(family='Baskerville Old Face', size=13)

#################################################################
#fonctions

def demarrer():
    """ Démarre une partie de jeu """
    global verif_temps, cpt_score
    verif_temps = True
    cpt_score = 0
    message_score.config(text="Score: " + str(cpt_score))
    generateur_mots()
    temps_restant()

def temps_restant():
    """ Fait le décompte du temps imparti (30 secondes) """
    global cpt_temps, temps_ecoule, verif_temps
    bouton_demarrer["state"] = "disabled"  #desactivation du bouton démarrer
    message_temps.configure(text="Temps restant: " + str(cpt_temps-1) + 's')
    cpt_temps -= 1
    temps_ecoule = racine.after(1000, temps_restant)
    
    if cpt_temps == 0:     #remet le compteur à 30 et réactive le bouton démarrer 
        racine.after_cancel(temps_ecoule)
        verif_temps = False
        for nom in bouton: #désactive les bouton une fois que le temps est écoulé
            nom.configure(state=tk.DISABLED)  
        print('Votre score est :' + str(cpt_score))  #test
        if difficulte == "normal": # 10 meilleurs score uniquement en difficulté normale
            topscore()
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

    #listes
    suppr_liste()
    modif_bouton()
    ecran.destroy()

def modif_bouton():
    ''' modifie l'état des boutons '''
    bouton_rouge.configure(border=0)
    bouton_bleu.configure(border=0)
    bouton_vert.configure(border=0)
    bouton_rose.configure(border=0)
    bouton_orange.configure(border=0)
    bouton_jaune.configure(border=0)
    bouton_blanc.configure(border=0)

def suppr_liste():
    ''' renitialise les listes impliqués dans la génération des mots '''
    ecran.destroy()
    liste_verif.clear()
    mini_liste.clear()
    liste_1.clear()
    liste_2.clear()

def generateur_mots():
    """ Génére un mot (une couleur) écrit avec une couleur aléatoire """
    global verif_temps, listeIntermediaire, compteur, ecran, bouton
    if verif_temps: #le générateur de mot ne se lance que si a == True, c'est a dire si le temps n'est pas écoulé
        compteur = rd.randint(2,6)
        ecran = tk.Canvas(racine)
        ecran.place(x=400, y=150, anchor='center')
        for i in range(compteur):
            liste_1.append(liste_couleurs[rd.randint(0,5)]) #liste avec les couleurs pour les fg des mots
            liste_2.append(liste_mots[rd.randint(0,5)]) #liste qui contient les mots pour la partie text
            listeIntermediaire = [liste_2[i], liste_1[i]]
            mini_liste.append(listeIntermediaire)
        for tc in mini_liste:
            tk.Label(ecran, text=tc[0] + '   ', fg=tc[1],
            font=texte_1, bg='gray84').pack(side = LEFT)
    else:  
        suppr_liste()
        modif_bouton()
        ecran.destroy()


def Couleur(COULEUR, bouton):
    """ Fonction liés à chaque boutons de couleur """
    global liste_verif, cpt_score, cpt_temps
    if verif_temps:
        if len(liste_verif) < len(liste_1):        
            bouton.configure(border=2, highlightbackground='black')
            liste_verif.append(COULEUR)
            print(liste_verif)

        elif len(liste_verif) == len(liste_1):
            if liste_verif == liste_1:
                cpt_score += bonus_score
                message_score.config(text="Score: " + str(cpt_score))
                cpt_temps += bonus_temps
                message_temps.configure(text="Temps restant: " + str(cpt_temps) + 's')
                modif_bouton()
                suppr_liste()
                generateur_mots()
            else:
                cpt_score -= minus_score
                cpt_temps -= minus_temps
                message_temps.configure(text="Temps restant: " + str(cpt_temps) + 's')
                message_score.config(text="Score: " + str(cpt_score))
                liste_verif.clear()
                modif_bouton()
    else:
        ecran.destroy()

    if cpt_temps < 0:
        reinitialiser()
        suppr_liste()

def topscore():
    """ Conserve les 10 meilleurs score dans le fichier de sauvegarde des scores """
    global cpt_score
    fic = open('Sauvegarde_des_scores', 'r')
    top10 = [int(ligne) for ligne in fic]
    fic.close()
    top10.append(cpt_score)
    top10.sort(reverse=True)
    if len(top10) > 10:
        top10.pop(10)
    fic = open('Sauvegarde_des_scores', 'w')

    for score in top10:
        fic.write("{}\n".format(str(score)))
    fic.close()

#fontionnalités additionnelles

def easy(event):
    """ mets le jeu en difficulté facile """
    global bonus_score, bonus_temps, difficulte
    difficulte = "facile"
    message_difficulte.config(text='Difficulté: FACILE')
    bonus_score = 2
    bonus_temps = 1

def normal(event):
    """ mets le jeu en difficulté normale """
    global minus_score, minus_temps, difficulte, bonus_score
    difficulte = "normal"
    message_difficulte.config(text='Difficulté: NORMALE')
    minus_score = 1
    minus_temps = 0
    bonus_score = 1

def hard(event):
    """ mets le jeu en difficulté difficile """
    global minus_score, minus_temps, difficulte
    difficulte = "difficile"
    message_difficulte.config(text='Difficulté: DIFFICILE')
    minus_score = 2
    minus_temps = 1

def hardcore(event):
    """ mets le jeu en difficulté hardcore """
    global minus_score, minus_temps, difficulte
    difficulte = "hardcore"
    message_difficulte.config(text='Difficulté: HARDCORE')
    minus_score = 10
    minus_temps = 5

def resetScore(event):
    ''' reinitialise le score du joueur dans le fichier sauvegarde '''
    fic = open('Sauvegarde_des_scores', 'w')
    fic.close()
    print('Scores réinitialisés')


################################################################################################


#création et positionnement des widgets
#création des widgets

texte1 = tk.Label(text=" Tapez la couleur des mots, pas le texte des mots ! ! !",
                font=texte, bg='gray84')
message_score = tk.Label(text="Score: " + str(cpt_score), font=score_temps,
                bg='gray84')
message_temps = tk.Label(text="Temps restant: " + str(cpt_temps) + 's',
                font=score_temps, bg='gray84')
message_difficulte = tk.Label(racine, text='Difficulté: NORMALE', 
                font=diff, bg='gray84')

#zone d'affichage des mots
ecran = tk.Canvas(racine, height= 30, bg='gray84', highlightbackground='gray84')

#boutons couleurs
bouton_rouge  = tk.Button(text="Rouge", font=bouton, bg=liste_couleurs[0],
                bd=0, height=3, width= 15, activebackground='red',
                command=lambda: Couleur('red', bouton_rouge))
bouton_bleu   = tk.Button(text="Bleu", font=bouton, bg=liste_couleurs[1],
                bd=0, height=3, width= 15, activebackground='blue',
                command=lambda: Couleur('blue', bouton_bleu))
bouton_vert   = tk.Button(text="Vert", font=bouton, bg=liste_couleurs[2],
                bd=0, height=3, width= 15, activebackground='green',
                command=lambda: Couleur('green', bouton_vert))
bouton_rose   = tk.Button(text="Rose", font=bouton, bg=liste_couleurs[3],
                bd=0, height=3, width= 15, activebackground='pink',
                command=lambda: Couleur('pink', bouton_rose))
bouton_orange = tk.Button(text="Orange", font=bouton, bg=liste_couleurs[4],
                bd=0, height=3, width= 15, activebackground='orange',
                command=lambda: Couleur('orange', bouton_orange))
bouton_jaune  = tk.Button(text="Jaune", font=bouton, bg=liste_couleurs[5],
                bd=0, height=3, width= 15, activebackground='yellow',
                command=lambda: Couleur('yellow', bouton_jaune))
bouton_blanc  = tk.Button(text="Blanc", font=bouton, bg=liste_couleurs[6],
                bd=0, height=3, width= 15, command=lambda: Couleur('white', bouton_blanc))

#liste simple contenant les noms des boutons
boutons = [bouton_blanc, bouton_bleu, bouton_jaune, bouton_orange, bouton_rose,
            bouton_rouge, bouton_vert]

#boutons demarrer et reinitialiser
bouton_demarrer   = tk.Button(text=" Démarrer ", bg='gray55', width=20,
                height=2, command=demarrer, font=demarrer_reinitialiser,
                activebackground='gray55')
bouton_reinitaliser = tk.Button(text=" Réinitialiser ", bg='gray55', width=20,
                height=2, command=reinitialiser, font=demarrer_reinitialiser,
                activebackground='gray55')

#positionnement des widgets
texte1.pack()
message_score.pack()
message_temps.pack()
message_difficulte.place(x=10, y=1)

#zone d'affichage des mots
ecran.pack(pady=50)

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


#gestion des actions de l'utilisateur
racine.bind('e', easy)
racine.bind('n', normal)
racine.bind('h', hard)
racine.bind('d', hardcore)
racine.bind('r', resetScore)


###############################################################


#lancement de la fenetre principale

racine.mainloop()


###############################################################
