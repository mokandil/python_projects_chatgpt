def love_score(name1, name2):
    """
    This function takes two names as inputs and calculates their love score.

    The love score is calculated by counting the number of occurrences of the letters 
    't', 'r', 'u', 'e', 'l', 'o', 'v', 'e' in the lowercase versions of the input names. 
    The total count of 't', 'r', 'u', 'e' letters and the total count of 'l', 'o', 'v', 'e' letters 
    are concatenated as two strings, and then the resulting two strings are concatenated as an integer.

    If the resulting love score is less than 10 or greater than 90, the function should print 
    "Your love score is X, you go together like coke and mentos.", where X is the calculated 
    love score. If the love score is between 40 and 50 (inclusive), the function should print 
    "Your love score is X, you are alright together." Otherwise, the function should print 
    "Your love score is X." where X is the calculated love score.

    Parameters:
    name1 (str): The first name.
    name2 (str): The second name.

    Returns:
    None
    """
    name1 = name1.lower()  # Convert name1 to lowercase
    name2 = name2.lower()  # Convert name2 to lowercase
    
    true_count = 0  # Initialize the count of 't', 'r', 'u', 'e' letters to zero
    love_count = 0  # Initialize the count of 'l', 'o', 'v', 'e' letters to zero
    
    # Count the number of occurrences of 't', 'r', 'u', 'e' letters in name1 and name2
    for letter in "true":
        true_count += name1.count(letter) + name2.count(letter)
        
    # Count the number of occurrences of 'l', 'o', 'v', 'e' letters in name1 and name2
    for letter in "love":
        love_count += name1.count(letter) + name2.count(letter)
        
    # Concatenate the counts as two strings, and then the resulting two strings as an integer
    love_score = int(str(true_count) + str(love_count))
    
    # Print the result based on the love score
    if love_score < 10  or love_score > 90:
        print(f"Your love score is {love_score}, you go together like coke and mentos.")
    elif love_score >= 40 and love_score <= 50:
        print(f"Your love score is {love_score}, you are alright together.")
    else:
        print(f"Your love score is {love_score}")

# Test the function with examples
love_score("Angela", "Jack")
love_score("Karl", "Anna")

