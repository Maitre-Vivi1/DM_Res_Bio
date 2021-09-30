import pandas as pd
import numpy

Human_HighQuality = pd.read_csv('../DM_Res_Bio/Human_HighQuality.txt', sep='\t', header=0,
                                 names=['Sommet', 'Interaction'])


# Initialisation
"""
L'ensemble des fonctions du DM utilisent un DataFrame pandas afin de traiter au mieux les données. Les différents
fichiers d'interactions entre protéines doivent alors respecter certaines conditions résumées dans la fonction
is_interaction_file et testées dans le fichier test correspondant : tests_unitaires_Chapitre_1_fichier.py
"""


def flatten(d):
    """
    Permet de désemboiter des éléments tels que les listes ou les dictionnaires
    :param d:
    :type d: list
    :return:
    :rtype: list
    """
    v = [[i] if not isinstance(i, list) else flatten(i) for i in d]
    return [i for b in v for i in b]


# Question 1.2.1
def read_interaction_file_dict(file):
    """
    Renvoie le dictionnaire associé au graph d'intéraction entre protéines
    :param file: tableau contenant un graphe
    :type file: dataframe
    :return: un dictionnaire de ce graphe où chaque sommet est prise comme clé
    :rtype: dict
    """
    dico_dict = {}  # Initialisation du dictionnaire
    for a in range(0, len(file)):
        try:
            if len(dico_dict[file.Sommet[a]]) > 0:
                dico_dict[file.Sommet[a]] = flatten([dico_dict[file.Sommet[a]], file.Interaction[a]])
                pass
        except KeyError:
            dico_dict[file.Sommet[a]] = file.Interaction[a]
    return dico_dict

# autre Proposition
def read_interaction_file_dic(file):
    dico_dict = {}
    for i in range(len(file)):
        if file.Sommet[i] not in dico_dict.keys() and file.Interaction[i] not in dico_dict.keys():
            dico_dict[file.Sommet[i]] = [file.Interaction[i]]
            dico_dict[file.Interaction[i]] = [file.Sommet[i]]
        elif file.Sommet[i] in dico_dict.keys() and file.Interaction[i] not in dico_dict.keys():
            if file.Interaction[i] not in dico_dict[file.Sommet[i]]:
                dico_dict[file.Sommet[i]].append(file.Interaction[i])
            dico_dict[file.Interaction[i]] = [file.Sommet[i]]
        elif file.Interaction[i] in dico_dict.keys() and file.Sommet[i] not in dico_dict.keys():
            if file.Sommet[i] not in dico_dict[file.Interaction[i]]:
                dico_dict[file.Interaction[i]].append(file.Sommet[i])
            dico_dict[file.Sommet[i]] = [file.Interaction[i]]
        elif file.Interaction[i] in dico_dict.keys() and file.Sommet[i] in dico_dict.keys():
            if file.Sommet[i] not in dico_dict[file.Interaction[i]]:
                dico_dict[file.Interaction[i]].append(file.Sommet[i])
            if file.Interaction[i] not in dico_dict[file.Sommet[i]]:
                dico_dict[file.Sommet[i]].append(file.Interaction[i])
    return dico_dict


# Question 1.2.2
def read_interaction_file_list(file):
    """
    Renvoie la liste associée au graph d'intéraction entre protéines
    :param file: tableau contenant un graphe
    :type file: dataframe
    :return: une liste de graphe sans interaction en double
    :rtype: list
    """
    res_list = []
    for i in range(len(file)):
        res1 = [file.Sommet[i], file.Interaction[i]]
        res2 = [file.Interaction[i], file.Sommet[i]]
        if res1 not in res_list and res2 not in res_list:
            res_list.append(res1)
        pass
    return res_list


# Question 1.2.3
def read_interaction_file_mat(file):
    """
    Renvoie la matrice d'adjacence associée au graph d'intéraction entre protéines ainsi que la liste
    ordonnée des sommets
    :param file: tableau contenant un graphe
    :type file: dataframe
    :return: une matrice d'adjascence de ce graphe et une liste ordonnée des sommets
    :rtype: tuple
    """
    list_sommets = pd.concat([file.Sommet, file.Interaction])
    list_sommets = sorted(list(dict.fromkeys(list_sommets)))
    res_mat = numpy.zeros((len(list_sommets), len(list_sommets)), dtype=int)
    res_list = read_interaction_file_list(file)
    for interaction in res_list:
        res_mat[list_sommets.index(interaction[0])][list_sommets.index(interaction[1])] = 1
        res_mat[list_sommets.index(interaction[1])][list_sommets.index(interaction[0])] = 1
    return res_mat, list_sommets


# Question 1.2.4
def read_interactions_file(file):
    """
    Renvoie l'ensemble des méthodes utilisées pour décrire un graph
    :param file: tableau contenant un graphe
    :type file: dataframe
    :return: tuple contenant 3 structures de graphe(dictionnaire, liste, matrice) et une liste ordonnée des sommets
    :rtype:tuple
    """
    d_int = read_interaction_file_dict(file)
    l_int = read_interaction_file_list(file)
    mat = read_interaction_file_mat(file)
    m_int = mat[0]
    l_som = mat[1]
    return d_int, l_int, m_int, l_som


# Question 1.2.5
"""On pourrait se contenter de seulement le dictionnaire / la liste ou bien la matrice et sa liste de sommets
puisque ces objets caractérisent tous complétement le graphe d'intéraction"""


# Question 1.2.7
def is_interaction_file(file):
    """
    Permet de savoir si le fichier utilisé est au bon format
    Le format utilisé est un DataFrame pandas dont deux de ses colonnes
    s'appelent Sommet et Interaction
    :param file: tableau contenant un graphe
    :type file: dataframe
    :return: True si le fichier est au bon format, False sinon
    :rtype: bool
    """
    try:
        file_type_bool = str(type(file)) == "<class 'pandas.core.frame.DataFrame'>"
        file_columns_bool = 'Sommet' in file.columns and 'Interaction' in file.columns
        file_empty_bool = file.empty is False
        file_inter_egal_sommet_bool = len(file.Sommet) == len(file.Interaction)

        if file_type_bool and file_columns_bool and file_empty_bool and file_inter_egal_sommet_bool:
            return True
        else:
            return False
    except:
        return False
