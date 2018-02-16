## Projet de vérification formelle

### Travail effectué
Nos outils d'analyse de couverture et de génération de tests se basent sur un type de graphe CFG particulier :
* chaque noeud possède un label et un type (voir classe NodeType)
* chaque arrête possède un object instruction (voir classe Instruction), un object decision (voir ```boolean_expression.py```)

Nous avons utilisé la bibliothèque Networkx pour modéliser les graphes de cette manière.
Dans ```trees.py```, nous avons ainsi construit deux graphes: celui de la consigne et un autre qui contient une boucle.

### Utilisation

Lancer la commande ```python main.py``` et vous obtiendrez ce résultat:

TODO: mettre un screenshot du résultat

* Il est possible de créer de nouveaux graphes dans trees.py, ainsi que de nouvelles variables.
* Il suffit ensuite de les importer dans main.py puis de créer un objet PROG qui contient le graphe, le noeud intial, les noeuds finaux et les variables utilisées.
* Lancer la fonction analyse_coverage avec le PROG, un set de critères et un set de tests.

### Architecture

#### IV\_Classes

Contient les classes ArithmeticExpression, BooleanExpression, Criteria, Instruction et NodeType dans lesquelles nous avons défini formellement les outils utilisés.

#### I\_Analyse\_de\_couverture

Contient les fonctions qui permettent de vérifier un critère particulier.

#### II\_Generation\_de\_tests

Permet de faire la génération de tests

Utilie le package constraint

Nous n'avons pas réussi à finir cette partie. Nous avons réalisé l'exécution symbolique du programme donné à la génération de tests, en implémentant en fonction replace à toutes nos classes héritant d'ArithmeticExpression et/ou BooleanExpression.
À la fin de l'exécution symbolique, on obtiens une liste de booléenne expressions exprimées en fonction des input du programme qui doivent être vrais. Nous n'avons pas réussi à exprimer ces expressions booléennes en contraintes que le constraint.problem comprend. 

#### III\_Graph\_utils

Contient toutes les fonctions propres aux graphes et utiles pour l'analyse de couverture.

Par exemple la fonction ```parse()``` qui parcours un graph donné pour un jeu de test et qui renvoie le chemin parcouru ainsi que l'état des variables à chaque étape.
