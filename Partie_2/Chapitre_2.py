import sys
sys.path.append("C:/Users/vivi1/PycharmProjects/DM_Res_Bio/Partie_1")
from Chapitre_1 import read_interactions_file, flatten

# Question 2.1.1
def count_vertices(nom_fichier):
    graph = read_interactions_file(nom_fichier)
    return len(graph[0])


#  Question 2.1.2
def count_edges(nom_fichier):
    graph = read_interactions_file(nom_fichier)
    return len(flatten(graph[0].values()))


# TODO Question 2.1.3
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


# Question 2.2.1
def get_degree(file, prot):
    graph = read_interactions_file(file)
    if type(graph[0][prot]) == str:
        degree = 1
    else:
        degree = len(graph[0][prot])
    return degree


# Question 2.2.2
def get_max_degree(file):
    compteur = []
    for i in file.Sommet:
        compteur.append(get_degree(file, i))
    indice = compteur.index(max(compteur))
    nom_prot = file.Sommet[indice]
    deg_prot = max(compteur)
    return nom_prot, deg_prot


# Question 2.2.3
def get_ave_degree(file):
    compteur = []
    for i in file.Sommet:
        compteur.append(get_degree(file, i))
    return sum(compteur)/len(file.Sommet)


# Question 2.2.4
def count_degree(file, deg):
    compteur = 0
    for i in file.Sommet:
        if get_degree(file, i) == deg:
            compteur += 1
    return compteur


# Question 2.2.5
def histogram_degree(file, dmin, dmax):
    compteur = []
    for d in range(dmin, dmax + 1):
        compteur.append(count_degree(file, d))
    l = list(range(dmin, dmax + 1))
    for i in l:
        print(str(i) + " : " + "*" * compteur[i])
