#Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
def even_or_odd(number):
    if number%2 == 0:
        return "Even"
    else:
        return "Odd"

#We need a function that can transform a number (integer) into a string.
def number_to_string(num):
    return str(num)

#Return the number (count) of vowels in the given string.
#We will consider a, e, i, o, u as vowels for this Kata (but not y).
def get_count(sentence):
    vowels = "aeiou"
    vowel_count = 0
    for char in sentence:
        if char in vowels:
            vowel_count += 1
    return vowel_count