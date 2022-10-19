with open("/home/alex/Github/starter-python/domains.xml", "r") as f:
    text = f.read()

print(len(text.split('"domain">')))


# Créer un programme job11.py qui parcourt le contenu du fichier “domains.xml” et qui
# compte le nombre de noms de domaine.