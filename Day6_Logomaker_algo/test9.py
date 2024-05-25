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

def is_word_in_dictionary(word):
    return bool(wordnet.synsets(word))

def get_permutations_and_synonyms_antonyms():
    # Get user input
    user_input = input("Enter a word: ")

    # Get synonyms and antonyms
    synonyms, antonyms = get_synonyms_antonyms(user_input)

    # Get permutations
    permutations = list(itertools.permutations(user_input))
    num_permutations = len(permutations)

    # Display permutations that are valid words
    print("\nPermutations (valid words):")
    valid_words = [ ''.join(perm) for perm in permutations if is_word_in_dictionary(''.join(perm)) ]
    for word in valid_words:
        print(word)
    print(f"\nTotal number of valid permutations: {len(valid_words)}")

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
