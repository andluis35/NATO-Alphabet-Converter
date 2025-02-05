import pandas

def get_encoded_letter(key, code_dictionary):
    return code_dictionary[key]

def encode_word(word, code_dictionary):
    encoded_word = []
    for letter in word:
        encoded_letter = get_encoded_letter(letter.upper(), code_dictionary)
        encoded_word.append(encoded_letter)
    return encoded_word

def set_phonetic_alphabet_dictionary():
    phonetic_alphabet_dataframe = pandas.read_csv("./nato_phonetic_alphabet.csv")
    phonetic_alphabet_dictionary = {row.letter: row.code for (index, row) in phonetic_alphabet_dataframe.iterrows()}
    return phonetic_alphabet_dictionary

def delete_spaces(string):
    return string.replace(" ", "")

def print_encoded_word(word):
    print(f"RESULT: {word}")

def start_encoding():
    phonetic_alphabet = set_phonetic_alphabet_dictionary()
    chosen_word = input("Type a word to convert: ")
    chosen_word = delete_spaces(chosen_word)

    word_in_phonetic = encode_word(chosen_word, phonetic_alphabet)
    print_encoded_word(word_in_phonetic)

start_encoding()