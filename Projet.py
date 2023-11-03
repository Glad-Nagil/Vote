from ast import Break # Importation de la Bibliothèque contenant Break
from random import * # Importation de la Bibliothèque random qui contient plusieurs module

Candidats = ["Glad", "Princesse"] #Déclaration des deux Candidats
Etudiants = [ "Sibelle", "Berthonge","Glad", "Japhet", "Princesse", "Herdy", "Merveille", "Exau", "Darnel", "Mercia"] #Déclaration de étudiants de la salle qui vont voter
pt_Glad = 0 # Initialisation et déclaration de la variable point de Glad en (pt_Glad)
pt_Princesse= 0# Initialisation et déclaration de la variable point de Princesse en (pt_Princesse)
N_E = 1 #Initialisation et déclaration du notre d'essaie des bonnes réponses en cas du second tour

print(f"Voici les deux candidats : {Candidats}\n") # Affichage des Candidats à l'écran
for i in Etudiants: # Condition avec la boucle for 
    try: # Début de la Condition pour traiter l'erreur des chaines de caractères
        print("attention si votre choix est invalide, il ne sera pas pris en compte lors du décompte des voix\n".upper()) #Affichage de l'avertissement à chaque étudiant avant de voter
        n = int (input(f"*{i}* Veuillez faire le choix de votre candidat en appuyant sur 1 ou deux 2 : ")) #  Demande à l'étudiant de choisir son candidat pour le vote
    except ValueError: # Fin de la Condition pour traiter l'erreur des chaines de caractères
        print("Merci pour votre choix du candidats\n ")#Affiche un message de remerciement 
        continue # Permet à la boucle de continue même si l'étudiant choisit un ou plusieurs caractères à la place des chiffres
    if (n==1): # Condition if
        print("Merci pour votre choix du candidats\n ")#Affiche un message de remerciement 
        pt_Glad = pt_Glad + 1 # Incrémentation pour les points de Glad
    elif (n==2):# Condition elif
        print("Merci pour votre choix du candidats\n ") #Affiche un message de remerciement 
        pt_Princesse = pt_Princesse + 1 # Incrémentation pour les points de Princesse
    else:# Condition else qui est le contraire if
        print("Merci pour votre choix du candidats\n ")#Affiche un message de remerciement 

print(f"{Candidats[0]} vous avez {pt_Glad} Points\n ")#Affiche le nombre de point(s) de Glad après les votes
print(f"{Candidats[1]} vous avez {pt_Princesse} Points\n ")#Affiche le nombre de point(s) de Princesse après les votes

if pt_Glad > pt_Princesse: # Condition if
    print(f"{Candidats[0]} est élu Délégué\n ")#Affiche que Glad est élu après les votes
elif pt_Glad < pt_Princesse: # Condition elif
    print(f"{Candidats[1]} est élue Déléguée\n ")#Affiche que Princesse est élue après les votes
else: # Condition else qui est le contraire if 
    print("Les deux candidats ont les mêmes points, il faut choisir aléatoirement un élève qui va revoter afin de les départager\n ")

    Aleatoire = ["Sibelle", "Berthonge", "Japhet","Herdy", "Merveille", "Exau", "Darnel", "Mercia"] #Liste des étudiants qui peuvent revoter au second tour en cas d'égalité au premier tour
    Elu = choice(Aleatoire) # La machine va choisir aléatoirement un seul étudiant parmi ceux qui peuvent revoter pour le second tour
    print(f"L'élève élu aléatoirement pour revoter est : {Elu}\n ") #Affichage de l'étudiant qui a été choisi aléatoirement pour revoter 
    print("attention si votre choix est invalide, il ne sera pas pris en compte lors du décompte des voix\n".upper()) #Affichage de l'avertissement à l'étudiant choisi avant de revoter
    
    while N_E > 0 : # Condition avec la boucle while pour le nombre d'éssaie (N_E)
        try: #Début de la Condition pour traiter l'erreur des chaines de caractères
            n = int (input(f"*{Elu}* Veuillez faire le choix de votre candidat en appuyant sur 1 ou deux 2 : \n "))#  Demande à l'étudiant de choisir son candidat pour le vote de départage
        except ValueError: # Fin de la Condition pour traiter l'erreur des chaines de caractères
            print("La valeur saisie n'est pas un nombre\n ") #Affiche un message d'erreur
            print("Reprenez la saisie\t") # Demande à l'étudiant de reprendre son choix
            continue# Permet à la boucle de continue même si l'élève choisit un ou plusieurs caractères à la place des chiffres
        if (n!=1 and n!=2): # Condition if
            print("Votre choix est invalide, Reprenez la saisie\t") #Affiche un message d'erreur
            continue# Permet à la boucle de continue même si l'étudiant choisit des chiffres différents de 1 et 2
        elif (n==1): # Condition elif
            print("Suite au second vote, Glad est élu délégué\n ") #Affiche que Glad est élu après les votes suite au second tour 
            Break # Permet d'arrêter la boucle dès que l'étudiant saisi 1
            N_E -= 1 # Décrémentation du nombre d'essaie pour que l'étudiant ne saisisse plus rien
        else: # Condition else qui est le contraire if 
            print("Suite au second vote, Princesse est élu délégué\n") # Affiche que Princesse est élue après les votes suite au second tour 
            Break # Permet d'arrêter la boucle dès que l'étudiant saisi 1
            N_E -= 1 # Décrémentation du nombre d'essaie pour que l'étudiant ne saisisse plus rien