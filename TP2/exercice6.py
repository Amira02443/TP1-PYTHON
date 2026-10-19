def est_palindrome(conteneur):
    return conteneur == conteneur[::-1]
def nettoyer_et_verifier(chaine):
    nettoye = "".join([c.lower() for c in chaine if c.isalnum()])
    return (est_palindrome(nettoye), nettoye)
def trouver_palindromes(liste_mots):
    return [mot for mot in liste_mots if est_palindrome(mot)]
print(est_palindrome("radar"))              
print(est_palindrome([1, 2, 3, 2, 1]))   
print(est_palindrome(("a", "b")))          
print(nettoyer_et_verifier("Esope reste ici et se repose"))
print(nettoyer_et_verifier("Bonjour !"))
mots = ["radar", "kayak", "python", "level", "coucou", "abcba"]
print(trouver_palindromes(mots))
