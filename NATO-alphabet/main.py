# {new_key:new_value for (index, row) in df.iterrows()

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row['letter']:row['code'] for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Digit something: ").upper()
word_nato = [nato_dict[letter] for letter in word if letter in nato_dict.keys()]
print(word_nato)
