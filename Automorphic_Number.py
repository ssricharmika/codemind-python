n=int(input())
n_of_digits=len(str(n))
sq=n**2
l_digits=sq%pow(10,n_of_digits)
if l_digits==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")