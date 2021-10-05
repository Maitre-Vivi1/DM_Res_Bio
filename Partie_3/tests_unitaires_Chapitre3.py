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
