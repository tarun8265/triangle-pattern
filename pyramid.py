n=int(input("enter number:"))
for i in range(n): #create a rows
    for j in range(n-i-1):#create a space
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()        