# BONUS QUESTIONS -------------------------------------------------------------


# B1. Build the function `sum_of_evens()` which accepts a single argument `numbers` (a list of integers)
#   The function returns the sum of only the even numbers in the list
#   If there are no even numbers, return 0
# Example: sum_of_evens([1, 2, 3, 4, 5, 6]) --> 12
# Example: sum_of_evens([7, 9, 11]) --> 0
 
def sum_of_evens(numbers):
    pass
 
 
# B2. Build the function `word_frequency()` which accepts a single argument `words` (a list of strings)
#   The function returns a dictionary mapping each word to the number of times it appears in the list
# Example: word_frequency(["apple", "banana", "apple"]) --> {"apple": 2, "banana": 1}
# Example: word_frequency([]) --> {}
 
def word_frequency(words):
    pass
 
 
# B3. Build the function `count_digits()` which accepts a single argument `number` (a non-negative integer)
#   The function returns how many digits are in `number`
#   You must use a while loop (do not convert the number to a string)
# Example: count_digits(12345) --> 5
# Example: count_digits(0) --> 1
 
def count_digits(number):
    pass
 
 
# B4. Build the function `count_types()` which accepts a single argument `values` (a list containing values of mixed types)
#   The function returns a dictionary mapping each type's name to how many values of that type are in the list
#   Hint: `type(value).__name__` gives the name of a value's type as a string
# Example: count_types([1, "a", 2.5, True, "b"]) --> {"int": 1, "str": 2, "float": 1, "bool": 1}
# Example: count_types([3, 4, 5]) --> {"int": 3}
 
def count_types(values):
    pass
 
 
# B5. Build the function `items_within_budget()` which accepts two arguments: `prices` (a list of floats) and `budget` (a float)
#   The function goes through `prices` in order, buying each item as long as the running total stays within `budget`
#   Stop at the first item that would push the total over the budget
#   The function returns the number of items purchased
#   You must use a while loop
# Example: items_within_budget([3.5, 2.0, 4.0, 1.5], 6.0) --> 2
# Example: items_within_budget([5.0, 5.0], 4.0) --> 0
 
def items_within_budget(prices, budget):
    pass
 
 
# B6. Build the function `grade_report()` which accepts a single argument `scores` (a dictionary mapping student names (str) to scores (int))
#   The function returns a dictionary mapping each student name to a letter grade
#   90 and above is "A", 80-89 is "B", 70-79 is "C", 60-69 is "D", and below 60 is "F"
# Example: grade_report({"Ana": 95, "Ben": 72, "Cy": 58}) --> {"Ana": "A", "Ben": "C", "Cy": "F"}
# Example: grade_report({"Dee": 80, "Eli": 89}) --> {"Dee": "B", "Eli": "B"}
 
def grade_report(scores):
    pass
 
 
# B7. Build the function `second_largest()` which accepts a single argument `numbers` (a list of integers)
#   The function returns the second largest DISTINCT value in the list
#   If the list has fewer than two distinct values, return None
# Example: second_largest([4, 9, 2, 7]) --> 7
# Example: second_largest([5, 5]) --> None
 
def second_largest(numbers):
    pass
 
 
# B8. Build the function `invert_dictionary()` which accepts a single argument `data` (a dictionary mapping strings to unique integers)
#   The function returns a new dictionary where each original value is now a key and each original key is now a value
# Example: invert_dictionary({"x": 10, "y": 20, "z": 30}) --> {10: "x", 20: "y", 30: "z"}
# Example: invert_dictionary({}) --> {}
 
def invert_dictionary(data):
    pass
 
 
# B9. Build the function `honor_roll()` which accepts two arguments: `students` (a list of dictionaries) and `min_gpa` (a float)
#   Each dictionary in `students` has a "name" key (a string) and a "gpa" key (a float)
#   The function returns a list of the names of students whose GPA is at least `min_gpa`, in their original order
# Example: honor_roll([{"name": "Ana", "gpa": 3.8}, {"name": "Ben", "gpa": 2.9}], 3.0) --> ["Ana"]
# Example: honor_roll([{"name": "Cy", "gpa": 3.0}, {"name": "Dee", "gpa": 3.2}], 3.0) --> ["Cy", "Dee"]
 
def honor_roll(students, min_gpa):
    pass
 
 
# B10. Build the function `is_palindrome()` which accepts a single argument `text` (a string)
#   The function returns True if `text` reads the same forwards and backwards, ignoring spaces and letter case
#   Otherwise, it returns False
# Example: is_palindrome("Never odd or even") --> True
# Example: is_palindrome("Python") --> False
 
def is_palindrome(text):
    pass
