n = int(input("Donnez un entier positif : "))

while n < 0:
    print("Erreur : le nombre doit être positif.")
    n = int(input("Donnez un entier positif : "))

s = 0
for i in range(1, n + 1):
    s = s + i

print("La somme des entiers de 1 à", n, "est :", s)