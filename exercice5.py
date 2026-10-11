constconst = True

while const == True:
    a = int(input("donner un entier : "))
    while a < 0:
        print("Erreur : l'entier doit être positif")
        a = int(input("donner un entier : "))

    b = int(input("donner la puissance : "))
    while b < 0:
        print("Erreur : la puissance doit être positive")
        b = int(input("donner la puissance : "))

    s = 1
    for i in range(b):
        s = s * a

    print("la puissance est", s)

    c = input("voulez vous continuer ? (oui/non) : ")
    if c == "oui":
        const = True
    else:
        const = False