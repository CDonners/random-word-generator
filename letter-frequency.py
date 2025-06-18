# Could be used for something possibly? 

import json
from collections import Counter

DICT_PATH = 'dictionary.json'

with open(DICT_PATH, 'r') as file:
    data = json.load(file)

letter_counter = Counter()

for word in data.keys():
    for letter in word:
        if letter.isalpha():
            letter_counter[letter.lower()] += 1

for letter, count in sorted(letter_counter.items()):
    print(f"{letter}: {count}")
