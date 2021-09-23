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

import json

with open('Graph_Inter_Vivien.txt', 'w') as file:
    file.write(json.dumps(Graph_Inter_Vivien))


# Question 2.1

# Travail avec un fichier tabulé / DataFrame
import pandas as pd

# On charge le fichier correspondant au travail demandé dans l'environnement de travail en précisant le nom des deux colonnes
Human_HighQuality = pd.read_csv('Human_HighQuality.txt', sep='\t', header=0, names=['Sommet','Interaction'])

# Construction de la fonction permettant de décrire les intéractions entre protéines
def read_interaction_file_dict(nom_fichier):
    dictionnaire = {}
    for i in range(1,len(nom_fichier)):

        while nom_fichier.at[i-1, "Sommet"] == nom_fichier.at[i, "Sommet"]:
            inter = [inter, nom_fichier.at[i-1, "Sommet"]]

    return dictionnaire


# Question structure 2
def read_interaction_file_list(data):
    res_list = []
    for i in range(len(data)):
        res1 = [data.Sommet[i], data.Interaction[i]]
        res2 = [data.Interaction[i], data.Sommet[i]]
        if res1 not in res_list and res2 not in res_list:
            res_list.append(res1)
        pass
    return res_list

read_interaction_file_dict(data)
read_interaction_file_list(Human_HighQuality)


#Question structure 3
def read_interaction_fiile_mat():
    pass