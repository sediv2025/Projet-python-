# Module pour manipuler les fichiers JSON
import json
# Module pour gérer les fichiers et répertoires
import os

# Créer une classe pour gérer la sauvegarde
class StorageManager:
    
    def __init__(self, file_path="database.json"):
        self.file_path = file_path
        
    """Sauvegarder les tables et leurs schémas dans un fichier JSON"""
    def sauvegarder_donnees(self, tables):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(tables, f, indent=4)
        print(f"Données sauvegardées dans {self.file_path}")

    """Charger les données depuis le fichier JSON"""
    def chargees_donnees(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print("Aucun fichier trouvé. Initialisation vide.")
            return {}
