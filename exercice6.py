def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n - 1)

continuer = "oui"
while continuer == "oui":
    while True:
        saisie = input("donner un nombre entre 0 et 10 : ").strip()
        if not saisie.isdigit():
            print("Erreur: Veuillez entrer un nombre valide entre 0 et 10")
        elif int(saisie) > 10:
            print("Le nombre doit etre compris entre 0 et 10")
        else:
            n = int(saisie)
            break

    print("la factorielle de", n, "est", factorielle(n))
    continuer = input("voulez-vous continuer ? (oui/non) : ").strip()

print("Au revoir !")