def myAddition(a, b):
    return(a+b)

first_value = int(input("Entrez un premier nombre : "))
second_value = int(input("Entrez un second nombre auquel additionner le premier : "))
result = myAddition(first_value, second_value)

print("le resultat de votre addition est :", result)