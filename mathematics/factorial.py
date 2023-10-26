n=int(input("enter a number: "))

# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     print("factorial is ",fact)

def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

print(factorial(n))       