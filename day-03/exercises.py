"""###EXERCISE 01: Human Class

Create a new class `Human` which has required attributes `first_name:str`, `last_name:str`, `age:int`, and `is_hungry:bool`.

A `Human` instance has a `__repr__` that shows their attributes.

A `Human` instance has a `full_name()` method which returns their `first_name` and `last_name` in a single string, for example `"Bob Dylan"`.

A `Human` instance has an `order_drinks()` method which either returns `"Party time!"` if their age is 21 or older and returns `"Denied"` if their age is 20 or younger.

A `Human` instance has an `eat()` method which sets their attribute `is_hungry` equal to `True`.

A `Human` instance has a `win_lottery()` method which sets their attribute `address` equal to `"Disneyworld"`.

A `Human` instance has a `change_first_name()` method which creates an input with the prompt `"Change Name >>>"`. When a user completes the input the `name` attribute changes to their input.

---
"""

class Human:
	pass

"""###EXERCISE 02: MovieReview Class

Create a class `MovieReview` which has required attributes `movie_title:str`, `reviewer_name:str`, `score:int`, `date_reviewed:datetime.date`.

You may need to look up how to use `datetime.date` (hint: you'll need `from datetime import date`)`


Create an instance method `pretty_print()` which prints the review like so: `"<movie_title> review by <reviewer_name> on <date_reviewed>: <score> / 5 stars"`.

Example: `land_before_time.pretty_print()` >>> `"Land Before Time review by Fred Flintstone on 2014-4-12: 5/5 stars"`

Create an instance method `increase_score()` which increases that movie's score by 1 but not above 5.

Create an instance method `update_review()`. This accepts an argument of a `new_score` and optionally a `new_reviewer`. This updates the `score` and sets the `date_reviewed` to today.  If `new_reviewer` was passed this will also update the `reviewer_name` and if not it will retain the previous `reviewer_name`.

Example: `land_before_time.update_review(4)` # score changed to `4`, date becomes today, reviewer is still `"Fred Flinstone"`

Example: `land_before_time.update_review(5, "Littlefoot")` # score changed to `5`, date becomes today, reviewer becomes `"Littlefoot"`

Create a class method `review_bomb()` which accepts a `movie_title` and `num_reviews`. This generates a review `num_reviews` times for the `movie_title` each with a `score` of 1, a `reviewer_name` of `Statler & Waldorf`, and a `date_reviewed` of today. Return all instances in a list.

Example: `MovieReview.review_bomb("Plan 9 From Outer Space", 10)` >>> creates 10 reviews for "Plan 9 From Outer Space"

---
"""

class MovieReview:
	pass