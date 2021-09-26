import unittest

sys.path.append("../DM_Res_Bio/Chapitre 2")
from Chapitre_2 import count_vertices, count_edges, get_degree, get_max_degree, get_ave_degree, count_degree, \
    histogram_degree


class TestFunction(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame(
            {'Sommet': ["ZW10_HUMAN", "ZWINT_HUMAN", "ZY11B_HUMAN", "ZYX_HUMAN", "ZYX_HUMAN", "ZN384_HUMAN"],
             'Interaction': ["ZWINT_HUMAN", "ZW10_HUMAN", "ELOC_HUMAN", "NEBL_HUMAN", "ZN384_HUMAN", "ZYX_HUMAN"]})
        self.vertices = count_vertices(self.df)
        self.edges = count_edges(self.df)
        self.degree = get_degree(self.df, self.df.Sommet[0])
        self.max_degree = get_max_degree(self.df)
        self.average_degree = get_ave_degree(self.df)
        self.count_degree = count_degree(self.df, 1)
        self.hist = histogram_degree(df, 0, 5)

    def test_count_vertices(self):
        self.assertGreaterEqual(self.vertices, 0,
                                "Renvoi bien un nombre positif")
    
    def test_count_edges(self):
        self.assertGreaterEqual(self.edges, 0,
                                "Nombre d'arrêtes entier")
        
    def test_get_degree(self):
        self.assertEqual(self.degree, sum(self.df.Sommet == self.df.Sommet[0]),
                         "Calcul le bon degré")

    def test_max_degree(self):
        self.assertGreaterEqual(self.max_degree[0], 0,
                                "Nombre positif")
        self.assertTrue(self.max_degree[1] != None,
                        "La protéine est nommée")

    def test_average_degree(self):
        self.assertGreaterEqual(self.average_degree, 1,
                                "Degré moyen supérieur à 1")

    def test_count_degree(self):
        self.assertEqual(self.count_degree, 4,
                         "Bon nombre de protéine de degré 1")

if __name__ == '__Chapitre_2__':
    unittest.main()
