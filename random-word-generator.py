import json
import random

# Constants
DICT_PATH = 'dictionary.json'
LETTERS = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j', 10:'k', 11:'l', 12:'m', 13:'n', 14:'o', 15:'p', 16:'q', 17:'r', 18:'2', 19:'t', 20:'u', 21:'v', 22:'w', 23:'x', 24:'y', 25:'z'}

# Opening dictionary JSON
with open(DICT_PATH, 'r') as file:
    dictionary = json.load(file)

# Letter Generation
def generate_letter(min_length):
    # Variables
    bad_words = []
    attempts = 0
    generated_lengths = []
    unsuccessful_lengths = []
    while True:
        # Looped Variables
        attempts += 1
        word_length = random.randint(2,15)
        word = ""
        # I wanna see the stats on the lengths generated so add current length to the lists
        generated_lengths.append(word_length)
        
        # Loops for n times to generate the letters
        for i in range(word_length):
            letter_generated = LETTERS[random.randint(0,25)] # Generate a number and get the corresponding letter
            word = word + letter_generated  #Add the letter to the word
        # Check if generated word is real
        if word in dictionary.keys():
            if len(word) >= min_length:
                #Make word lengths readable
                indiv_lengths = list(set(generated_lengths))
                readable_lengths = {i:generated_lengths.count(i) for i in indiv_lengths}
                indiv_unsuccessful_lengths = list(set(unsuccessful_lengths))
                readable_unsuccessful_lengths = {i:unsuccessful_lengths.count(i) for i in indiv_unsuccessful_lengths}
                
                print(f"""
After {attempts} attempts '{word}' was generated!
It's {word_length} letters long
{word}: {dictionary[word]}

Number of Failed Words:
{len(bad_words)}

Failed Word Lengths:
{readable_unsuccessful_lengths}

Word Lengths: 
{readable_lengths}""")
                break
            else:
                bad_words.append(word)
                unsuccessful_lengths.append(word_length)
            
        
generate_letter(6)