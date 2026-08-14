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

