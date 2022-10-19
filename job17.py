def infinite(*args):
    myList = args
    
    for i in myList:
         if i%2 == 0:
             print(i)

infinite(1, 2, 3, 6, 8, 9 , 10, 13, 15, 18, 20, 50, 75, 88, 99, 100)
    