nombre = int(input ("Entrez un nomnbre de lettres : "))

with open("/home/alex/Github/starter-python/data.txt", "r") as f:
    text = f.read()
    text = text.replace(",", "").replace(";", "").replace(".", "").replace("?", "").replace("!", "").replace(":", "")
    words = text.split()
    count = 0

    for i in words:
        if len(i) == nombre:
            count = count +1

print(count)


#Créer un programme job13.py qui demande à l’utilisateur de renseigner un nombre
#entier. Le programme devra alors parcourir le contenu du fichier “data.txt” compter le
#nombre de mots de la taille renseignée qui s’y trouvent.