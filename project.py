import random
num=int(random.randrange(-100,100))
print(num)
if num==0:
    print(num,"is neither odd nor even")
elif  num%2==0 :
    print(num,"is a even number")
else:
    print(num,'is a odd number')
if num>0:
    print(num,"is positive ")
elif num==0:
    print(num,"is neither positive nor negative")
else:
    print(num,"is negative")
# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
flag = 0

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = flag+1
            # break out of loop
            break
    if flag>=1:
        print(num, "is a composite number")
    else:
        print(num, "is a prime number")
else:
    print("neither prime neither composite" )