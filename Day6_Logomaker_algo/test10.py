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
    permutations = [''.join(perm) for perm in itertools.permutations(user_input)]
    valid_permutations = [word for word in permutations if is_word_in_dictionary(word)]
    
    # Get combinations
    combinations = []
    for r in range(1, n + 1):
        combinations.extend([''.join(comb) for comb in itertools.combinations(user_input, r)])
    valid_combinations = [word for word in combinations if is_word_in_dictionary(word)]

    # Display permutations
    print("---------------------------------------------------------------------------------------")
    print("\nPermutations (valid words):")
    for perm in valid_permutations:
        print(perm)
    print(f"\nTotal number of valid permutations: {len(valid_permutations)}")

    # Display combinations
    print("---------------------------------------------------------------------------------------")
    print("\nCombinations (valid words):")
    for comb in valid_combinations:
        print(comb)
    print(f"\nTotal number of valid combinations: {len(valid_combinations)}")

    # Display synonyms and antonyms
    print("---------------------------------------------------------------------------------------")
    print("\n Synonyms :")
    if synonyms:
        for synonym in synonyms:
            print(synonym)
    else:
        print("No synonyms found.")


    # Display synonyms and antonyms
    print("---------------------------------------------------------------------------------------")
    print("\nAntonyms:")
    if antonyms:
        for antonym in antonyms:
            print(antonym)
    else:
        print("No antonyms found.")

if __name__ == "__main__":
    get_permutations_and_combinations()
