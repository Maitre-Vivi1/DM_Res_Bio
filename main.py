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

# df exemple
#df = pd.DataFrame({'Sommet': ["ZW10_HUMAN", "ZWINT_HUMAN", "ZY11B_HUMAN", "ZYX_HUMAN", "ZYX_HUMAN", "ZN384_HUMAN"],
 #                  'Interaction': ["ZWINT_HUMAN", "ZW10_HUMAN", "ELOC_HUMAN","NEBL_HUMAN", "ZN384_HUMAN", "ZYX_HUMAN"]})

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
    return res_mat

read_interaction_file_mat(Human_HighQuality)