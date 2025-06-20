# créer une classe pour gérer le tri
class SortEngine:
    
    """
    initialiser le moteur de tri avec une liste de dictionnaires
    data: liste de dictionnaires représentant les enregistrements.
    """
    def __init__(self,data):
        self.data = data
        
    """ implémenter le tri par insertion avec une liste de dictionnaire"""
    def tri_insertion(self,key):
        for i in range (1, len(self.data)):
            temp = self.data[i]
            j = i-1
            while j >= 0 and temp[key] < self.data[j][key]:
                self.data[j+1] = self.data[j]
                j-=1
            self.data[j+1] = temp
            
    """implémenter un tri rapide basé sur la recursivité"""
    def tri_rapide(self,key):
        self.data = self.tri_rapide_recursive(self.data,key)

    """ implémenter une fonction recursive pour le tri rapide."""
    def tri_rapide_recursive(self,arr,key):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr)//2][key]
        gauche = [x for x in arr if x [key] < pivot]
        milieu = [x for x in arr if x [key] == pivot]
        droite = [x for x in arr if x [key] > pivot]
        return self.tri_rapide_recursive(gauche,key)+ milieu + self.tri_rapide_recursive(droite,key)

    """ implémenter un tri multit-niveaux basé sur plusieurs clés."""
    def tri_multi_colonne(self,key):
        self.data.tri(key=lambda x: tuple(x[k]for k in key))

    """construire une fonction qui retourne les données triées"""
    def construire_donnees_sortie(self):
        return self.data 
