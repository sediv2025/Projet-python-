# créer une classe pour les opérations CRUD
class CRUDOperations :
    
    def __init__(self):
        #stocker les tables sous forme de listes de dictionnaires
        self.tables = {}
        #gestion des identifiants uniques
        self.auto_increment_ids = {}
        
        """ créer une nouvelle table vide"""
        def creer_table(self,nom_table):
            if nom_table in self.tables :
                raise ValueError(f"la table'{nom_table}'existe déjà.")
            self.tables[nom_table] = []
            self.auto_increment_ids[nom_table] = 1
            print(f"Table'{nom_table}'créée avec succès.")

        """ ajouter un nouvel enregistrement à une table(record: enregistrer)"""
        def ajouter_enregistrement(self,nom_table,record):
            if nom_table not in self.tables :
                raise ValueError(f"la table'{nom_table}' n'existe pas.")
            #ajouter l'id (ID) uniqe
            record["id"] = self.auto_increment_ids[nom_table]
            self.tables[nom_table].append(record)
            self.auto_increment_ids[nom_table]+=1
            print(f"enregistrement ajouuté à table '{nom_table}' : {record}")
            
        """récupéérer un enregistrement par son identifiant"""
        def recueillir_enregistrement(self,nom_table,record_id):
            if nom_table not in self.tables :
                raise ValueError(f"la table'{nom_table}' n'existe pas.")
            for record in self.tables[nom_table]:
                if record["id"] == record_id :
                    return record
            raise ValueError(f"aucun enregistrement avec l'ID {record_id} trouvé.")
        """ récupérer tous les enregistrements  d'une table"""
        def recueillir_tous_enregestriment(self,nom_table):
            if nom_table not in self.tables:
                raise ValueError(f"la table'{nom_table}' n'existe pas.")
            return self.tables[nom_table]

        """mettre à jour un enregistrement existant"""
        def mise_a_jour__enregistrement(self,nom_table,record_id,updated_data):
            if nom_table not in self.tables :
                raise ValueError(f"la table'{nom_table}'n'existe pas.")
            for record in self.tables[nom_table]:
                if record ["id"]== record_id :
                    record.update(updated_data)
                    print(f"enregistrement mis à jour:{record}")
                    return
            raise ValueError(f"aucun enregistrement avec l'ID {record_id} trouvé.")

        """supprimer un enregistrement par son identifiant"""
        def supprimer_enregistrement(self,nom_table,record_id):
            if nom_table not in self.tables :
                raise ValueError(f"la table'{nom_table}'n'existe pas.")
            for record in self.tables[nom_table]:
                if record["id"] == record_id:
                    self.tables[nom_table].remove(record)
                    print(f"enregistrement avec ID {record_id} supprimé.")
                    return
                raise ValueError(f"aucun enregistrement avec l'ID {record_id} trouvé.")
            
                    

















            
