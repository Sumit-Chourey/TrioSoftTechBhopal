import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')


import itertools
from nltk.corpus import wordnet

def get_synonyms_antonyms(word):
    synonyms = set()
    antonyms = set()
    
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
            if lemma.antonyms():
                antonyms.add(lemma.antonyms()[0].name())
    
    return list(synonyms), list(antonyms)

def get_permutations_and_combinations():
    # Get user input
    user_input = input("Enter a word: ")
    n = len(user_input)

    # Get synonyms and antonyms
    synonyms, antonyms = get_synonyms_antonyms(user_input)

    # Get permutations and combinations
    permutations = list(itertools.permutations(user_input))
    combinations = []

    for r in range(1, n + 1):
        combinations.extend(itertools.combinations(user_input, r))

    # Count permutations and combinations
    num_permutations = len(permutations)
    num_combinations = len(combinations)

    # Display permutations
    print("\nPermutations:")
    for perm in permutations:
        print(''.join(perm))
    print(f"\nTotal number of permutations: {num_permutations}")

    # Display combinations
    print("\nCombinations:")
    for comb in combinations:
        print(''.join(comb))
    print(f"\nTotal number of combinations: {num_combinations}")

    # Display synonyms and antonyms
    print("\nSynonyms:")
    if synonyms:
        for synonym in synonyms:
            print(synonym)
    else:
        print("No synonyms found.")

    print("\nAntonyms:")
    if antonyms:
        for antonym in antonyms:
            print(antonym)
    else:
        print("No antonyms found.")

if __name__ == "__main__":
    get_permutations_and_combinations()
