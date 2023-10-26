n=int(input('Enter a number '))

def countDigits(n):
    count=0
    while n>0:
        remainder=n%10
        n=n//10
        count=count+1
    return count
print(countDigits(n))    
        