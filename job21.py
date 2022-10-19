def mySort(*args):
    liste = list(args)
    for i in range(len(liste)):
        for j in range(i + 1, len(liste)):
            if liste[i] > liste[j]:
               liste[i], liste[j] = liste[j], liste[i]
    return(liste)

def myDisplay(a):
    print(a)

myDisplay(mySort(158, 85, 268, 2, 6, 4, 75, 60, 200, 350, 150, 67, 43))



# Créer un programme job21.py. Reprenez l’exercice 19, mais modifiez le de façon à
# utiliser deux fonctions :
# - Une fonction mySort, qui prendra en paramètre une liste. Elle retourne une liste
# avec les valeurs de celle passée en paramètre, triés par ordre croissant.
# - Une fonction myDisplay qui prendra en paramètre une liste. Elle affichera dans le
# terminal le contenu de cette liste.