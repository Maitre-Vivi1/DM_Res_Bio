import pandas as pd
import numpy
from itertools import combinations
from collections import Counter
from itertools import repeat

# Question 3.1.1
# On lit le fichier dmax - dmin + 1 fois lors de l'execution de la fonction histogram_degree.

class Structure:
    def __init__(self, file):
        """
        Constructeur d'un graphe
        :param file: nom du fichier avec son extension
        :type file: str
        """
        self.graph_data = pd.read_csv('../DM_Res_Bio/' + str(file), sep='\t', header=0,
                                     names=['Sommet', 'Interaction'])

    def read_interaction_file_dict(self):
        """
        Renvoie le dictionnaire associé au graphe d'intéraction entre protéines
        :return: un dictionnaire de ce graphe où chaque sommet est prise comme clé
        :rtype: dict
        """
        dico_dict = {}
        for i in range(len(self.graph_data)):
            if self.graph_data.Sommet[i] not in dico_dict.keys() and self.graph_data.Interaction[i] not in dico_dict.keys():
                dico_dict[self.graph_data.Sommet[i]] = [self.graph_data.Interaction[i]]
                dico_dict[self.graph_data.Interaction[i]] = [self.graph_data.Sommet[i]]
            elif self.graph_data.Sommet[i] in dico_dict.keys() and self.graph_data.Interaction[i] not in dico_dict.keys():
                if self.graph_data.Interaction[i] not in dico_dict[self.graph_data.Sommet[i]]:
                    dico_dict[self.graph_data.Sommet[i]].append(self.graph_data.Interaction[i])
                dico_dict[self.graph_data.Interaction[i]] = [self.graph_data.Sommet[i]]
            elif self.graph_data.Interaction[i] in dico_dict.keys() and self.graph_data.Sommet[i] not in dico_dict.keys():
                if self.graph_data.Sommet[i] not in dico_dict[self.graph_data.Interaction[i]]:
                    dico_dict[self.graph_data.Interaction[i]].append(self.graph_data.Sommet[i])
                dico_dict[self.graph_data.Sommet[i]] = [self.graph_data.Interaction[i]]
            elif self.graph_data.Interaction[i] in dico_dict.keys() and self.graph_data.Sommet[i] in dico_dict.keys():
                if self.graph_data.Sommet[i] not in dico_dict[self.graph_data.Interaction[i]]:
                    dico_dict[self.graph_data.Interaction[i]].append(self.graph_data.Sommet[i])
                if self.graph_data.Interaction[i] not in dico_dict[self.graph_data.Sommet[i]]:
                    dico_dict[self.graph_data.Sommet[i]].append(self.graph_data.Interaction[i])
        return dico_dict


    def read_interaction_file_list(self):
        """
        Renvoie la liste associée au graph d'intéraction entre protéines
        :return: une liste de graphe sans interaction en double
        :rtype: list
        """
        res_list = []
        for i in range(len(self.graph_data)):
            res1 = [self.graph_data.Sommet[i], self.graph_data.Interaction[i]]
            res2 = [self.graph_data.Interaction[i], self.graph_data.Sommet[i]]
            if res1 not in res_list and res2 not in res_list:
                res_list.append(res1)
            pass
        return res_list


    def read_interaction_file_mat(self):
        """
        Renvoie la matrice d'adjacence associée au graph d'intéraction entre protéines ainsi que la liste
        ordonnée des sommets
        :return: une matrice d'adjascence de ce graphe et une liste ordonnée des sommets
        :rtype: tuple
        """
        list_sommets = pd.concat([self.graph_data.Sommet, self.graph_data.Interaction])
        list_sommets = sorted(list(dict.fromkeys(list_sommets)))
        res_mat = numpy.zeros((len(list_sommets), len(list_sommets)), dtype=int)
        res_list = self.read_interaction_file_list()
        for interaction in res_list:
            res_mat[list_sommets.index(interaction[0])][list_sommets.index(interaction[1])] = 1
            res_mat[list_sommets.index(interaction[1])][list_sommets.index(interaction[0])] = 1
        return res_mat, list_sommets



class Interactome(Structure):
    def __init__(self, file):
        """
        Constructeur de l'interactome
        :param file: nom du fichier avec son extension
        :type file: str
        """
        super().__init__(file)
        self.int_list = super().read_interaction_file_list()
        self.int_dict = super().read_interaction_file_dict()
        self.int_mat_tuple = super().read_interaction_file_mat() # matrice et liste des sommets ordonnés
        self.int_mat = self.int_mat_tuple[0]
        self.proteins = self.int_mat_tuple[1]


    def count_vertices(self):
        """
        Compte le nombre de sommet du graphe
        :return: le nombre de sommets
        :rtype: int
        """
        return len(self.proteins)


    def count_edges(self):
        """
        Compte le nombre d'arrêtes d'un graphe en se servant de sa représentation en liste
        :return: le nombre d'intéractions
        :rtype: int
        """
        return len(self.int_list)


    def clean_interactome(self, fileout):
        """
        permet de nettoyer tous les intéractions redondantes et tous les homo-dimères
        qui se trouve dans le fichier de départ et stocke le résultat dans un fichier fileout
        :param fileout: nom du fichier qu'on veut créer avec son extension
        :type fileout: str
        :return: none
        :rtype: none
        """
        graph_list = ["\t".join(map(str, elem)) for elem in self.int_list]
        graph_list.insert(0, str(len(graph_list)))
        with open(fileout, "w") as fichier:
            fichier.write("\n".join(map(str, graph_list)))


    def get_degree(self, prot):
        """
        Calcul le nombre d'interaction de la protéine choisie
        :param prot: le nom de la protéine
        :type prot: str
        :return: nombre d'intéraction de la protéine choisie
        :rtype: int
        """
        try:
            degree_int = len(self.int_dict[prot])
        except KeyError:
            return f"Erreur : La protéine {prot} n'existe pas dans ce graphe"
        return degree_int


    def get_max_degree(self):
        """
        Calcul le degré maximal obtenu par au moins une des protéines du graphe
        :return: nom de la protéine de dégré maximal et son degré
        :rtype: tuple
        """
        deg_list = [len(degre) for degre in self.int_dict.values()]
        deg_prot_int = max(deg_list)
        nom_prot_str = list(self.int_dict.keys())[deg_list.index(deg_prot_int)]
        return nom_prot_str, deg_prot_int


    def get_ave_degree(self):
        """
        Calcul le degré moyen des protéines du graphe
        :return: le degré moyen des protéines du graphe
        :rtype: int
        """
        deg_list = [len(degre) for degre in self.int_dict.values()]
        deg_ave_int = sum(deg_list)/len(deg_list)
        return round(deg_ave_int)


    def count_degree(self, deg_int):
        """
        Calcul le nombre de protéines correspondant au degré sélectionné
        :param deg_int: un degré quelconque d'une protéine
        :type deg_int: int
        :return: nombre de protéines qui ont un degré égal à deg_int
        :rtype: int
        """
        deg_list = [len(degre) for degre in self.int_dict.values()]
        count_int = deg_list.count(deg_int)
        return count_int


    def histogram_degree(self, dmin, dmax):
        """
        Renvoie l'histgramme du nombre de protéine de certains degré suivant des bornes indiquées
        :param dmin: degré minimal
        :type dmin: int
        :param dmax: degré maximal
        :type dmax: int
        :return: None
        :rtype:None
        """
        deg_list = [len(degre) for degre in self.int_dict.values()]
        for degre in range(dmin, dmax + 1):
            print(str(degre) + " : " + "*" * deg_list.count(degre))


    def density(self):
        """
        Calcule la densité d'un graphe non orienté G=(V,E)
        :return: densité du graphe
        :rtype: float
        """
        vertices_int = self.count_vertices()
        edges_int = self.count_edges()
        density_float = (2*edges_int)/(vertices_int*(vertices_int-1))
        return density_float


    def clustering(self, prot):
        """
        Permet de calculer le coefficient de clustering d'un graphe
        :param prot: nom de protéine du graphe
        :type prot: str
        :return: coefficient de clustering du sommet <prot>
        :rtype: float
        """
        try:
            degre_int = self.get_degree(prot)
            if degre_int <= 1:
                coef_float = 0
            else:
                interact_list = self.int_dict[prot]
                triangle_list = []
                for i in range(len(interact_list)):
                    for elem in interact_list:
                        if elem in self.int_dict[interact_list[i]] and \
                                (elem, interact_list[i]) not in triangle_list and \
                                (interact_list[i], elem) not in triangle_list:
                            triangle_list.append((elem, interact_list[i]))
                pairs_int = [i for i in combinations(range(degre_int), 2)]
                coef_float = len(triangle_list)/len(pairs_int)
        except KeyError:
            return f"Erreur : La protéine {prot} n'existe pas dans ce graphe"
        return coef_float

    def compute_cc(self):
        """
        renvoie une liste lcc dont chaque élément lcc[i] correspond au numéro de composante connexe
        de la protéine à la position i dans la liste des protéines du graphe (attribut de la classe)
        :return: liste de numero de composante connexe
        :rtype: list
        """
        num_prot_list = list(range(len(self.proteins)))
        modifications = True
        while modifications:
            modifications = False
            for i in range(len(self.proteins)):
                for j in range(i + 1, len(self.proteins)):
                    if self.int_mat[i, j] == 1 and num_prot_list[i] != num_prot_list[j]:
                        num_prot_list[i] = num_prot_list[j] = min(num_prot_list[i], num_prot_list[j])
                        modifications = True
        return num_prot_list

    def count_cc(self):
        """
        calcule le nombre de composantes connexes d’un graphe, et donne pour chacune d’elle sa taille
        (c’est à dire son nombre de protéines)
        :return: le nombre de composantes connexes et un dictionnaire de composantes connexes et leurs tailles
        :rtype: tuple
        """
        cc_dict = dict(Counter(self.compute_cc()))
        return len(cc_dict), cc_dict

    def write_cc(self):
        """
        Ecrit dans un fichier les différentes composantes connexes d’un graphe selon le format suivant:
        - une ligne par composante connexe
        - le premier élément de la ligne est la taille de la composante connexe,
        - ensuite vous ajouterez la liste des sommets qui composent cette composante connexe.
        """
        cc_index_list = {}
        for i, c in enumerate(self.compute_cc()):
            if c not in cc_index_list:
                cc_index_list[c] = []
            cc_index_list[c].append(i)
        cc_name_list = [[self.proteins[indice] for indice in num_prot] for num_prot in cc_index_list.values()]
        cc_graph_list = [[len(elem), elem] for elem in cc_name_list]
        graph_list = ["\t".join(map(str, elem)) for elem in cc_graph_list]
        with open("connex_components.txt", "w") as fichier:
            fichier.write("\n".join(map(str, graph_list)))

    def extract_cc(self, prot):
        """
        permet de calculer toutes les sommets de la composante connexe de prot
        :param prot: nom du protéine dont on  veut extraire les sommets correspondants
        :type prot: str
        :return: liste de protéines appartenant à une même composante connexe
        :rtype: list
        """
        cc_index_list = {}
        for i, c in enumerate(self.compute_cc()):
            if c not in cc_index_list:
                cc_index_list[c] = []
            cc_index_list[c].append(i)
        cc_name_list = [[self.proteins[indice] for indice in num_prot] for num_prot in cc_index_list.values()]
        return [prot_list for prot_list in cc_name_list if prot in prot_list][0]


