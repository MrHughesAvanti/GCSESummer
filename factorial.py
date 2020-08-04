factorial = int(input("enter a number"))
result = 1
 
for i in range(1,factorial +1):
    result = result * i

print("the factorial of "+str(factorial)+" is : "+str(result))
