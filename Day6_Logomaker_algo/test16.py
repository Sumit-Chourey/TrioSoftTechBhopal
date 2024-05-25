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

def get_valid_substrings(word):
    valid_substrings = []
    n = len(word)
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = word[i:j]
            if is_word_in_dictionary(substring) and len(substring) > 2:
                valid_substrings.append(substring)
    return valid_substrings

def get_permutations_and_combinations():
    # Get user input
    user_input = input("Enter a word: ")

    # Get synonyms and antonyms
    synonyms, antonyms = get_synonyms_antonyms(user_input)

    # Get valid substrings
    valid_substrings = get_valid_substrings(user_input)

    # Get permutations
    print("---------------------------------------------------------------------------------------")
    print("\nPermutations (valid words):")
    perms = []
    for substring in valid_substrings:
        for perm in itertools.permutations(substring):
            perm_word = ''.join(perm)
            if is_word_in_dictionary(perm_word):
                perms.append(perm_word)
    bubble_sort(perms)
    for perm_word in perms:
        if len(perm_word)>2:
            print(perm_word)
    print(f"\nTotal number of valid permutations: {len(perms)}")

    # Get combinations
    print("---------------------------------------------------------------------------------------")
    print("\nCombinations (valid words):")
    combs = []
    for substring in valid_substrings:
        for r in range(1, len(substring) + 1):
            for comb in itertools.combinations(substring, r):
                comb_word = ''.join(comb)
                if is_word_in_dictionary(comb_word):
                    combs.append(comb_word)
    bubble_sort(combs)
    for comb_word in combs:
        if len(comb_word)>2:
            print(comb_word)
    print(f"\nTotal number of valid combinations: {len(combs)}")

    # Display synonyms
    print("---------------------------------------------------------------------------------------")
    print("\nSynonyms (valid words):")
    bubble_sort(synonyms)
    for synonym in synonyms:
        print(synonym)

    # Display antonyms
    print("---------------------------------------------------------------------------------------")
    print("\nAntonyms (valid words):")
    bubble_sort(antonyms)
    for antonym in antonyms:
        print(antonym)

if __name__ == "__main__":
    get_permutations_and_combinations()
