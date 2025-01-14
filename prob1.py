def Somme_etalonnage(document):
    try:
        with open(document,'r') as document:
            lignes = document.readlines()
        somme_finale = 0
        for ligne in lignes:
            ligne = ligne.strip()
            chiffres = [char for char in ligne if char.isdigit()]
            valeur_etalonnage = int(chiffres[0] + chiffres[-1])
            somme_finale += valeur_etalonnage
        return somme_finale

    except FileNotFoundError:
        print("Fichier introuvable")
        return None
document= "document.txt"
resultat=Somme_etalonnage(document)
if resultat is not None:
    print(f"La somme des valeurs d'étalonnage est: {resultat}")