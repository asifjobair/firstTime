x = int(input("the no:"))
sum = 0
org = x
while x>0:
    sum = sum+(x%10)*(x%10)*(x%10)
    x = x//10
if org == sum:
    print("arms")
else:
    print("not arm")
    