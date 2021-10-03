import unittest
import sys
import pandas as pd

sys.path.append("../DM_Res_Bio/Partie_3")
from Chapitre_3 import Interactome


Human_HighQuality = pd.read_csv('../DM_Res_Bio/Human_HighQuality.txt', sep='\t', header=0,
                                 names=['Sommet', 'Interaction'])


class TestInteractome(unittest.TestCase, Interactome):

    def setUp(self):
        self.object = Interactome(Human_HighQuality)

    def test_density(self):
        self.assertTrue()

    def test_clustering(self):
        for i in range(100):
            self.assertGreaterEqual(self.object.clustering(list(self.object.int_dict.keys())[i]), 0,
                                    "Coefficient négatif")
        deg_int = 2*self.object.get_degree('1433B_HUMAN')
        count_int = 0
        for prot_arrete in self.object.int_dict.get('1433B_HUMAN'):
            count_int += self.object.get_degree(prot_arrete)
        coeff = deg_int / (count_int * (count_int - 1))
        self.assertTrue(self.object.clustering(list(self.object.int_dict.keys())[0]), coeff, "Mauvais coefficient")

