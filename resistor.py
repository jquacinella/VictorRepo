# Ask the user for first color
first_color = input("Please enter in the first color: ")

# Ask the user for second color
second_color = input("Please enter in the second color: ")

# Ask the user for third color
third_color = input("Please enter in the third color: ")

# Ask the user for fourth color
fourth_color = input("Please enter in the fourth color: ")

# Mapping between color and value for first three bands
band_mapping = {
    "black": '0',
    "brown": '1',
    "red": '2',
    "orange": '3',
    "yellow": '4',
    "green": '5',
    "blue": '6',
    "violet": '7',
    "grey": '8',
    "white": '9'
}

# Mapping between color and multipler for fourth band
multiplier_mapping = {
    "black": 10 ** 0,
    "brown": 10 ** 1,
    "red": 10 ** 2,
    "orange": 10 ** 3,
    "yellow": 10 ** 4,
    "green": 10 ** 5,
    "blue": 10 ** 6,
    "violet": 10 ** 7,
    "gold": 10 ** -1,
    "silver": 10 ** -2
}

# Lookup band values from the dictionary from the user inputs
first_band = band_mapping[first_color]
second_band = band_mapping[second_color]
third_band = band_mapping[third_color]

# Lookup the multiplier from the multiplier_mapping from the user input
multiplier = multiplier_mapping[fourth_color] 

# Construct the number by concatenating the digits into an int and then multiplying
final_value = int(first_band + second_band + third_band) * multiplier

# Print out final value
print("Final value is {} in Ohms".format(final_value))