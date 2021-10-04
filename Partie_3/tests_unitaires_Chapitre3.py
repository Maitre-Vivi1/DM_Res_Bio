import unittest
import sys
import pandas as pd

sys.path.append("../DM_Res_Bio/Partie_3")
from Chapitre_3 import Interactome


Human_HighQuality = pd.read_csv('../DM_Res_Bio/Human_HighQuality.txt', sep='\t', header=0,
                                 names=['Sommet', 'Interaction'])


class TestInteractome(unittest.TestCase, Interactome):

    def setUp(self):

        self.df = pd.DataFrame(
            {'Sommet': ["ZW10_HUMAN", "ZWINT_HUMAN", "ZY11B_HUMAN", "ZYX_HUMAN", "ZYX_HUMAN", "ZN384_HUMAN"],
             'Interaction': ["ZWINT_HUMAN", "ZW10_HUMAN", "ELOC_HUMAN", "NEBL_HUMAN", "ZN384_HUMAN", "ZYX_HUMAN"]})
        self.df = Interactome(self.df)
        self.object = Interactome(Human_HighQuality)

    def test_density(self):
        self.assertGreaterEqual(self.df.density(), 0, "La densité doit être positive")
        self.assertEqual(self.df.density(), 1/3, 'la densité calculée est fausse')

    def test_clustering(self):
        for i in range(100):
            self.assertGreaterEqual(self.object.clustering(list(self.object.int_dict.keys())[i]), 0,
                                    "Coefficient négatif")
        deg_int = 2*self.object.get_degree('1433B_HUMAN')
        count_int = 0
        for prot_arrete in self.object.int_dict.get('1433B_HUMAN'):
            count_int += self.object.get_degree(prot_arrete)
        coeff = deg_int / (count_int * (count_int - 1))
        self.assertEqual(self.object.clustering(list(self.object.int_dict.keys())[0]), coeff, "Mauvais coefficient")


if __name__ == '__Chapitre_3__':
    unittest.main()
