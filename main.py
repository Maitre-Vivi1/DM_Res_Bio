# TODO : Commenter / restructurer le code suivant consignes

# Travail avec un fichier tabulé / DataFrame
import pandas as pd
# Pour l'écriture du graph d'intéractions
import json
import numpy

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


# fonction utilisée afin de délister les éléments
def flatten(d):
 v = [[i] if not isinstance(i, list) else flatten(i) for i in d]
 return [i for b in v for i in b]


# Construction de la fonction permettant de décrire les intéractions entre protéines
def read_interaction_file_dict(nom_fichier):
    dico = {} # Initialisation du dictionnaire
    for a in range(0, len(nom_fichier)):
        try:
            if len(dico[nom_fichier.Sommet[a]]) > 0:
                dico[nom_fichier.Sommet[a]] = flatten([dico[nom_fichier.Sommet[a]], nom_fichier.Interaction[a]])
                pass
        except:
            dico[nom_fichier.Sommet[a]] = nom_fichier.Interaction[a]
    return dico

read_interaction_file_dict(Human_HighQuality)

def read_interaction_file_list(data):
    res_list = []
    for i in range(len(data)):
        res1 = [data.Sommet[i], data.Interaction[i]]
        res2 = [data.Interaction[i], data.Sommet[i]]
        if res1 not in res_list and res2 not in res_list:
            res_list.append(res1)
        pass
    return res_list

read_interaction_file_list(Human_HighQuality)


# TODO : Trop long :O
# Question 1.2.3 structure 3
def read_interaction_file_mat(data):
    list_sommet = list(data.Sommet[data.Sommet.duplicated()==False])
    list_interaction = list(data.Interaction[data.Interaction.duplicated()==False])
    res_mat = pd.DataFrame(numpy.zeros((len(list_interaction), len(list_sommet)), dtype=int),
                               index=list_interaction, columns=list_sommet)
    res_list = []
    for i in range(len(data)):
        res = [data.Sommet[i], data.Interaction[i]]
        res_list.append(res)
    for sommet in list_sommet:
        for interaction in list_interaction:
            if [sommet, interaction] in res_list:
                res_mat.loc[interaction][sommet] = 1
    l_som =  list(res_mat.columns)
    return res_mat, l_som

read_interaction_file_mat(Human_HighQuality)


# Question 2.4

def read_interactions_file(nom_fichier):
    d_int = read_interaction_file_dict(nom_fichier)
    l_int = read_interaction_file_list(nom_fichier)
    mat = read_interaction_file_mat(nom_fichier)
    m_int = mat[1]
    l_som = mat[2]
    return(d_int, l_int, m_int, l_som)

# Question 2.5

# On pourrait se contenter de seulement le disctionnaire / la liste ou bien la matrice et sa liste de sommets
# puisque ces objets caractérisent tous complétement le graphe d'intéraction










