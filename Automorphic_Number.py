n=int(input())
n_of_digits=len(str(n))
sq=n**2
last_digits=sq%pow(10,n_of_digits)
if last_digits==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")