# ChatGPT Prompt to generate love_score.py

Write a function love_score(name1, name2) that takes two names as inputs and calculates their love score.

The love score is calculated by counting the number of occurrences of the letters 't', 'r', 'u', 'e', 'l', 'o', 'v', 'e' in the lowercase versions of the input names. The total count of 't', 'r', 'u', 'e' letters and the total count of 'l', 'o', 'v', 'e' letters are concatenated as two strings, and then the resulting two strings are concatenated as an integer.

If the resulting love score is less than 10 or greater than 90, the function should print "Your love score is X, you go together like coke and mentos.", where X is the calculated love score. If the love score is between 40 and 50 (inclusive), the function should print "Your love score is X, you are alright together." Otherwise, the function should print "Your love score is X." where X is the calculated love score.

Make sure to include a docstring for the function and comment your code to explain how it works.