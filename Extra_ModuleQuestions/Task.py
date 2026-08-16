# 1.Write a python program to sum of the first n positive integers.
'''n = int(input("Enter a n number:"))
summ = 0
for i in range(1,n+1):
    summ +=i
print("the sum of numbers:",summ)'''

#2. Write a Python program to count occurrences of a substring in a string.

'''n = input("Enter a word:")
sub_string = input("Enter your substring:")
count = n.count(sub_string)
print(f"The Substring is appeared {count} times")'''

#3. Write a Python program to count the occurrences of each word in a given sentence.

'''word = "python is easy and python is powerful"
split = word.split(" ")
count = {}

for i in split:
    if i in count:
        count[i] += 1
    else :
        count[i] = 1
for j in count:
    print(j,":",count[j])'''


#4. Write a Python program to get a single string from two given strings, separated by a space and
#  swap the first two characters of each string.

'''first = input("Enter the first character:")
second = input("Enter the second character:")
print(first[0]+second[1:]+ " " +second[0]+first[1:])  '''   

#5. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
#If the given string already ends with 'ing' then add 'ly' instead If the string length of the given
#string is less than 3, leave it unchanged


'''n = input("Enter a string at least 3 lenght:")
if len(n)>=3:
    if n[-3:] == "ing":
        n+="ly"
        print(n)
    else:
        n+="ing"
        print(n)
else:
    print("Enter a string atleast 3 len!")
'''

#6. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if
# 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
# Return the resulting string

'''import re 
text = "The movie is not very poor"
not_pos = text.find("not")
poor_pos = text.find("poor")

print(not_pos)
print(poor_pos)

if not_pos != -1 and poor_pos != -1 and not_pos < poor_pos:text = text[:not_pos] + "good" + text[poor_pos + 4:]

print(text)'''

# 7. Program to find Greatest Common Divisor of two numbers.
# For example, the GCD of 20 and 28 is 4 and GCD of 98 and 56 is 14.

'''import math
a = 20
b = 28
print(math.gcd(a,b))'''

# 8. Write a Python program to check whether a list contains a sublist.

#9. Write a Python program to find the second smallest number in a list.
'''l1 = [10, 5, 8, 3, 15]
l = sorted(l1)
print("Second Smallest number is",l[1])'''

# 10. Write a Python program to get unique values from a list.
'''l1 = [1, 2, 2, 3, 4, 4, 5]
l = list(set(l1))
print(l)
'''
#11. Write a Python program to unzip a list of tuples into individual lists.
'''l1 = [('A', 1), ('B', 2), ('C', 3)]
l2 = []
l3 = []
for i in range(len(l1)):
    l2.append(l1[i][0])
    l3.append(l1[i][1])

print(l2)
print(l3)'''

#12. Write a Python program to convert a list of tuples into a dictionary

'''l1 =  [('a', 1), ('b', 2), ('c', 3)]
d1 = dict(l1)
print(d1)'''


#13. Write a Python program to sort a dictionary (ascending /descending) by value.
'''d1  = {'a': 3, 'b': 1, 'c': 2}
a = dict(sorted(d1.items(),key=lambda x : x[1]))
d = dict(sorted(d1.items(),key=lambda x : x[1],reverse=True))


print("Asscending order:",a)
print("Descending order:",d)
'''

#14. Write a Python program to find the highest 3 values in a dictionary.
'''d1 = {'a': 50, 'b': 90, 'c': 30, 'd': 80, 'e': 70}
a = dict(sorted(d1.items(),key=lambda x : x[1])[-3:])
print(a)'''


#15. Given a number n, write a python program to make and print the list of Fibonacci series up to n.
# Input : n=7
# Hint : first 7 numbers in the series
# Expected output :
# First few Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13

'''n=int(input("enter the number: "))
a=0
b=1
c=0
for i in range(n+1):
    print(a)
    c=a+b
    a=b
    b=c '''

# 16. Counting the frequencies in a list using a dictionary in Python.
# Input : [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
# Expected output : 1 : 5 , 2 : 4 , 3 : 3 , 4 : 3 , 5 : 2

'''l1 = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
d1 = {}
for i in l1:
    count = 0
    if i not in d1:
        d1[i] = l1.count(i)
d2 = dict(sorted(d1.items()))
print(d2)'''

# 17. Write a python program using function to find the sum of odd series and even series
# Odd series: 12/ 1! + 32/ 3! + 52/ 5!+……n
# Even series: 22/ 2! + 42/ 4! + 62/ 6!+……n

'''import math
n = int(input("Enter a number:"))

odd = []
even = []
for i in range(n+1):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
 

def sum_odd_series (odd):
    total = 0
    for i in odd:
        total += ((i**2)/math.factorial(i))
    return total
def sum_even_series(even):
    totall = 0
    for i in even:
        
        totall += ((i**2)/math.factorial(i))
    return totall

print("Sum of odd series:",sum_odd_series(odd))
print("Sum of even series:",sum_even_series(even))'''

# 18. Python Program to Find Factorial of Number Using Recursion
'''def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5))'''

#19. Write a Python function that takes a list and returns a new list with unique elements of the first list.
'''l1 = [1, 2, 2, 3, 4, 3, 5]
l2 = list(set(l1))
print(l2)'''

#20. Mini project :
# Problem Statement : Password Generator
# Make a program to generate a strong password using the input given by the user. To generate a password,
# randomly take some words from the user input and then include numbers, special characters and capital
# letters to generate the password. Also, keep a check that password length is more than 8 characters.
# Note: Include Exception handling wherever required. Also, make a ‘User’ class and store the details like user
# id, name and password of each user as a tuple.


# Input:
# Enter User ID: 101
# Enter Name: Priyanka
# Enter some words: python coding
# Enter password length: 10

# Output:
# Generated Password: Py7#coding
# User Details:
# (101, 'Priyanka', 'Py7#coding')

import random
import string


class User:
    def __init__(self, user_id, name, password):
        self.user_id = user_id
        self.name = name
        self.password = password

    def get_details(self):
        return (self.user_id, self.name, self.password)


def generate_password(words, length):
    split_words = words.split()

    if len(split_words) == 0:
        raise ValueError("Please enter at least one word.")

    
    random_word = random.choice(split_words)
    short_word = random_word[:2].capitalize()

    
    random_num = str(random.randint(0, 9))
    random_symbol = random.choice(string.punctuation)

    
    last_random_word = random.choice(split_words)

    
    password = short_word + random_num + random_symbol + last_random_word

    
    if len(password) > length:
        password = password[:length]

    elif len(password) < length:
        remaining = length - len(password)

        characters = string.ascii_letters + string.digits + string.punctuation

        for i in range(remaining):
            password += random.choice(characters)

    return password


def check_password(password):
    if len(password) <= 8:
        return False

    upper = False
    lower = False
    digit = False
    special = False

    special_char = string.punctuation

    for ch in password:
        if ch.isupper():
            upper = True

        elif ch.islower():
            lower = True

        elif ch.isdigit():
            digit = True

        elif ch in special_char:
            special = True

    return upper and lower and digit and special


def main():

    try:
        user_id = int(input("Enter User ID: "))
        name = input("Enter Name: ")
        words = input("Enter some words: ")
        length = int(input("Enter password length: "))

        if length <= 8:
            raise ValueError("Password length must be more than 8.")

        password = generate_password(words, length)

        if check_password(password):
            user = User(user_id, name, password)

            print("\nGenerated Password:", password)
            print("User Details:")
            print(user.get_details())

        else:
            print("Password does not satisfy all requirements.")

    except ValueError as e:
        print("Error:", e)


main()