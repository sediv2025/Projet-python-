from storage import StorageManager

#ajout
class CLIApp:
    def __init__(self):
        self.storage = StorageManager()
        self.tables = self.storage.chargees_donnees()

    def afficher_menu(self):
        print("\n********** Système de gestion **********")
        print("1. Afficher les tables")
        print("2. Ajouter une entrée")
        print("3. Sauvegarder les données")
        print("4. Créer une nouvelle table")
        print("5. Supprimer une table")
        print("6. Mettre à jour un enregistrement")   # Ajouté
        print("7. Filtrer les enregistrements") 
        print("8. Modifier le nom d'une table")      # Ajouté
        print("9. Quitter")                           # Modifié

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
    
    def supprimer_table(self):
        nom_table = input("Nom de la table à supprimer : ").strip()
        if nom_table not in self.tables:
            print(f"La table '{nom_table}' n'existe pas.")
            return
        del self.tables[nom_table]
        print(f"Table '{nom_table}' supprimée avec succès.")

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
    def mettre_a_jour_enregistrement(self):
        nom_table = input("Nom de la table : ").strip()
        if nom_table not in self.tables:
            print(f"La table '{nom_table}' n'existe pas.")
            return
        id_modif = input("ID de l'enregistrement à modifier : ").strip()
        for enregistrement in self.tables[nom_table]:
            if str(enregistrement.get("id")) == id_modif:
                print(f"Enregistrement actuel : {enregistrement}")
                cle = input("Clé à modifier : ").strip()
                if cle not in enregistrement:
                    print("Clé inexistante.")
                    return
                nouvelle_valeur = input("Nouvelle valeur : ").strip()
                enregistrement[cle] = nouvelle_valeur
                print("Enregistrement mis à jour.")
                return
        print("Aucun enregistrement avec cet ID.")
    def filtrer_enregistrements(self):
        nom_table = input("Nom de la table : ").strip()
        if nom_table not in self.tables:
            print(f"La table '{nom_table}' n'existe pas.")
            return
        cle = input("Clé à filtrer : ").strip()
        valeur = input("Valeur recherchée : ").strip()
        print(f"Résultats pour {cle} = {valeur} :")
        trouve = False
        for enregistrement in self.tables[nom_table]:
            if str(enregistrement.get(cle, "")).lower() == valeur.lower():
                print(enregistrement)
                trouve = True
        if not trouve:
            print("Aucun enregistrement trouvé.")
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
        
    def modifier_nom_table(self):
        ancien_nom = input("Nom actuel de la table à modifier : ").strip()
        if ancien_nom not in self.tables:
            print(f"La table '{ancien_nom}' n'existe pas.")
            return
        nouveau_nom = input("Nouveau nom pour la table : ").strip()
        if not nouveau_nom:
            print("Nom invalide.")
            return
        if nouveau_nom in self.tables:
            print(f"Une table avec le nom '{nouveau_nom}' existe déjà.")
            return
        self.tables[nouveau_nom] = self.tables.pop(ancien_nom)
        print(f"Le nom de la table '{ancien_nom}' a été modifié en '{nouveau_nom}'.")

    def executer(self):
        while True:
            self.afficher_menu()
            choix = input("Choisissez une option comprise entre (1-9) : ")
            if choix == "1":
                self.afficher_tables()
            elif choix == "2":
                self.ajouter_enregistrement()
            elif choix == "3":
                self.storage.sauvegarder_donnees(self.tables)
            elif choix == "4":
                self.creer_table()
            elif choix == "5":
                self.supprimer_table()
            elif choix == "6":
                self.mettre_a_jour_enregistrement()   # Ajouté
            elif choix == "7":
                self.filtrer_enregistrements() 
            elif choix == "8":
                self.modifier_nom_table()        # Ajouté
            elif choix == "9":
                print("Fermeture du programme.")
                break 
            else: 
                print("choix invalide")

# Lancer le programme
if __name__ == "__main__":
    app = CLIApp()
    app.executer()
