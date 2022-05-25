# ''' Word Formation From a Dictionary Using Trie '''

from Trie import Trie
from TrieNode import TrieNode


def is_formation_possible(dct, word):

    # Create Trie and insert dctionary elements in it
    trie = Trie()
    for elem in dct:
        trie.insert(elem)

    # Get Root
    current = trie.root

    # Iterate all the letters of the word
    for i in range(len(word)):
        # get index of the character from Trie
        char = trie.get_index(word[i])

        # if the prefix of word does not exist, word would not either
        if current.children[char] is None:
            return False

        # if the substring of the word exists as a word in trie,
        # check whether rest of the word also exists,
        # if it does return true
        elif current.children[char].is_end_word:
            if trie.search(word[i+1:]):
                print(word[:i + 1], word[i+1:])
                return True

        current = current.children[char]

    return False


keys = ["the", "hello", "there", "answer",
        "any", "educative", "world", "their", "abc"]
print(is_formation_possible(keys, "helloworld"))
