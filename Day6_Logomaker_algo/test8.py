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

def get_permutations_and_synonyms_antonyms():
    # Get user input
    user_input = input("Enter a word: ")

    # Get synonyms and antonyms
    synonyms, antonyms = get_synonyms_antonyms(user_input)

    # Get permutations
    permutations = list(itertools.permutations(user_input))
    num_permutations = len(permutations)

    # Display permutations
    print("\nPermutations:")
    for perm in permutations:
        print(''.join(perm))
    print(f"\nTotal number of permutations: {num_permutations}")

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
    get_permutations_and_synonyms_antonyms()
