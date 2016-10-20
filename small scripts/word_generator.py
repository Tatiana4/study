import random, string

vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxz'
letters = string.ascii_lowercase

letter_input_1 = input("Enter 'v' for vowels, 'c' for consonants or 'l' for any letter: ")
letter_input_2 = input("Enter 'v' for vowels, 'c' for consonants or 'l' for any letter: ")
letter_input_3 = input("Enter 'v' for vowels, 'c' for consonants or 'l' for any letter: ")

def word_gen():
    if letter_input_1 == 'v':
        letter_1 = random.choice(vowels)
    elif letter_input_1 == 'c':
        letter_1 = random.choice(consonants)
    elif letter_input_1 == 'l':
        letter_1 = random.choice(letters)
    else:
        letter_1 = letter_input_1

    if letter_input_2 == 'v':
        letter_2 = random.choice(vowels)
    elif letter_input_2 == 'c':
        letter_2 = random.choice(consonants)
    elif letter_input_2 == 'l':
        letter_2 = random.choice(letters)
    else:
        letter_2 = letter_input_2

    if letter_input_3 == 'v':
        letter_3 = random.choice(vowels)
    elif letter_input_3 == 'c':
        letter_3 = random.choice(consonants)
    elif letter_input_3 == 'l':
        letter_3 = random.choice(letters)
    else:
        letter_3 = letter_input_3

    word = letter_1 + letter_2 + letter_3
    return word

print(word_gen())