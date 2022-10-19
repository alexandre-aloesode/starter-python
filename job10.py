texte = input("Que souhaitez vous écrire? ")

with open ("/home/alex/Github/starter-python/output.txt", "w") as f:  
    f.write(texte)