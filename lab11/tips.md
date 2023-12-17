---
marp: true
---

# Exercise 1: Counting words

 - Use a dictionary to keep track of the number of occurrences
 - Each word is a key, and the value is a counter
 - You increment the counter each time you see the word

___

# Exercise 2: Counting words (2) - Most frequent words

 - Start from the dictionary created previously
 - You can not sort the dictionary by value directly
 - You can create a list of tuples `(value, key)` and sort it

___

# Exercise 3: Strings and set operations

 - When working directly with strings you will have to implement the operations manually.
 - After transforming the string to sets, remember you can use:
   - `intersection()`
   - `difference()`

___
# Exercise 4: Adding dictionaries
 - This one can be solved by just using dictionaries
 - Just remember to check for the existence of the key before adding

___
# Exercise 5: Prime numbers
 - Use two sets
   - One for all the numbers from 2 to n
   - One for the prime numbers

___

# Summary
 - **Ex1:** Dictionary of the form `words: count`
 - **Ex2:** Create a new container that you can sort by value
 - **Ex3:**
   - With strings: implement the operations manually
   - With sets: use the built-in operations `intersection()` and `difference()`
 - **Ex4:** Can be solved just using dictionaries
 - **Ex5:** Use two sets
    - One for all the numbers from 2 to n
    - One for the prime numbers
