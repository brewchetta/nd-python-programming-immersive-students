# =============================================================================
# PYTHON BEGINNER EXERCISES
# =============================================================================
# These are your very first exercises with lists, dictionaries, and loops.
# Each function should RETURN its result (not print it).
# Replace `pass` with your own code.
# =============================================================================
 
 
# 1. Build the function `first_item()` which accepts a single argument `items` (a list of strings)
#   The function returns the first item in the list
#   You may assume the list always has at least one item
# Example: first_item(["red", "green", "blue"]) --> "red"
# Example: first_item(["dog"]) --> "dog"
 
def first_item(items):
    pass
 
 
# 2. Build the function `add_item()` which accepts two arguments: `items` (a list of strings) and `new_item` (a string)
#   The function adds `new_item` to the end of the list and returns the updated list
# Example: add_item(["apple", "banana"], "cherry") --> ["apple", "banana", "cherry"]
# Example: add_item([], "milk") --> ["milk"]
 
def add_item(items, new_item):
    pass
 
 
# 3. Build the function `get_age()` which accepts two arguments: `ages` (a dictionary mapping names (str) to ages (int)) and `name` (a string)
#   The function returns the age stored in the dictionary for `name`
#   You may assume `name` is always in the dictionary
# Example: get_age({"Sam": 12, "Priya": 14}, "Priya") --> 14
# Example: get_age({"Leo": 9}, "Leo") --> 9
 
def get_age(ages, name):
    pass
 
 
# 4. Build the function `add_pet()` which accepts three arguments: `pets` (a dictionary mapping owner names (str) to pet types (str)), `owner` (a string) and `animal` (a string)
#   The function adds `owner` to the dictionary with `animal` as their value, and returns the updated dictionary
# Example: add_pet({"Ana": "cat"}, "Ben", "dog") --> {"Ana": "cat", "Ben": "dog"}
# Example: add_pet({}, "Cy", "fish") --> {"Cy": "fish"}
 
def add_pet(pets, owner, animal):
    pass
 
 
# 5. Build the function `total()` which accepts a single argument `numbers` (a list of integers)
#   The function uses a for loop to add up every number in the list and returns the sum
#   If the list is empty, return 0
# Example: total([1, 2, 3, 4]) --> 10
# Example: total([]) --> 0
 
def total(numbers):
    pass
 
 
# 6. Build the function `double_all()` which accepts a single argument `numbers` (a list of integers)
#   The function uses a for loop to build a new list where every number has been multiplied by 2, and returns the new list
# Example: double_all([1, 2, 3]) --> [2, 4, 6]
# Example: double_all([5]) --> [10]
 
numbers = [1,2,3,4,5,0,-5]

def double_all(numbers):
    new_list = []
    for n in numbers:
        doubled = n * 2
        new_list.append(doubled)
    return new_list
    # alternative
    return [ num * 2 for num in numbers ]
 
 
# 7. Build the function `countdown()` which accepts a single argument `start` (a positive integer)
#   The function uses a while loop to build a list that counts down from `start` to 1, and returns the list
# Example: countdown(3) --> [3, 2, 1]
# Example: countdown(1) --> [1]
 
def countdown(start):
    pass
 
 
# 8. Build the function `describe_number()` which accepts a single argument `number` (an integer)
#   The function returns "positive" if `number` is greater than 0 and "negative" if it is less than 0
#   If `number` is 0, return "zero"
# Example: describe_number(8) --> "positive"
# Example: describe_number(-3) --> "negative"
 
def describe_number(number):
    pass
 
 
# 9. Build the function `add_text_numbers()` which accepts two arguments: `first` (a string) and `second` (a string)
#   Both strings are whole numbers written as text, such as "5"
#   The function converts both to integers and returns their sum as an integer
# Example: add_text_numbers("5", "7") --> 12
# Example: add_text_numbers("10", "20") --> 30
 
def add_text_numbers(first, second):
    pass
 
 
# 10. Build the function `count_big()` which accepts a single argument `numbers` (a list of integers)
#   The function uses a for loop to count how many numbers in the list are greater than 10, and returns that count
# Example: count_big([4, 12, 30, 7]) --> 2
# Example: count_big([1, 2, 3]) --> 0
 
def count_big(numbers):
    pass

