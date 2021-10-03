import sys
import numpy
import pandas as pd
sys.path.append("../DM_Res_Bio/Partie_2")
from Chapitre_2 import *


# Question 3.1.1
# On lit le fichier dmax - dmin + 1 fois lors de l'execution de la fonction histogram_degree.


# Question 3.2.2


class Interactome():
    def __init__(self, file):
        self.file = file
        self.int_list = self.read_interaction_file_list()
        self.int_dict = self.read_interaction_file_dict()
        self.proteins = self.read_interaction_file_mat()

    def read_interaction_file_dict(self):
        """
        Renvoie le dictionnaire associé au graphe d'intéraction entre protéines
        :return: un dictionnaire de ce graphe où chaque sommet est prise comme clé
        :rtype: dict
        """
        dico_dict = {}
        for i in range(len(self.file)):
            if self.file.Sommet[i] not in dico_dict.keys() and self.file.Interaction[i] not in dico_dict.keys():
                dico_dict[self.file.Sommet[i]] = [self.file.Interaction[i]]
                dico_dict[self.file.Interaction[i]] = [self.file.Sommet[i]]
            elif self.file.Sommet[i] in dico_dict.keys() and self.file.Interaction[i] not in dico_dict.keys():
                if self.file.Interaction[i] not in dico_dict[self.file.Sommet[i]]:
                    dico_dict[self.file.Sommet[i]].append(self.file.Interaction[i])
                dico_dict[self.file.Interaction[i]] = [self.file.Sommet[i]]
            elif self.file.Interaction[i] in dico_dict.keys() and self.file.Sommet[i] not in dico_dict.keys():
                if self.file.Sommet[i] not in dico_dict[self.file.Interaction[i]]:
                    dico_dict[self.file.Interaction[i]].append(self.file.Sommet[i])
                dico_dict[self.file.Sommet[i]] = [self.file.Interaction[i]]
            elif self.file.Interaction[i] in dico_dict.keys() and self.file.Sommet[i] in dico_dict.keys():
                if self.file.Sommet[i] not in dico_dict[self.file.Interaction[i]]:
                    dico_dict[self.file.Interaction[i]].append(self.file.Sommet[i])
                if self.file.Interaction[i] not in dico_dict[self.file.Sommet[i]]:
                    dico_dict[self.file.Sommet[i]].append(self.file.Interaction[i])
        return dico_dict

    def read_interaction_file_list(self):
        res_list = []
        for i in range(len(self.file)):
            res1 = [self.file.Sommet[i], self.file.Interaction[i]]
            res2 = [self.file.Interaction[i], self.file.Sommet[i]]
            if res1 not in res_list and res2 not in res_list:
                res_list.append(res1)
            pass
        return res_list

    def read_interaction_file_mat(self):
        list_sommets = pd.concat([self.file.Sommet, self.file.Interaction])
        list_sommets = sorted(list(dict.fromkeys(list_sommets)))
        res_mat = numpy.zeros((len(list_sommets), len(list_sommets)), dtype=int)
        for interaction in self.int_list:
            res_mat[list_sommets.index(interaction[0])][list_sommets.index(interaction[1])] = 1
            res_mat[list_sommets.index(interaction[1])][list_sommets.index(interaction[0])] = 1
        return res_mat, list_sommets

    def read_interactions_file(self):
        """
        Renvoie l'ensemble des méthodes utilisées pour décrire un graph
        :return: tuple contenant 3 structures de graphe(dictionnaire, liste, matrice) et une liste ordonnée des sommets
        :rtype:tuple
        """
        m_int = self.proteins[0]
        l_som = self.proteins[1]
        return self.int_dict, self.int_list, m_int, l_som

    def is_interaction_file(self):
        """
        Permet de savoir si le fichier utilisé est au bon format
        Le format utilisé est un DataFrame pandas dont deux de ses colonnes
        s'appelent Sommet et Interaction
        :return: True si le fichier est au bon format, False sinon
        :rtype: bool
        """
        try:
            file_type_bool = str(type(self.file)) == "<class 'pandas.core.frame.DataFrame'>"
            file_columns_bool = 'Sommet' in self.file.columns and 'Interaction' in self.file.columns
            file_empty_bool = self.file.empty is False
            file_inter_egal_sommet_bool = len(self.file.Sommet) == len(self.file.Interaction)

            if file_type_bool and file_columns_bool and file_empty_bool and file_inter_egal_sommet_bool:
                return True
            else:
                return False
        except:
            return False

    def count_vertices(self):
        """
        Compte le nombre de sommet du graphe en se servant de sa représentation en dictionnaire
        :return: le nombre de sommets
        :rtype: int
        """
        return len(self.proteins[1])

    def count_edges(self):
        """
        Compte le nombre d'arrêtes d'un graphe en se servant de sa représentation en dictionnaire
        :return: le nombre d'intéractions
        :rtype: int
        """
        return len(self.int_list)

    def clean_interactome(self, fileout):
        """
        permet de nettoyer tous les intéractions redondantes et tous les homo-dimères
        qui se trouve dans filein et stocke le résultat dans un fichier fileout
        :return: none
        :rtype: none
        """
        list_graph = self.int_list
        list_graph = ["\t".join(map(str, elem)) for elem in list_graph]
        list_graph.insert(0,len(list_graph))
        with open(fileout, "w") as fichier:
            fichier.write("\n".join(map(str, list_graph)))

    def get_degree(self, prot_str):
        """
        Calcul le nombre d'interaction de la protéine choisie
        :param prot_str:
        :type prot_str:
        :return:
        :rtype:
        """
        if type(self.int_dict[prot_str]) == str:
            degree = 1
        else:
            degree = len(self.int_dict[prot_str])
        return degree

    def get_max_degree(self):
        """
        Calcul le degré maximal obtenu par au moins une des protéines du graphe
        :return:
        :rtype:
        """
        count_list = []
        for i in self.file.Sommet:
            count_list.append(self.get_degree(i))
        indice_int = count_list.index(max(count_list))
        nom_prot_str = self.file.Sommet[indice_int]
        deg_prot_int = max(count_list)
        return nom_prot_str, deg_prot_int

    def get_ave_degree(self):
        """
        Calcul le degré moyen des protéines du graphe
        :return:
        :rtype:
        """
        count_list = []
        for i in self.file.Sommet:
            count_list.append(self.get_degree(i))
        return sum(count_list)/len(self.file.Sommet)

    def count_degree(self, deg_int):
        """
        Calcul le nombre de protéines étant du degré sélectionné
        :param deg_int:
        :type deg_int:
        :return:
        :rtype:
        """
        count_int = 0
        for i in self.file.Sommet:
            if self.get_degree(i) == deg_int:
                count_int += 1
        return count_int

    def histogram_degree(self, dmin, dmax):
        """
        Renvoie l'histgramme du nombre de protéine de certains degré suivant des bornes indiquées
        :param dmin:
        :type dmin:
        :param dmax:
        :type dmax:
        """
        count_list = []
        for d in range(dmin, dmax + 1):
            count_list.append(self.count_degree(d))
        l = list(range(dmin, dmax + 1))
        for i in l:
            print(str(i) + " : " + "*" * count_list[i-dmin])

    def density(self):
        D = 2 * len(self.int_dict.keys()) / (len(self.int_dict.values()) * (len(self.int_dict.values()) -1))
        return D

    def clustering(self, prot):
        count_int = 0
        for prot_arrete in self.int_dict.get(prot):
            count_int += self.get_degree(prot_arrete)
        if count_int in [0,1]:
            coeff = 0
        else:
            coeff = 2*self.get_degree(prot) / (count_int * (count_int - 1))
        return coeff
