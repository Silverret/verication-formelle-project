## Projet de vérification formelle

### Travail effectué
Nos outils d'analyse de couverture et de génération de tests se basent sur un type de graphe CFG particulier :
* chaque noeud possède un label et un type (voir classe NodeType)
* chaque arrête possède un object instruction (voir classe Instruction), un object decision (voir boolean_expression.py)

Nous avons utilisé la bibliothèque Networkx pour modéliser les graphes de cette manière.
Dans trees.py, nous avons ainsi construit deux graphes: celui de la consigne et un autre qui contient une boucle.

### Utilisation

Lancer la commande ```python main.py``` et vous obtiendrez ce résultat:

TODO: mettre un screenshot du résultat

Il est possible de créer de nouveaux graphes dans trees.py, ainsi que de nouvelles variables.

Il suffit ensuite de les importer dans main.py puis de créer un objet PROG qui contient le graphe, le noeud intial, les noeuds finaux et les variables utilisées.

Lancer la fonction analyse_coverage avec le PROG, un set de critères et un set de tests.


### Architecture

#### IV_Classes

Contient les classes ArithmeticExpression, BooleanExpression, Criteria, Instruction et NodeType dans lesquelles nous avons défini formellement les outils que nous allions utilisés.

#### I_Analyse_de_couverture

Contient les fonctions qui permettent de vérifier un critère particulier.

#### II_Generation_de_tests

Permet de faire la génération de tests

TODO: expliquer ce qu'on a fait et là ou on est arrivé.


#### III_Graph_utils

Contient toutes les fonctions propres aux graphes et utiles pour l'analyse de couverture.

Par exemple la fonction parse() qui parcours un graph donné pour un jeu de test et qui renvoie le chemin parcouru ainsi que l'état des variables à chaque étape.



