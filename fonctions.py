import donnes


def trouver():
    a = True
    while a:
        for i in range(donnes.coup):
            i = 0
            donnes.coup -= 1
            print(f"Il ne vous reste que {donnes.coup} en ne comptant pas celui actuelle")
            lettre = [input(''), input(''), input(''), input(''), input(''), input(''), input(''), input('')]
            if donnes.coup == 0:
                print("Perdu")
            elif donnes.coup > 0:
                if lettre[i] == donnes.list_mots[i]:
                    print(f"les lettre trouvés sont equivalente")
                    i += 1
                    print("Bravo")
                    a = False

                elif lettre != donnes.list_mots[i]:
                    print("Les lettres trouvés ne sont pas équivalents")
                else:
                    print("Probleme 1")
            elif donnes.coup < 0:
                print("Il est impossible d'avoir une valeur inferieur à 0")
            else:
                print("Je ne comprend pas, probleme 2")
