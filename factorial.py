import math
print("Factorial Program")
num= eval(input("Enter Number to find the factorial of it: "))

fact=1
for i in range(num,1,-1):
    x= lambda a: a*1
    fact= fact* x(i)
print(fact)



