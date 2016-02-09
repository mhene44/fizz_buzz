import sys

if sys.argv[1:]:
    upper_limit = sys.argv[1]
else:
    upper_limit = input("How far should we play 'Fizz Buzz' to? ")

print("Fizz buzz counting up to " + upper_limit + ".")

for n in range(1,int(upper_limit)+ 1):

    if n % 3 == 0 and n % 5 == 0:
        print("fizz buzz")
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("buzz")
    else:
        print(n)