import sys
sys.path.append("../DM_Res_Bio/Partie_1")
from Chapitre_1 import *


# Question 2.1.1
def count_vertices(file):
    """
    Compte le nombre de sommet du graphe en se servant de sa représentation en dictionnaire
    :param file: tableau contenant un graphe
    :type file: dataframe
    :return: le nombre de sommets
    :rtype: int
    """
    graph_tuple = read_interaction_file_mat(file)
    return len(graph_tuple[1])


#  Question 2.1.2
def count_edges(file):
    """
    Compte le nombre d'arrêtes d'un graphe en se servant de sa représentation en dictionnaire
    :param file: tableau contenant un graphe
    :type file: dataframe
    :return: le nombre d'intéractions
    :rtype: int
    """
    graph_tuple = read_interaction_file_list(file)
    return len(graph_tuple)


# Question 2.1.3
def clean_interactome(filein, fileout):
    """
    permet de nettoyer tous les intéractions redondantes et tous les homo-dimères
    qui se trouve dans filein et stocke le résultat dans un fichier fileout
    :param filein: tableau contenant un graphe
    :type filein: dataframe
    :param fileout: nom du fichier qu'on veut créer
    :type fileout: str
    :return: none
    :rtype: none
    """
    list_graph = read_interaction_file_list(filein)
    list_graph = ["\t".join(map(str, elem)) for elem in list_graph]
    list_graph.insert(0,len(list_graph))
    with open(fileout, "w") as fichier:
        fichier.write("\n".join(map(str, list_graph)))


# Question 2.2.1
def get_degree(file, prot_str):
    """
    Calcul le nombre d'interaction de la protéine choisie
    :param file:
    :type file:
    :param prot_str:
    :type prot_str:
    :return:
    :rtype:
    """
    graph_tuple = read_interactions_file(file)
    if type(graph_tuple[0][prot_str]) == str:
        degree = 1
    else:
        degree = len(graph_tuple[0][prot_str])
    return degree


# Question 2.2.2
def get_max_degree(file):
    """
    Calcul le degré maximal obtenu par au moins une des protéines du graphe
    :param file:
    :type file:
    :return:
    :rtype:
    """
    count_list = []
    for i in file.Sommet:
        count_list.append(get_degree(file, i))
    indice_int = count_list.index(max(count_list))
    nom_prot_str = file.Sommet[indice_int]
    deg_prot_int = max(count_list)
    return nom_prot_str, deg_prot_int


# Question 2.2.3
def get_ave_degree(file):
    """
    Calcul le degré moyen des protéines du graphe
    :param file:
    :type file:
    :return:
    :rtype:
    """
    count_list = []
    for i in file.Sommet:
        count_list.append(get_degree(file, i))
    return sum(count_list)/len(file.Sommet)


# Question 2.2.4
def count_degree(file, deg_int):
    """
    Calcul le nombre de protéines étant du degré sélectionné
    :param file:
    :type file:
    :param deg_int:
    :type deg_int:
    :return:
    :rtype:
    """
    count_int = 0
    for i in file.Sommet:
        if get_degree(file, i) == deg_int:
            count_int += 1
    return count_int


# Question 2.2.5
def histogram_degree(file, dmin, dmax):
    """
    Renvoie l'histgramme du nombre de protéine de certains degré suivant des bornes indiquées
    :param file:
    :type file:
    :param dmin:
    :type dmin:
    :param dmax:
    :type dmax:
    """
    count_list = []
    for d in range(dmin, dmax + 1):
        count_list.append(count_degree(file, d))
    l = list(range(dmin, dmax + 1))
    for i in l:
        print(str(i) + " : " + "*" * count_list[i-dmin])
