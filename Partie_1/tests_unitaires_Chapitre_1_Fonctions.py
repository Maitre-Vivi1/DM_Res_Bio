import sys
import unittest
import pandas as pd

sys.path.append("../DM_Res_Bio/Partie_1")
from Chapitre_1 import read_interaction_file_dict, read_interaction_file_list, read_interaction_file_mat, \
    read_interactions_file


class TestChapitre1Function(unittest.TestCase):

    def setUp(self):
        """Factorise les éléments utilisés pour les tests afin de ne pas se répéter"""
        self.df = pd.DataFrame(
            {'Sommet': ["ZW10_HUMAN", "ZWINT_HUMAN", "ZY11B_HUMAN", "ZYX_HUMAN", "ZYX_HUMAN", "ZN384_HUMAN"],
             'Interaction': ["ZWINT_HUMAN", "ZW10_HUMAN", "ELOC_HUMAN", "NEBL_HUMAN", "ZN384_HUMAN", "ZYX_HUMAN"]})
        self.interaction_dict = read_interaction_file_dict(self.df)
        self.interaction_list = read_interaction_file_list(self.df)
        self.interaction_mat = read_interaction_file_mat(self.df)
        self.interaction_all = read_interactions_file(self.df)

    def test_read_interaction_file_dict(self):
        """Test si le dictionnaire renvoyé est le même que celui attendu"""
        dico_dict = read_interaction_file_dict(self.df)
        expected_dict = {'ZW10_HUMAN': ['ZWINT_HUMAN'], 'ZWINT_HUMAN': ['ZW10_HUMAN'],
                         'ZY11B_HUMAN': ['ELOC_HUMAN'], 'ELOC_HUMAN': ['ZY11B_HUMAN'],
                         'ZYX_HUMAN': ['NEBL_HUMAN', 'ZN384_HUMAN'],
                         'NEBL_HUMAN': ['ZYX_HUMAN'], 'ZN384_HUMAN': ['ZYX_HUMAN']}
        self.assertTrue((dico_dict == expected_dict),
                        "Le dictionnaire doit contenir tout les sommets et leurs voisins")

    def test_read_interaction_file_list(self):
        """Test si la même relation est présente dans la liste"""
        self.assertTrue(4 == len(self.interaction_list),
                        "Il y a des doublons dans la liste")

    def test_read_interaction_file_mat(self):
        """Test la bonne taille de la matrice d'adjacence"""
        list_sommets = pd.concat([self.df.Sommet, self.df.Interaction])
        list_sommets = sorted(list(dict.fromkeys(list_sommets)))
        self.assertTrue(len(self.interaction_mat[0]) == len(list_sommets),
                        "Le nombre de lignes dans la matrice ne correspond pas au nombre de sommets")
        self.assertTrue(len(self.interaction_mat[0][0]) == len(list_sommets),
                        "Le nombre de colonnes dans la matrice ne correspond pas au nombre de sommets")

    def test_read_interaction_file(self):
        """Test si toutes les sorties prévues sont bien renvoyées"""
        self.assertTrue(len(self.interaction_all) == 4,
                        "On doit renvoyer 4 éléments")


if __name__ == '__Chapitre_1__':
    unittest.main()
