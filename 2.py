def factorial(a):
    if a==1:
        return 1
    else:
        return a*day7(a-1)
    
a=int(input("Enter any num :"))
res=day7(a)
print("Factorial is ",res)