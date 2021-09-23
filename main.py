# Travail avec un fichier tabulé / DataFrame
import pandas as pd
# Pour l'écriture du graph d'intéractions
import json

# Question 1.1

Graph_Inter_Vivien = {
    "A": ["B", "E"],
    "B": ["A", "C", "F"],
    "C": ["B", "F", "I"],
    "D": ["F"],
    "E": ["A"],
    "F": ["B", "C", "D"],
    "G": ["J"],
    "H": ["J"],
    "I": ["C", "J"],
    "J": ["G", "H", "I"]
}

with open('Graph_Inter_Vivien.txt', 'w') as file:
    file.write(json.dumps(Graph_Inter_Vivien))

# Question 2.1

# On charge le fichier correspondant au travail demandé dans l'environnement de travail en précisant
# le nom des deux colonnes
Human_HighQuality = pd.read_csv('Human_HighQuality.txt', sep='\t', header=0, names=['Sommet', 'Interaction'])
donnees_test = Human_HighQuality.loc[1:50]


# fonction utilisée afin de délister les éléments
def flatten(d):
 v = [[i] if not isinstance(i, list) else flatten(i) for i in d]
 return [i for b in v for i in b]


# Construction de la fonction permettant de décrire les intéractions entre protéines
def read_interaction_file_dict(nom_fichier):
    dico = {} # Initialisation du dictionnaire
    for a in range(1, len(nom_fichier)):
        try:
            if len(dico[nom_fichier.Sommet[a]]) > 0:
                dico[nom_fichier.Sommet[a]] = flatten([dico[nom_fichier.Sommet[a]], nom_fichier.Interaction[a]])
                pass
        except:
            dico[nom_fichier.Sommet[a]] = nom_fichier.Interaction[a]
    return dico

def read_interaction_file_list(data):
    res_list = []
    for i in range(len(data)):
        res1 = [data.Sommet[i], data.Interaction[i]]
        res2 = [data.Interaction[i], data.Sommet[i]]
        if res1 not in res_list and res2 not in res_list:
            res_list.append(res1)
        pass
    return res_list

read_interaction_file_dict(Human_HighQuality)



