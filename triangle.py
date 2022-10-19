h = int(input("Entrez la hauteur du triangle : "))

for i in range(h):
    if i == h-1:
        print("_"*(h-i)+ "/"+ "_"*(i*2)+ "\\")
    else:
        print(" "*(h-i)+ "/"+ " "*(i*2)+ "\\")
