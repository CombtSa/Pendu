import donnes
import fonctions
import pickle



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

score = {
    donnes.nom: donnes.coup
}

for donnes.coup in donnes.nom:
    score = {
        donnes.nom: donnes.coup
    }

with open('scores', 'wb') as fichier:
    mon_pickler = pickle.Pickler(fichier)
    mon_pickler.dump(score)
    fichier.close()

with open('scores', 'rb') as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    score_recupere = mon_depickler.load()
    fichier.close()
