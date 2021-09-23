import unittest


class TestStringMethods(unittest.TestCase):

    def test_nb_inter(self):


    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')



if __name__ == '__main__':
    unittest.main()





graph = {'Sommet': ['Vivien', 'Vivien', 'Vivien', 'Vivien', 'Guy', 'Guy'],
     'Interaction': ['Inter1', 'Inter2', 'Inter3', 'Inter4', 'Inter5', 'Inter6']}
df = pd.DataFrame(graph)

def flatten(d):
 v = [[i] if not isinstance(i, list) else flatten(i) for i in d]
 return [i for b in v for i in b]

def test_read_interaction_file_dict():
    if len(df) == len(flatten(read_interaction_file_dict(df).values())) and read_interaction_file_dict(df) == {'Guy':
        ['Inter5', 'Inter6'],'Vivien': ['Inter1', 'Inter2', 'Inter3', 'Inter4']}\
        or {'Vivien': ['Inter1', 'Inter2', 'Inter3', 'Inter4'],'Guy': ['Inter5', 'Inter6']}:
        print("Bon nombre d'intéractions ; Bon type de renvoi")
    else:
        print("Nombre d'intéractions ne correspond pas au dictionnaire ou bien le dictionnaire renvoyé est incorrecte")

def struct_nom_fichier(nom_fichier):
    if str(type(nom_fichier)) == "<class 'pandas.core.frame.DataFrame'>" and list(nom_fichier) == ['Interaction',
        'Sommet']or list(df.columns) == ['Sommet', 'Interaction']:
        print('Bon format de fichier')
    else:
        print("Le fichier doit être un DataFrame Pandas avec au moins deux colonnes nommées Sommet et Interaction")



