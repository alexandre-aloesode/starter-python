chain = input("veuillez entrer une chaine de caractères : ")
typeOfSort = input("choisissez un mode de tri (upper / lower / title / clean) : ")



def myUper(a):
    print(a.upper())

def myLower(b):
    b = print(chain.lower())

def myTittle(c):
    import string
    c = print(string.capwords(chain))

def myClean(d):
    d = print(chain.replace("  "," "))


if typeOfSort == "upper":
    myUper(chain)

elif typeOfSort == "lower":
    myLower(chain)

elif typeOfSort == "title":
    myTittle(chain)

elif typeOfSort == "clean":
    myClean(chain)

else:
    print("mode de tri invalide")



#     Créer un programme job22.py. Il devra prendre un premier input qui sera une chaine de
# caractère, puis un deuxième. Si le deuxième input est :
# - “upper” : une fonction “myUper” devra être appellée. Cette fonction prend en
# paramètre une chaine de caractère, et retourne cette chaîne en majuscule.
# - “lower” : une fonction “myLower” devra être appellée. Cette fonction prend en
# paramètre une chaine de caractère, et retourne cette chaîne en minuscule.
# - “title” : une fonction “myTitle” devra être appellée. Cette fonction prend en
# paramètre une chaine de caractère, et retourne cette chaîne avec une majuscule
# au début de chaque mot.
# - “clean” : une fonction “myClean” devra être appellée. Cette fonction prend en
# paramètre une chaine de caractère, et retourne cette chaîne en enlevant tous les
# espaces inutiles (en début et en fin de chaine de caractère, et les doubles
# espaces).
# Aucune fonction system n’est autorisée. Vous pouvez cependant les tester afin d’étudier
# leur fonctionnement.
# A la fin de votre programme, la chaine de caractère retournée par la fonction devra être
# affichée sur le terminal.