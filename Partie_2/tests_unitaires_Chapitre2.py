import unittest
import sys
import pandas as pd

sys.path.append("../DM_Res_Bio/Partie_2")
from Chapitre_2 import count_vertices, count_edges, get_degree, get_max_degree, get_ave_degree, count_degree, \
    histogram_degree


class TestFunction(unittest.TestCase):

    def setUp(self):
        """Factorise les éléments utilisés pour les tests afin de ne pas se répéter"""
        self.df = pd.DataFrame(
            {'Sommet': ["ZW10_HUMAN", "ZWINT_HUMAN", "ZY11B_HUMAN", "ZYX_HUMAN", "ZYX_HUMAN", "ZN384_HUMAN"],
             'Interaction': ["ZWINT_HUMAN", "ZW10_HUMAN", "ELOC_HUMAN", "NEBL_HUMAN", "ZN384_HUMAN", "ZYX_HUMAN"]})
        self.vertices = count_vertices(self.df)
        self.edges = count_edges(self.df)
        self.degree = get_degree(self.df, self.df.Sommet[0])
        self.max_degree = get_max_degree(self.df)
        self.average_degree = get_ave_degree(self.df)
        self.count_degree = count_degree(self.df, 1)
        self.hist = histogram_degree(self.df, 0, 5)

    def test_count_vertices(self):
        """Permet de tester le bon type de renvoi pour la fonction count_vertices"""
        self.assertGreaterEqual(self.vertices, 0,
                                "Renvoi bien un nombre positif")
    
    def test_count_edges(self):
        """Permet de tester le bon type de renvoi pour la fonction count_edges"""
        self.assertGreaterEqual(self.edges, 0,
                                "Nombre d'arrêtes entier")
        
    def test_get_degree(self):
        """Permet de tester si le calcul de get_degree est exact"""
        self.assertEqual(self.degree, sum(self.df.Sommet == self.df.Sommet[0]),
                         "Calcul le bon degré")

    def test_max_degree(self):
        """Permet de tester les bons types de renvoi pour la fonction max_degree"""
        self.assertGreaterEqual(self.max_degree[1], 0,
                                "Nombre positif")
        self.assertTrue(self.max_degree[0] != None,
                        "La protéine est nommée")

    def test_average_degree(self):
        """Permet de tester le bon type de renvoi pour la fonction average_degree"""
        self.assertGreaterEqual(self.average_degree, 1,
                                "Degré moyen supérieur à 1")

    def test_count_degree(self):
        """Permet de tester l'exactitude du renvoi de la fonction count_degree"""
        self.assertEqual(self.count_degree, 4,
                         "Bon nombre de protéine de degré 1")


if __name__ == '__Chapitre_2__':
    unittest.main()
