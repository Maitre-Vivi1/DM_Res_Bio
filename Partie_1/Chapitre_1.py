# Travail avec un fichier tabulé / DataFrame
import pandas as pd
# Pour l'écriture du graph d'intéractions
import numpy
# Question 2.1

# On charge le fichier correspondant au travail demandé dans l'environnement de travail en précisant
# le nom des deux colonnes

# Human_HighQuality = pd.read_csv('../DM_Res_Bio/Human_HighQuality.txt', sep='\t', header=0,
#                                  names=['Sommet', 'Interaction'])


# fonction utilisée afin de délister les éléments
def flatten(d):
    v = [[i] if not isinstance(i, list) else flatten(i) for i in d]
    return [i for b in v for i in b]


# Construction de la fonction permettant de décrire les intéractions entre protéines
def read_interaction_file_dict(nom_fichier):
    dico = {}  # Initialisation du dictionnaire
    for a in range(0, len(nom_fichier)):
        try:
            if len(dico[nom_fichier.Sommet[a]]) > 0:
                dico[nom_fichier.Sommet[a]] = flatten([dico[nom_fichier.Sommet[a]], nom_fichier.Interaction[a]])
                pass
        except KeyError:
            dico[nom_fichier.Sommet[a]] = nom_fichier.Interaction[a]
    return dico


# read_interaction_file_dict(Human_HighQuality)


def read_interaction_file_list(data):
    res_list = []
    for i in range(len(data)):
        res1 = [data.Sommet[i], data.Interaction[i]]
        res2 = [data.Interaction[i], data.Sommet[i]]
        if res1 not in res_list and res2 not in res_list:
            res_list.append(res1)
        pass
    return res_list


# read_interaction_file_list(Human_HighQuality)


# TODO : Trop long :O
# Question 1.2.3 structure 3
def read_interaction_file_mat(data):
    list_sommets = pd.concat([data.Sommet, data.Interaction])
    list_sommets = sorted(list(dict.fromkeys(list_sommets)))
    res_mat = pd.DataFrame(numpy.zeros((len(list_sommets), len(list_sommets)), dtype=int),
                           index=list_sommets, columns=list_sommets)
    res_list = []
    for i in range(len(data)):
        res = [data.Sommet[i], data.Interaction[i]]
        res_list.append(res)
    for sommet1 in list_sommets:
        for sommet2 in list_sommets[list_sommets.index(sommet1)+1:]:
            if [sommet1, sommet2] in res_list or [sommet2, sommet1] in res_list:
                res_mat.loc[sommet1][sommet2] = 1
                res_mat.loc[sommet2][sommet1] = 1
    return res_mat, list_sommets




# read_interaction_file_mat(Human_HighQuality)


# Question 2.4

def read_interactions_file(nom_fichier):
    d_int = read_interaction_file_dict(nom_fichier)
    l_int = read_interaction_file_list(nom_fichier)
    mat = read_interaction_file_mat(nom_fichier)
    m_int = mat[0]
    l_som = mat[1]
    return d_int, l_int, m_int, l_som


# Question 2.5

# On pourrait se contenter de seulement le disctionnaire / la liste ou bien la matrice et sa liste de sommets
# puisque ces objets caractérisent tous complétement le graphe d'intéraction


# Question 2.7
def is_interaction_file(nom_fichier):
    try:
        file_type = str(type(nom_fichier)) == "<class 'pandas.core.frame.DataFrame'>"
        file_columns = 'Sommet' in nom_fichier.columns and 'Interaction' in nom_fichier.columns
        file_empty = nom_fichier.empty is False
        file_inter_egal_sommet = len(nom_fichier.Sommet) == len(nom_fichier.Interaction)

        if file_type and file_columns and file_empty and file_inter_egal_sommet:
            return True
        else:
            return False
    except:
        return False
