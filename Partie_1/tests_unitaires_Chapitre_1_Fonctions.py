import sys
import unittest
import pandas as pd

sys.path.append("../DM_Res_Bio/Partie_1")
from Chapitre_1 import flatten, read_interaction_file_dict, read_interaction_file_list, read_interaction_file_mat, \
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
        """Test si le dictionnaire renvoyé contient le bon nombre d'intéractions"""
        self.assertTrue(len(self.df) == len(flatten(self.interaction_dict.values())),
                        "autant d'intéractions que de valeurs dans le dictionnaire")

    def test_read_interaction_file_list(self):
        """Test si la même relation est présente dans la liste"""
        self.assertTrue(4 == len(self.interaction_list),
                        "Pas de doublon dans la liste")

    def test_read_interaction_file_mat(self):
        """Test la bonne taille de la matrice d'adjacence"""
        list_sommets = pd.concat([self.df.Sommet, self.df.Interaction])
        list_sommets = sorted(list(dict.fromkeys(list_sommets)))
        self.assertTrue(len(self.interaction_mat[0]) == len(list_sommets),
                        "Autant de lignes dans la matrice que de sommets")
        self.assertTrue(len(self.interaction_mat[0][0]) == len(list_sommets),
                        "Autant de colonnes dans la matrice que de sommets")

    def test_read_interaction_file(self):
        """Test si toutes les sorties prévues sont bien renvoyées"""
        self.assertTrue(len(self.interaction_all) == 4,
                        "On renvoie bien 4 éléments")


if __name__ == '__Chapitre_1__':
    unittest.main()
