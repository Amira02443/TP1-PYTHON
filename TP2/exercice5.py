MOTS = ("pierre", "feuille", "ciseaux")
def f(mot):
    return MOTS.index(mot)
def g(code):
    return MOTS[code]
print(f("pierre"), f("feuille"), f("ciseaux"))
print(g(0), g(1), g(2))                          