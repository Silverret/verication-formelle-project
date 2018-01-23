class Criteria:
    """
    TA : Toutes les affectations
    Tous les noeuds "assign" sont parcourus au moins une fois.
    """
    TA = 0

    """
    TD : Toutes les décisions
    Toutes les expressions booléennes qui apparaissent dans une instructions IF ou WHILE
    sont évaluées au moins une fois VRAI et FAUX.
    """
    TD = 1
    
    """
    k-TC : tous les k-chemins
    Tous les chemins de longueurs <= k sont parcourus/exécutés au moins par les tests
    """
    KTC = 2
    
    """
    i-TB : toutes les i-boucles
    Tous les chemins qui passent au plus i fois dans une boucle WHILE sont parcourus par les tests.
    """
    ITB = 3
    
    """
    T-Def : toutes les définitions
    Toutes les définitions des variables sont utilisées au moins une fois
    """
    TDEF = 4

    """
    TU : Toutes les utilisations
    Toutes les utilisations accessibles par chaque définition sont exécutées au moins une fois
    """
    TU = 5

    """
    T-DU : Tous les DU-chemins
    Pour chaque couple (définition, utilisation) d'une variable X,
    tous les chemins simples sans redéfinition intermédiaire de X sont exécutés une fois.
    """
    TDU = 6

    """
    TC : Toutes les conditions
    Tous les IF sont exécutés une fois VRAI une fois FAUX (au moins).
    """
    TC  = 7