x = int(input("enter the no:"))
n1,n2 = 0,1
sum = 0
if x<0:
    print("fog is")
else:
    for i in range (0,x):
        print(sum, end=" ")
        n1 = n2
        n2 = sum
        sum = n1+n2