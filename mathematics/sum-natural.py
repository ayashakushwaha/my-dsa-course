n=int(input("enter the value of n"))  
#python is a interpreted language it compiles from up to down so u have to declare the function before using it
#1st method
# def sum(n):
#     sum1=0
#     for i in range (1,n+1):
#         sum1=sum1+i
#     return sum1    
# print(sum(n))      
    
#2nd method

def sum(n):
    sum=n*(n+1)/2
    return sum
print(sum(n))   



  


