import pandas as pd

# Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato_phonetic_dataframe = pd.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic_dictionary = {row["letter"]: row["code"] for (index, row) in nato_phonetic_dataframe.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.

user_input = input("What is your name: ").upper()
result = [nato_phonetic_dictionary[letter] for letter in user_input]

print(result)
