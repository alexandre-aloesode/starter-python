x = int (input("Largeur du rectangle : "))-2
y = int (input("hauteur du rectangle : "))-2

print ("|"+"-"*x+"|")
for y in range(y):
    print ("|"+" "*x+"|")
print ("|"+"-"*x+"|")