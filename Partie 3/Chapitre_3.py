import sys
sys.path.append("../DM_Res_Bio/Partie_2")
from Chapitre_2 import *


class Interactome:

    def __init__(self, file):
        self.int_list = []
        self.int_dict = {}
        self.proteins = []

    def read_interaction_file_dict(file):
        dico_dict = {}  # Initialisation du dictionnaire
        for a in range(0, len(file)):
            try:
                if len(dico_dict[file.Sommet[a]]) > 0:
                    dico_dict[file.Sommet[a]] = flatten([dico_dict[file.Sommet[a]], file.Interaction[a]])
                    pass
            except KeyError:
                dico_dict[file.Sommet[a]] = file.Interaction[a]
        return dico_dict

    def read_interaction_file_list(file):
        res_list = []
        for i in range(len(file)):
            res1 = [file.Sommet[i], file.Interaction[i]]
            res2 = [file.Interaction[i], file.Sommet[i]]
            if res1 not in res_list and res2 not in res_list:
                res_list.append(res1)
            pass
        return res_list

    def read_interaction_file_mat(file):
        list_sommets = pd.concat([file.Sommet, file.Interaction])
        list_sommets = sorted(list(dict.fromkeys(list_sommets)))
        res_mat = numpy.zeros((len(list_sommets), len(list_sommets)), dtype=int)
        res_list = read_interaction_file_list(file)
        for interaction in res_list:
            res_mat[list_sommets.index(interaction[0])][list_sommets.index(interaction[1])] = 1
            res_mat[list_sommets.index(interaction[1])][list_sommets.index(interaction[0])] = 1
        return res_mat, list_sommets

    def read_interactions_file(file):
        d_int = read_interaction_file_dict(file)
        l_int = read_interaction_file_list(file)
        mat = read_interaction_file_mat(file)
        m_int = mat[0]
        l_som = mat[1]
        return d_int, l_int, m_int, l_som

    def is_interaction_file(file):
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

    def count_vertices(file):
        graph_tuple = read_interaction_file_mat(file)
        return len(graph_tuple[1])

    def count_edges(file):
        graph_tuple = read_interaction_file_list(file)
        return len(graph_tuple)

    def clean_interactome(filein, fileout):
        list_graph = read_interaction_file_list(filein)
        list_graph = ["\t".join(map(str, elem)) for elem in list_graph]
        list_graph.insert(0, len(list_graph))
        with open(fileout, "w") as fichier:
            fichier.write("\n".join(map(str, list_graph)))

    def get_degree(file, prot_str):
        graph_tuple = read_interactions_file(file)
        if type(graph_tuple[0][prot_str]) == str:
            degree = 1
        else:
            degree = len(graph_tuple[0][prot_str])
        return degree

    def get_max_degree(file):
        count_list = []
        for i in file.Sommet:
            count_list.append(get_degree(file, i))
        indice_int = count_list.index(max(count_list))
        nom_prot_str = file.Sommet[indice_int]
        deg_prot_int = max(count_list)
        return nom_prot_str, deg_prot_int

    def get_ave_degree(file):
        count_list = []
        for i in file.Sommet:
            count_list.append(get_degree(file, i))
        return sum(count_list) / len(file.Sommet)

    def count_degree(file, deg_int):
        count_int = 0
        for i in file.Sommet:
            if get_degree(file, i) == deg_int:
                count_int += 1
        return count_int

    def histogram_degree(file, dmin, dmax):
        count_list = []
        for d in range(dmin, dmax + 1):
            count_list.append(count_degree(file, d))
        l = list(range(dmin, dmax + 1))
        for i in l:
            print(str(i) + " : " + "*" * count_list[i])