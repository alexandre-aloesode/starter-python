def infinite(*args):
    myList = args
    
    for i in myList:
         if i%2 == 0:
             print(i)

infinite(1, 2, 3, 6, 8, 9 , 10, 13, 15, 18, 20, 50, 75, 88, 99, 100)
    

# Créer un programme job17.py. Le programme devra contenir une fonction qui prend en
# paramètres un nombre de paramètres indéfini (uniquement des nombres).
# La fonction devra :
# - Remplir une liste myList contenant tous ces paramètres.
# - Parcourir et afficher dans le terminal uniquement les nombres pairs de la liste.