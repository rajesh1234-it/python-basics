# list comprehension
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(n) for n in list_of_strings]
result = [num for num in numbers if num % 2 == 0]
print(result)

import random
# dictionary comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {student: random.randint(1, 100) for student in names}
passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)



# Filter Even Numbers
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [n for n in numbers if n % 2 == 0]

# Convert Strings to Integers
string_numbers = ['10', '20', '30']
int_numbers = [int(n) for n in string_numbers]

#Flatten a 2D List
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [item for row in matrix for item in row]

# Capitalize Names
names = ['alice', 'bob', 'charlie']
capitalized = [name.capitalize() for name in names]

#  Dictionary Comprehension Use Cases
# Word Length Dictionary
sentence = "Python is powerful"
word_lengths = {word: len(word) for word in sentence.split()}

#Filter Only Expensive Products
products = {'pen': 10, 'laptop': 1000, 'book': 50}
expensive = {k: v for k, v in products.items() if v > 100}

#Invert a Dictionary (values become keys)
fruit_prices = {'apple': 3, 'banana': 2, 'orange': 4}
inverted = {v: k for k, v in fruit_prices.items()}

#Create a Lookup Table
squares = {x: x*x for x in range(1, 6)}

# use dataframe
import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_df = pd.DataFrame(student_dict)
print(student_df)

# loop through a dataframe
for (index, row) in student_df.iterrows():
    if row.student == "Angela":
        print(row.score)


# phonotic alphabet game
df = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for _, row in df.iterrows()}

word = input("Enter a word: ").upper()

output = [phonetic_dict[letter] for letter in word if letter in phonetic_dict]

print("Phonetic Code:", output)
