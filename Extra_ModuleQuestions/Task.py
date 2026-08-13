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

word = "python is easy and python is powerful"
split = word.split(" ")

for i in split:
    count = word.count(i)
    print(f"'{i}' : {count}")
print(split)

#4. Write a Python program to get a single string from two given strings, separated by a space and
#  swap the first two characters of each string.

first = input("Enter the first character:")
second = input("Enter the second character:")
print(f"{first[0]}+{second[1:]}")

#5. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
#If the given string already ends with 'ing' then add 'ly' instead If the string length of the given
#string is less than 3, leave it unchanged


'''n = input("Enter a string at least 3 lenght:")
if len(n)>=3:
    if n[-3:] == "ing":
        n+="ly"
    else:
        n+="ing"
else:
    print("Enter a string atleast 3 len!")
print(n)'''

#6. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if
# 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
# Return the resulting string

text = "The movie is not very poor"


