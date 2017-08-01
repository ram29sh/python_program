def isprime(n):
    if n==1:
        print("1 is a special")
    for x in range(2,n):
        if n%x ==0:
            print(n,"is not a prime number")
        else:
            print(n,"not a prime number")
        
for n in range(1,20):
    isprime(n)

     
