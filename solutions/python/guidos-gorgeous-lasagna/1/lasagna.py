"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME_PER_LAYER = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time (in minutes) as a function of the number of layers.

    Parameters:
        number_of_layers (int): Number of layers you want to add to the lasagna.

    Returns:
        int: The time (in minutes) you would spend making them before cooking derived from 'PREPARATION_TIME_PER_LAYER'.

    Function that takes the number of layers you want to add to the lasagna as
    an argument and returns how many minutes you would spend making the layers before
    baking, based on the `PREPARATION_TIME_PER_LAYER`.
    """
    return PREPARATION_TIME_PER_LAYER * number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate total elapsed time (in minutes).

    Parameters:
        number_of_layers (int): Number of layers you want to add to the lasagna.
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The total ammount of time (in minutes) you have spent in the kitchen cooking..

    Function that takes the number of layers you want to add to the lasagna and 
    the baking time already elapsed as arguments and returns the total ammount of time 
    spent in the kitchen cooking.
    """
    layers_time = preparation_time_in_minutes(number_of_layers)
    return elapsed_bake_time + layers_time