import donnes
import fonctions
#TypeError: '<' not supported between instances of 'int' and 'str'



def verif_listmot():
    if donnes.list_mots.count(donnes.list_mots) == 8:
        print("Le mot a trouve est validé")
    elif donnes.list_mots.count(donnes.list_mots) < 8:
        print("Probleme valeur superieur")
        print("Fin du programme")
        quit()
    else:
        print("Erreur")


print(donnes.list_mots)
verif_listmot()
fonctions.trouver()
