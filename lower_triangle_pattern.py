#n=number of rows
n=int(input("enter number:"))
for i in range(n):
      for j in range(i,n): #create a rows
            print("",end="")
      for j in range(i+1):
            print("*",end="")
      
      print()      