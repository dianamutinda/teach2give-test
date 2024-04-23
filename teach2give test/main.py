
#write a program that prints the numbers from 1 to 100.For multiples of 3,print "fizz";for multiples of 5, print
#"buzz"; and for numbers that are both multiples of 3 and 5 print "fizz_buzz"
def fizz_buzz(n):
    result = []
    for i in range (1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("fizz_buzz")
        elif i % 3 == 0:
            result.append("fizz")
        elif i % 5 == 0:
            result.append("buzz")
        else:
            result.append(str(i))
    return result
n = 100
result = fizz_buzz(n)
print('' . join(result))

#write an program that takes an integer as input and returns true if the input is a power of two.
nterms = int(input("How many terms? "))
n1 = 0
n2 = 1
count = 0

if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

#Write a program that takes an integer as input and returns true if the input is a power of two
import math
def log2(x):
    return (math.log10(x)/
            math.log10(2));

def isPowerOfTwo(n):
    return (math.ceil(log2(n)) == math.floor(log2(n)));

if(isPowerOfTwo(3)):
    print("True");
else:
    print("False");

if(isPowerOfTwo(4)):
    print("True");
else:
    print("False");


#write a program that accepts string as input, capitalizes the first letter of each word in the string and then the result string
def capitalize(str):
    return ''.join(map(lambda s:s[:-1]+s[-1].upper(), s.title().split()))

s = "i love programming"
print("string before:", s)
print("string after:", capitalize(str))


#write a program that takes an integer as input and returns an integer with reversed digit odering
n = 1234
rev = 0

while (n > 0):
    a = n % 10
    rev = rev * 10 + a
    n = n//10
print(rev)

#Write a program that counts the number of vowels in a sentence
string = "hello world"
vowels = "aeiouAEIOU"

count = sum(string.count(vowel)
            for vowel in vowels)
print(count)