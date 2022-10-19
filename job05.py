valeur1 = input("Valeur 1 : ")
valeur1 = int(valeur1)

valeur2 = input("Valeur 2 : ")
valeur2 = int(valeur2)

for x in range(valeur1+1, valeur2) or reversed(range(valeur2+1, valeur1)):
    print(x)

if valeur1 == valeur2:
    print("valeurs égales")