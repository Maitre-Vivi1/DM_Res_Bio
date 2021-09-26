import sys
sys.path.append("../DM_Res_Bio/Partie_1")
from Chapitre_1 import read_interactions_file, flatten


# Question 2.1.1
def count_vertices(file):
    """Compte le nombre de sommet du graphe en se servant de sa représentation en dictionnaire"""
    graph_tuple = read_interactions_file(file)
    return len(graph_tuple[0])


#  Question 2.1.2
def count_edges(file):
    """Compte le nombre d'arrêtes d'un graphe en se servant de sa représentation en dictionnaire"""
    graph_tuple = read_interactions_file(file)
    return len(flatten(graph_tuple[0].values()))


# TODO Question 2.1.3
"""
Écrire une fonction clean_interactome(filein, fileout) qui lit un fichier contenant un graphe d’interactions
protéine-protéine et y enlève (i) toutes les interactions
redondantes, et (ii) tous les homo-dimères. Le graphe obtenu sera écrit dans un nouveau
fichier au même format que le format de départ (posez-vous la question de savoir si ça
ne vaut pas le coup d’écrire une ou plusieurs fonctions d’écriture d’un graphe dans un
fichier).
"""


# Question 2.1.3
def clean_interactome(file):
    graph_tuple = read_interactions_file(file)
    return graph_tuple


# Question 2.2.1
def get_degree(file, prot_str):
    """Calcul le nombre d'interaction de la protéine choisie"""
    graph_tuple = read_interactions_file(file)
    if type(graph_tuple[0][prot_str]) == str:
        degree = 1
    else:
        degree = len(graph_tuple[0][prot_str])
    return degree


# Question 2.2.2
def get_max_degree(file):
    """Calcul le degré maximal obtenu par au moins une des protéines du graphe"""
    count_list = []
    for i in file.Sommet:
        count_list.append(get_degree(file, i))
    indice_int = count_list.index(max(count_list))
    nom_prot_str = file.Sommet[indice_int]
    deg_prot_int = max(count_list)
    return nom_prot_str, deg_prot_int


# Question 2.2.3
def get_ave_degree(file):
    """Calcul le degré moyen des protéines du graphe"""
    count_list = []
    for i in file.Sommet:
        count_list.append(get_degree(file, i))
    return sum(count_list)/len(file.Sommet)


# Question 2.2.4
def count_degree(file, deg_int):
    """Calcul le nombre de protéines étant du degré sélectionné"""
    count_int = 0
    for i in file.Sommet:
        if get_degree(file, i) == deg_int:
            count_int += 1
    return count_int


# Question 2.2.5
def histogram_degree(file, dmin, dmax):
    """Renvoie l'histgramme du nombre de protéine de certains degré suivant des bornes indiquées"""
    count_list = []
    for d in range(dmin, dmax + 1):
        count_list.append(count_degree(file, d))
    l = list(range(dmin, dmax + 1))
    for i in l:
        print(str(i) + " : " + "*" * count_list[i])
