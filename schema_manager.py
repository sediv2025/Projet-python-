#créer une classe pour définir et gérer les schémas d'une table #ajout
class SchemaManager:
    
    """la ligne de constructrice qui va initialiser un objet créer à partir d'une classe"""
    def __init__ (self):
        
        # créer un dictionnaire pour stocker les tables
        self.schemas = {}
        
        """créer une nouvelle définition de table avec colonnes et types"""
        def creer_schema(self,nom_table,colonne):
            
            #vérifier si le nom de la table existe dans le dictionnaire
            if nom_table in self.schemas :
                
                #lever une exception lorsqu'une valeur invalide est détectée
                raise ValueError(f"le schema '{nom_table}' existe déjà")
            #stocker le schéma sous forme de dictionnaire
            self.schemas[nom_table] = colonne
            print(f"schema'{nom_table}'créé avec succès.")
            
        """
        valider les données insérer par rapport au schéma
        la fonction retourne True si valide sinon une exception est levée
        
        """
        def valider_data(self,nom_table,data):
            
            #vérifier si le schéma existe dans le dictionnaire
            if nom_table not in self.schemas:
                raise ValueError(f"le schéma'{nom_table}' n'existe pas")
            schema = self.schhemas[ nom_table]
            for colonne, value in data.items():
                if colonne not in schema :
                    raise ValueError (f"colonne'{colonne}': attendu {self.schemas[colonne]._nom_} obtenu {type(value)._nom_}")
            print(f"données valides pour'{nom_table}'.")
            return True
        
        """afficher tous les schémas disponibles"""
        def afficher_schemas(self):
            # vérifier si aucun schéma n'existe encore
            if not self.schemas :
                print("aucun schéma enregistré")
                return
            #parcourir et afficher chaque schéma
            for nom_table,colonnes in self.schemas.items():
                print(f"{nom_table}:{colonnes}")
       
            
            
            
            
            
    
