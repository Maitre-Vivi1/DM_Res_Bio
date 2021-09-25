from Chapitre_1 import read_interactions_file, flatten
import pandas as pd

df = pd.DataFrame({'Sommet': ["ZW10_HUMAN", "ZWINT_HUMAN", "ZY11B_HUMAN", "ZYX_HUMAN", "ZYX_HUMAN", "ZN384_HUMAN"],
                  'Interaction': ["ZWINT_HUMAN", "ZW10_HUMAN", "ELOC_HUMAN", "NEBL_HUMAN", "ZN384_HUMAN", "ZYX_HUMAN"]})


# Question 2.1.1
def count_vertices(nom_fichier):
    graph = read_interactions_file(nom_fichier)
    return len(graph[0])


#  Question 2.1.2
def count_edges(nom_fichier):
    graph = read_interactions_file(nom_fichier)
    return len(flatten(graph[0].values()))


# Question 2.1.3
"""
Écrire une fonction clean_interactome(filein, fileout) qui lit un fichier contenant un graphe d’interactions
protéine-protéine et y enlève (i) toutes les interactions
redondantes, et (ii) tous les homo-dimères. Le graphe obtenu sera écrit dans un nouveau
fichier au même format que le format de départ (posez-vous la question de savoir si ça
ne vaut pas le coup d’écrire une ou plusieurs fonctions d’écriture d’un graphe dans un
fichier).
"""


def clean_interactome(nom_fichier):
    graph = read_interactions_file(nom_fichier)
    return graph
