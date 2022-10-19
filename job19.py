def manualSort(*args):

#On doit trier une série d'arguments sans utiliser les fonctions sort et sorted
#Pour éviter l'erreur "TypeError: 'tuple' object does not support item assignment", on doit convertir le tuple en liste. Plus d'info sur 
# https://bobbyhadz.com/blog/python-typeerror-tuple-object-does-not-support-item-assignment#:~:text=The%20Python%20%22TypeError%3A%20%27tuple,list%20back%20to%20a%20tuple.

    liste = list(args)
    for i in range(len(liste)):
        for j in range(i + 1, len(liste)):
            if liste[i] > liste[j]:
               liste[i], liste[j] = liste[j], liste[i]
    print(liste)

manualSort(158, 85, 268, 2, 6, 4, 75, 60, 200, 350, 150, 67, 43)                                                                                                                                                                                                                                                                                              