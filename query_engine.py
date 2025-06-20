#créer une classe pour gérer les recherches et filtrer #ajout
class QueryEngine :
    
    """
    initialiser le moteur de recherche avec une table de données.
    data source : liste de dictionnaires réprésentants les enregistrments
    """
    def __init__(self,data_source):
        self.data_source = data_source
        #créer les index pour les recherches rapides (optionnel)
        self.index = {}
        
    """
    construire un index basé sur une clé donnée pour des recherches rapides.
    key (clé):nom du champ utilisé comme index
    """
    def construire_index(self,key):
        self.index = {record[key]: record for record in self.data_source if key in record}
        print(f"index construit sur'{key}'.")
        
    """
    implémenter la recherche sequentiel correspondant aux critères
    critere: dictionnaire contenant des clés-valeurs à rechercher.
    retourne la liste des enregistrements correspondants.
    """
    def recherche_sequentiel(self,critere):
        results = [
            record for record in self.data_source
            if all(record.get(k)== v for k, v in critere.items())
        ]
        return results
    
    """
    recherche rapide à l'aide de l'index si disponibble
    key : clé de recherche
    value: valeur associée
    retourne enregistrement trouvé ou None
    """
    def recherche_avec_index(self,key,value):
        if not self.index :
            print(f"aucun index disponible. effectuez une recherche séquentielle à la place.")
            return self.recherche_sequentiel({key:value})
        return self.index.get(value)

    """
    filtrer les enregistrements selon une condition donnée(age > 30).
    condition : fonction lambda définissant la condition.
    retourne la liste des enregistrements filtrés
    """
    def filtrer_enregistrement(self,condition):
        return[record for record in self.data_source if condition(record)]
    
