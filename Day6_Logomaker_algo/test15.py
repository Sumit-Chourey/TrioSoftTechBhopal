

import itertools
from nltk.corpus import wordnet
import nltk

# Download the required WordNet data
nltk.download('wordnet')
nltk.download('omw-1.4')

def get_synonyms_antonyms(word):
    synonyms = set()
    antonyms = set()
    
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
            if lemma.antonyms():
                antonyms.add(lemma.antonyms()[0].name())
    
    return list(synonyms), list(antonyms)

def is_word_in_dictionary(word):
    return bool(wordnet.synsets(word))

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def get_permutations_and_combinations():
    # Get user input
    user_input = input("Enter a word: ")
    n = len(user_input)

    # Get synonyms and antonyms
    synonyms, antonyms = get_synonyms_antonyms(user_input)

    # Get permutations
    print("---------------------------------------------------------------------------------------")
    print("\nPermutations (valid words):")
    perms = []
    if n > 2:
        for perm in itertools.permutations(user_input):
            perm_word = ''.join(perm)
            if is_word_in_dictionary(perm_word):
                perms.append(perm_word)
        bubble_sort(perms)
        for perm_word in perms:
            if len(perm_word)>2:#we have apply here condition of length of string
                print(perm_word)
        print(f"\nTotal number of valid permutations: {len(perms)}")
    else:
        print("Word length is less than or equal to 2. Permutations not generated.")

    # Get combinations
    print("---------------------------------------------------------------------------------------")
    print("\nCombinations (valid words):")
    combs = []
    if n > 2:
        for r in range(1, n + 1):
            for comb in itertools.combinations(user_input, r):
                comb_word = ''.join(comb)
                if is_word_in_dictionary(comb_word):
                    combs.append(comb_word)
        bubble_sort(combs)
        for comb_word in combs:
            if len(comb_word)>2:
                print(comb_word)
        print(f"\nTotal number of valid combinations: {len(combs)}")
    else:
        print("Word length is less than or equal to 2. Combinations not generated.")

    # Display synonyms
    print("---------------------------------------------------------------------------------------")
    print("\nSynonyms (valid words):")
    valid_synonyms = [synonym for synonym in synonyms if is_word_in_dictionary(synonym)]
    bubble_sort(valid_synonyms)
    if valid_synonyms:
        for synonym in valid_synonyms:
            print(synonym)
    else:
        print("No synonyms found.")

    # Display antonyms
    print("---------------------------------------------------------------------------------------")
    print("\nAntonyms (valid words):")
    valid_antonyms = [antonym for antonym in antonyms if is_word_in_dictionary(antonym)]
    bubble_sort(valid_antonyms)
    if valid_antonyms:
        for antonym in valid_antonyms:
            print(antonym)
    else:
        print("No antonyms found.")

if __name__ == "__main__":
    get_permutations_and_combinations()
