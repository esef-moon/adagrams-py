
import random


def draw_letters(): 
    LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}
    available_letters = []

    for letter in LETTER_POOL.keys():
        for num in range(LETTER_POOL[letter]):
            available_letters.append(letter)

    chosen_letters = random.sample(available_letters,k=10)  

    return chosen_letters



def uses_available_letters(word, letter_bank):

    word_in_caps = word.upper()
    letter_bank_copy = letter_bank.copy()

    for letter in word_in_caps:
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
            is_valid = True
            continue
        else:
            is_valid = False
    return is_valid


def score_word(word):
    score = 0 
    score_values = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10 
    }

    for letter in word:
        score+= score_values[letter]

    return score

def get_highest_word_score(word_list):
    pass