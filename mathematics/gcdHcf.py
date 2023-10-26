a=int(input('Enter first number '))
b=int(input('Enter second number '))

#1st method
# def gcdHcf(n,m):
#     arr=[]
#     for i in range(1,n+1):
#         remainder1=n%i
#         remainder2=m%i
#         if remainder1==0 and remainder2==0:
#             arr.append(i)
#     print("gcd is ", arr[len(arr)-1])    

             
            
#2nd method(ecuilidean algorithm)

# def gcd(a,b):
#     while a!=b:
#         if a>b:
#             a=a-b
#         else:
#             b=b-a
#     print("gcd is ",a)

#3rd method(optimized eculidean algorithm)

def gcd(a,b):
    while b==0:
        return a
    return gcd(b,a%b)

gcd(a,b)                
                    