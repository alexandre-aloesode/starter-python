#J'avais au départ compris qu'il fallait créer un fichier myList.txt dans lequel on retrouverait les arguments de la fonction. 
#Je garde le script par rapport aux recherches que ça m'a amené à faire.

def infinite(*args):

    with open ("/home/alex/Github/starter-python/mylist.txt", "w") as f:
        monconvert = args
        maliste= tuple(map(str, monconvert))
# on utilise ces arguments et la commande ci-dessous plutôt que de faire directement f.write(maliste) pour contourner l'erreur
# "TypeError: write() argument must be str, not tuple " et pouvoir ecrire notre suite de chiffres/nombres
# dans un fichier. plus d'infos sur https://bobbyhadz.com/blog/python-typeerror-write-argument-must-be-str-not-tuple
        f.write("\n".join(maliste))

    for i in args:
        if i%2 == 0:
            print(i)

infinite(1, 2, 3, 6, 8, 9 , 10, 13, 15, 18, 20, 50, 75, 88, 99, 100)