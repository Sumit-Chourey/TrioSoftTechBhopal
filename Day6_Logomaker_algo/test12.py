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

def get_permutations_and_combinations():
    # Get user input
    user_input = input("Enter a word: ")
    n = len(user_input)

    # Get synonyms and antonyms
    synonyms, antonyms = get_synonyms_antonyms(user_input)

    # Get permutations
    print("---------------------------------------------------------------------------------------")
    print("\nPermutations (valid words):")
    for perm in itertools.permutations(user_input):
        perm_word = ''.join(perm)
        if is_word_in_dictionary(perm_word):
            print(perm_word)
    print(f"\nTotal number of valid permutations: {sum(1 for perm in itertools.permutations(user_input) if is_word_in_dictionary(''.join(perm)))}")

    # Get combinations
    print("---------------------------------------------------------------------------------------")
    print("\nCombinations (valid words):")
    for r in range(1, n + 1):
        for comb in itertools.combinations(user_input, r):
            comb_word = ''.join(comb)
            if is_word_in_dictionary(comb_word):
                print(comb_word)
    print(f"\nTotal number of valid combinations: {sum(1 for r in range(1, n + 1) for comb in itertools.combinations(user_input, r) if is_word_in_dictionary(''.join(comb)))}")

    # Display synonyms
    print("---------------------------------------------------------------------------------------")
    print("\nSynonyms (valid words):")
    valid_synonyms = [synonym for synonym in synonyms if is_word_in_dictionary(synonym)]
    if valid_synonyms:
        for synonym in valid_synonyms:
            print(synonym)
    else:
        print("No synonyms found.")

    # Display antonyms
    print("---------------------------------------------------------------------------------------")
    print("\nAntonyms (valid words):")
    valid_antonyms = [antonym for antonym in antonyms if is_word_in_dictionary(antonym)]
    if valid_antonyms:
        for antonym in valid_antonyms:
            print(antonym)
    else:
        print("No antonyms found.")

if __name__ == "__main__":
    get_permutations_and_combinations()
