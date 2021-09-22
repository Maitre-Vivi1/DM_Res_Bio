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

import pandas as pd

data = pd.read_csv('C:\\Users\\vivi1\\Desktop\\Master BIS\\Réseaux bio\\Human_HighQuality.txt', sep='\t')
data.columns = ['Sommet', 'Interaction']


def read_interaction_file_dict(nom_fichier):
    dictionnaire = {}
    for i in range(1,len(nom_fichier)):

        while nom_fichier.at[i-1, "Sommet"] == nom_fichier.at[i, "Sommet"]:
            inter = [inter, nom_fichier.at[i-1, "Sommet"]]

    return dictionnaire

read_interaction_file_dict(data)

