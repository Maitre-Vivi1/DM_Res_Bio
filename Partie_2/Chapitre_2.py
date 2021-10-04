import sys
sys.path.append("../DM_Res_Bio/Partie_1")
from Chapitre_1 import *


# Question 2.1.1
def count_vertices(file):
    """
    Compte le nombre de sommets du graphe
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
    Compte le nombre d'arrêtes d'un graphe en se servant de sa représentation en liste
    :param file: tableau contenant un graphe
    :type file: dataframe
    :return: le nombre d'intéractions
    :rtype: int
    """
    graph_list = read_interaction_file_list(file)
    return len(graph_list)


# Question 2.1.3
def clean_interactome(filein, fileout):
    """
    permet de nettoyer tous les intéractions redondantes et tous les homo-dimères
    qui se trouve dans filein et stocke le résultat dans un fichier fileout
    :param filein: tableau contenant un graphe
    :type filein: dataframe
    :param fileout: nom du fichier qu'on veut créer avec l'extension .txt
    :type fileout: str
    :return: none
    :rtype: none
    """
    graph_list = read_interaction_file_list(filein)
    graph_list = ["\t".join(map(str, elem)) for elem in graph_list]
    graph_list.insert(0, len(graph_list))
    with open(fileout, "w") as fichier:
        fichier.write("\n".join(map(str, graph_list)))


# Question 2.2.1
def get_degree(file, prot_str):
    """
    Calcul le nombre d'interaction de la protéine choisie
    :param file: tableau contenant un graphe
    :type file: dataframe
    :param prot_str: le nom de la protéine
    :type prot_str: str
    :return: nombre d'intéraction de la protéine choisie
    :rtype: int
    """
    try:
        graph_dict = read_interaction_file_dict(file)
        degree = len(graph_dict[prot_str])
    except KeyError:
        return f"Erreur : La protéine {prot_str} n'existe pas dans ce graphe"
    return degree


# Question 2.2.2
def get_max_degree(file):
    """
    Calcul le degré maximal obtenu par au moins une des protéines du graphe
    :param file: tableau contenant un graphe
    :type file: dataframe
    :return: nom de la protéine de dégré maximal et son degré
    :rtype: tuple
    """
    graph_dict = read_interaction_file_dict(file)
    deg_list = [len(degre) for degre in graph_dict.values()]
    deg_prot_int = max(deg_list)
    nom_prot_str = list(graph_dict.keys())[deg_list.index(deg_prot_int)]
    return nom_prot_str, deg_prot_int


# Question 2.2.3
def get_ave_degree(file):
    """
    Calcul le degré moyen des protéines du graphe
    :param file: tableau contenant un graphe
    :type file: dataframe
    :return: le degré moyen des protéines du graphe
    :rtype: int
    """
    graph_dict = read_interaction_file_dict(file)
    deg_list = [len(degre) for degre in graph_dict.values()]
    no_duplicated_sort_list = sorted(list(dict.fromkeys(deg_list)))
    index_int = (len(no_duplicated_sort_list)//2) \
        if isinstance(len(no_duplicated_sort_list)/2, float) \
        else len(no_duplicated_sort_list)/2  # dans ce cas devrait-on prendre l'inf ou le sup?
    deg_ave_int = no_duplicated_sort_list[index_int]
    return deg_ave_int


# Question 2.2.4
def count_degree(file, deg_int):
    """
    Calcul le nombre de protéines correspondant au degré sélectionné
    :param file: tableau contenant un graphe
    :type file: dataframe
    :param deg_int: un degré quelconque d'une protéine
    :type deg_int: int
    :return: nombre de protéines qui ont un degré égal à deg_int
    :rtype: int
    """
    graph_dict = read_interaction_file_dict(file)
    deg_list = [len(degre) for degre in graph_dict.values()]
    count_int = deg_list.count(deg_int)
    return count_int


# Question 2.2.5
def histogram_degree(file, dmin, dmax):
    """
    Renvoie l'histgramme du nombre de protéine de certains degré suivant des bornes indiquées
    :param file: tableau contenant un graphe
    :type file: dataframe
    :param dmin: degré minimal
    :type dmin: int
    :param dmax: degré maximal
    :type dmax: int
    :return: none
    :rtype:none
    """
    graph_dict = read_interaction_file_dict(file)
    deg_list = [len(degre) for degre in graph_dict.values()]
    for degre in range(dmin, dmax + 1):
        print(str(degre) + " : " + "*" * deg_list.count(degre))


# Commentaire : D'après la distribution de Human_HighQuality plus le degré augmente,
#               plus le nombre de protéine diminue. Nous avons donc plus d'intéractions une à une.
