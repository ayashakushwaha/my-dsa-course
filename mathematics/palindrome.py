n=int(input('Enter a number '))

def palindrome(n):
    nCopy=n
    reversed=0
    while nCopy>0:
        r=nCopy%10
        nCopy=nCopy//10 
        reversed=reversed*10+r  
    if(n==reversed):
        print(str(n) +" is a palindrome number.")
    else:
        print(str(n)+" is not a palindrome number.")    
 
palindrome(n)
        