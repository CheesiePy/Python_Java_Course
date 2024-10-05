# Given string
my_str = "Pikachu is the most boring Pokémon ever!"

# Split the string into a list of substrings, separated by "most"
word_list = my_str.split("most")  # ['Pikachu is the ', ' boring Pokémon ever!']
print(word_list)

# Some More Useful String Methods

# 1. .upper() - Converts all characters to uppercase
upper_str = my_str.upper()
print(upper_str)  # Output: 'PIKACHU IS THE MOST BORING POKÉMON EVER!'

# 2. .lower() - Converts all characters to lowercase
lower_str = my_str.lower()
print(lower_str)  # Output: 'pikachu is the most boring pokémon ever!'

# 3. .title() - Converts the first character of each word to uppercase
title_str = my_str.title()
print(title_str)  # Output: 'Pikachu Is The Most Boring Pokémon Ever!'

# 4. .strip() - Removes leading and trailing whitespace characters
extra_spaces = "   Pikachu is cute!   "
stripped_str = extra_spaces.strip()
print(stripped_str)  # Output: 'Pikachu is cute!'

# 5. .replace(old, new) - Replaces all occurrences of a substring with another substring
replaced_str = my_str.replace("boring", "exciting")
print(replaced_str)  # Output: 'Pikachu is the most exciting Pokémon ever!'

# 6. .find(substring) - Returns the index of the first occurrence of the substring
index = my_str.find("boring")
print(index)  # Output: 21 (index where "boring" starts)

# 7. .count(substring) - Returns the number of occurrences of a substring
count = my_str.count("the")
print(count)  # Output: 1

# 8. .startswith(substring) - Checks if the string starts with the given substring
starts_with = my_str.startswith("Pikachu")
print(starts_with)  # Output: True

# 9. .endswith(substring) - Checks if the string ends with the given substring
ends_with = my_str.endswith("ever!")
print(ends_with)  # Output: True

# 10. .join(iterable) - Joins a list of strings into a single string with a delimiter
words = ["Pikachu", "is", "the", "best!"]
joined_str = " ".join(words)
print(joined_str)  # Output: 'Pikachu is the best!'

# 11. .isalpha() - Checks if all characters in the string are alphabetic
alpha_str = "Pokemon"
is_alpha = alpha_str.isalpha()
print(is_alpha)  # Output: True

# 12. .isdigit() - Checks if all characters in the string are digits
digit_str = "12345"
is_digit = digit_str.isdigit()
print(is_digit)  # Output: True

# Example usage with functions
def add(x, y):
    print(x + y)

def greet(name):
    print("Hello", name)

add(5, 10)  # Output: 15
greet("Ash")  # Output: Hello Ash

# Important String Facts

# 1. Strings are Immutable
#    - Strings in Python cannot be changed after they are created. When you use a string method like .replace() or .upper(), it creates a new string, leaving the original string unchanged.
original = "Hello"
new_string = original.replace("H", "J")
print(original)      # Output: 'Hello' (remains unchanged)
print(new_string)    # Output: 'Jello'

# 2. Indexing and Slicing
#    - Strings can be indexed (zero-based) to access individual characters.
#    - Negative indexing starts from the end of the string.
#    - Slicing can be used to extract substrings.
my_str = "Pikachu"
print(my_str[0])    # Output: 'P' (first character)
print(my_str[-1])   # Output: 'u' (last character)
print(my_str[1:4])  # Output: 'ika' (from index 1 to 3)

# 3. Escape Characters
#    - Use the backslash \ for special characters (e.g., \n for a newline or \' to include a quote).
quote = "Pikachu said, \"Pika Pika!\""
print(quote)  # Output: 'Pikachu said, "Pika Pika!"'

# 4. String Formatting
#    - You can use formatted strings (f-strings) for easier variable inclusion in strings.
name = "Pikachu"
power = "Electric"
description = f"{name} is a {power} type Pokémon!"
print(description)  # Output: 'Pikachu is an Electric type Pokémon!'

# 5. Concatenation
#    - You can concatenate strings using the + operator.
first = "Pika"
second = "chu"
full_name = first + second
print(full_name)  # Output: 'Pikachu'