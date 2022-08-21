import donnes
import fonctions



def verif_listmot():
    if donnes.list_mots.count(donnes.list_mots) == 8:
        print("Le mot a trouve est validé")
        fonctions.trouver()
    else:
        print("Erreur")
        quit()

print(donnes.nom)
print(donnes.list_mots)
verif_listmot()
