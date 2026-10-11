texte = input("Entrez un mot ou une phrase : ")

voyelles = "aeiouyAEIOUY"
compteur = 0

for lettre in texte:
    if lettre in voyelles:
        compteur += 1

print("Nombre de voyelles :", compteur)