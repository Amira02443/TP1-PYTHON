
pronoms = ["je", "tu", "il/elle", "nous", "vous", "ils/elles"]
terminaisons_er = ["e", "es", "e", "ons", "ez", "ent"]
terminaisons_ir = ["is", "is", "it", "issons", "issez", "issent"]
def conjuguer(verbe):
    radical = verbe[:-2]          
    if verbe.endswith("er"):
        terminaisons = terminaisons_er
    elif verbe.endswith("ir"):
        terminaisons = terminaisons_ir
    else:
        print("Le verbe", verbe, "n'est pas du 1er ou du 2e groupe.")
        return
    print("Conjugaison du verbe", verbe, ":")
    for i in range(len(pronoms)):
        print(pronoms[i], radical + terminaisons[i])
    print()
verbes = ["parler", "chanter", "finir", "choisir"]
for verbe in verbes:
    conjuguer(verbe)