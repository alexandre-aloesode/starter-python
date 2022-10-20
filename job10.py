texte = input("Que souhaitez vous écrire? ")

with open ("/home/alex/Github/starter-python/output.txt", "w") as f:  
    f.write(texte)

with open ("/home/alex/Github/starter-python/output.txt", "r") as f:
    contenu = f.read()
print(contenu)