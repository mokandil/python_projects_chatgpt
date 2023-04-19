def is_leap_year(year):
    """
    This function takes a year as an input and returns whether it's a leap year or not.

    A leap year is a year that is divisible by 4, except for century years (ending in 00), 
    which must be divisible by 400 to be a leap year.

    Parameters:
    year (int): The year to check.

    Returns:
    str: "Leap" if the input year is a leap year, and "Not leap" otherwise.
    """
    is_leap = False  # Initialize is_leap to False
  
    if year % 4 == 0:  # If the year is divisible by 4
        is_leap = True  # Then it's a leap year

        if year % 100 == 0:  # If the year is a century year
            is_leap = False  # Then it's not a leap year

            if year % 400 == 0:  # Except if the year is divisible by 400
                is_leap = True  # Then it's a leap year

    # Set res to "Leap" if is_leap is True, "Not leap" otherwise
    res = "Leap" if is_leap else "Not leap"
  
    # Print the result
    print(f"{year} is {res}")    

# Test the function with an example
year = 2016
is_leap_year(year)
