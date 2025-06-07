from storage import StorageManager

class CLIApp:
    def __init__(self):
        self.storage = StorageManager()
        self.tables = self.storage.chargees_donnees()

    def afficher_menu(self):
        print("\n********** Système de gestion **********")
        print("1. Afficher les tables")
        print("2. Ajouter une entrée")
        print("3. Sauvegarder les données")
        print("4. Créer une nouvelle table")  # Nouvelle option
        print("5. Quitter")

    def afficher_tables(self):
        if not isinstance(self.tables, dict):
            print("Erreur : les données chargées ne sont pas un dictionnaire.")
            return
        
        if not self.tables:
            print("Aucune table enregistrée.")
            return
        
        for table, records in self.tables.items():
            print(f"\nTable: {table}")
            for record in records:
                print(record)

    def obtenir_prochain_id(self, nom_table):
        table = self.tables.get(nom_table, [])
        if not table:
            return 1

        ids = []
        for enregistrement in table:
            if isinstance(enregistrement, dict) and "id" in enregistrement:
                try:
                    ids.append(int(enregistrement["id"]))
                except ValueError:
                    pass

        return max(ids, default=0) + 1

    def ajouter_enregistrement(self):
        nom_table = input("Nom de la table : ")
        if nom_table not in self.tables:
            print(f"La table '{nom_table}' n'existe pas.")
            return
        
        nouveau_enregistrement = {}
        prochain_id = self.obtenir_prochain_id(nom_table)
        nouveau_enregistrement["id"] = prochain_id

        print("Ajoutez un nouvel enregistrement (clé = valeur), terminez par 'fin'")
        
        while True:
            ligne = input(">")
            if ligne.lower() == "fin":
                break
            if "=" not in ligne:
                print("Format invalide. Utilisez clé=valeur.")
                continue
            key, value = ligne.split("=", 1)
            nouveau_enregistrement[key.strip()] = value.strip()
        
        self.tables[nom_table].append(nouveau_enregistrement)
        print(f"Enregistrement ajouté à la table '{nom_table}' avec ID {prochain_id}.")

    def creer_table(self):
        nom_table = input("Nom de la nouvelle table à créer : ").strip()
        if not nom_table:
            print("Nom invalide.")
            return
        if nom_table in self.tables:
            print(f"La table '{nom_table}' existe déjà.")
            return
        self.tables[nom_table] = []
        print(f"Table '{nom_table}' créée avec succès.")

    def executer(self):
        while True:
            self.afficher_menu()
            choix = input("Choisissez une option comprise entre (1-5) : ")
            if choix == "1":
                self.afficher_tables()
            elif choix == "2":
                self.ajouter_enregistrement()
            elif choix == "3":
                self.storage.sauvegarder_donnees(self.tables)
            elif choix == "4":
                self.creer_table()
            elif choix == "5":
                print("Fermeture du programme.")
                break
            else:
                print("Choix invalide. Veuillez entrer un chiffre entre 1 et 5.")

# Lancer le programme
if __name__ == "__main__":
    app = CLIApp()
    app.executer()
