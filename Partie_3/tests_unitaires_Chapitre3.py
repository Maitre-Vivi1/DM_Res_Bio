import unittest
import sys
#import pandas as pd

sys.path.append("../DM_Res_Bio/Partie_3")
from Chapitre_3 import Interactome


class TestInteractome(unittest.TestCase, Interactome):

    def setUp(self):
        self.df = Interactome("df_test.txt")

    def test_density(self):
        self.assertGreaterEqual(self.df.density(), 0, "La densité doit être positive")
        self.assertEqual(self.df.density(), 16/72, 'la densité calculée est fausse')

    def test_clustering(self):
        self.assertGreaterEqual(self.df.clustering("ZN384_HUMAN"), 0, "Le coefficient doit être positive")
        self.assertEqual(self.df.clustering("ZYX_HUMAN"), 2/6, 'la densité calculée est fausse')

    def test_count_cc(self):
        self.assertEqual(self.df.count_cc()[0], 3, "Pas le bon nbre de classes connexes")
    
    def test_compute_cc(self):
        self.assertEqual(len(self.df.compute_cc()), 9, "Tous les sommets sont représentés")
        
    def test_extract_cc(self):
        self.assertEqual(self.df.extract_cc("ZW10_HUMAN"),
                         ['1433B_HUMAN', 'BAD_HUMAN', 'NEBL_HUMAN', 'ZN384_HUMAN', 'ZYX_HUMAN'],
                         "Bonne classe convexe")
