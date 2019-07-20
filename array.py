from array import *
import numpy

def hasd():
    for i in range(4):
        for j in range(4):
            print('# ',end="")
        print()

vals = array('i',[1,2,3,4,5])
print(vals)

square = lambda a : a*a

print("Lambda function: ", square(5))

for i in vals:
    print(i,end="")

hasd()

def details(a, **b):
    print(a)
    
    for i,j in b.items():
        print(i,j)
    print(b)

details('santosh',age=29,city='Mumbai',target='1000M')

x=int(input("Enter the value you want to search"))
print(vals.index(x))