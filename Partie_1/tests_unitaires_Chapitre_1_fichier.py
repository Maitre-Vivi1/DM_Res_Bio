import sys
import unittest
import pandas as pd

sys.path.append("../DM_Res_Bio/Partie_1")
from Chapitre_1 import is_interaction_file


class TestChapitre1Fichier(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame(
            {'Sommet': ["ZW10_HUMAN", "ZWINT_HUMAN", "ZY11B_HUMAN", "ZYX_HUMAN", "ZYX_HUMAN", "ZN384_HUMAN"],
             'Interaction': ["ZWINT_HUMAN", "ZW10_HUMAN", "ELOC_HUMAN", "NEBL_HUMAN", "ZN384_HUMAN", "ZYX_HUMAN"]})
        self.df2 = pd.DataFrame(
            {'Sommet_bla': ["ZW10_HUMAN", "ZWINT_HUMAN", "ZY11B_HUMAN", "ZYX_HUMAN", "ZYX_HUMAN", "ZN384_HUMAN"],
             'Interaction_bla': ["ZWINT_HUMAN", "ZW10_HUMAN", "ELOC_HUMAN", "NEBL_HUMAN", "ZN384_HUMAN", "ZYX_HUMAN"]})
        self.df3 = {'Sommet': ["ZW10_HUMAN", "ZWINT_HUMAN", "ZY11B_HUMAN", "ZYX_HUMAN", "ZYX_HUMAN", "ZN384_HUMAN"],
                    'Interaction': ["ZWINT_HUMAN", "ZW10_HUMAN", "ELOC_HUMAN", "NEBL_HUMAN", "ZN384_HUMAN",
                                    "ZYX_HUMAN"]}
        self.df4 = pd.DataFrame({})
        self.df5 = {'Sommet': ["ZW10_HUMAN", "ZWINT_HUMAN", "ZY11B_HUMAN", "ZYX_HUMAN", "ZYX_HUMAN", "ZN384_HUMAN"],
             'Interaction': ["ZW10_HUMAN", "ELOC_HUMAN", "NEBL_HUMAN", "ZN384_HUMAN", "ZYX_HUMAN"]}

    def test_is_interaction(self):
        self.assertTrue(is_interaction_file(self.df))
        self.assertFalse(is_interaction_file(self.df2))
        self.assertFalse(is_interaction_file(self.df3))
        self.assertFalse(is_interaction_file(self.df4))
        self.assertFalse(is_interaction_file(self.df5))


if __name__ == '__Chapitre_1__':
    unittest.main()
