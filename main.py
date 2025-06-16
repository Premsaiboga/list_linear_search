# Reverse a String Without Using [::-1]:
# Reverse a string using a loop or recursion.
def reverse_sting(a):
    original = a
    left = 0
    right = len(a)-1
    while left<right:
        if a[left] != a[right]:
            return "not Palindrome"
        left +=1
        right -=1
    return "Palindrome"

print(reverse_sting("madam"))

# Count Frequency of an Element in a List:
# Input a list and an element; count how many times the element appears.
def count_elemet(a,b):
    count = 0
    for i in a:
        if i == b:
            count+=1
    return count
    
x = [2,1,3,4,5,2,4,2,5,2]
print(count_elemet(x,2))

# Print First N Prime Numbers:
# Take N as input and print the first N prime numbers.
def prime_number(n):
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i)

prime_number(10)


# Remove Duplicates from a List:
# Given a list, return a new list without duplicates (maintain order).
def remove_duplicates(lst):
    result = []
    for item in lst:
        duplicate_found = False
        for r in result:
            if item == r:
                duplicate_found = True
                break
        if not duplicate_found:
            result.append(item)
    return result

my_list = [1, 2, 2, 3, 1, 4, 3]
print(remove_duplicates(my_list))  #



# FizzBuzz:
# For numbers from 1 to N, print:

# “Fizz” if divisible by 3

# “Buzz” if divisible by 5

# “FizzBuzz” if divisible by both

# Else print the number itself."
def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizz_buzz(20)
