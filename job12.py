with open("/home/alex/Github/starter-python/data.txt", "r") as f:
    text = f.read()

print(len(text.split()))


# Créer un programme job12.py qui parcourt le contenu du fichier “data.txt” et qui compte
# le nombre de mots (sans caractère spéciaux) qui s’y trouvent.