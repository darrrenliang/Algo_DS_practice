''' List Sort Using Trie '''

from Trie import Trie
from TrieNode import TrieNode


def get_words(root, result, level, word):
    # Leaf denotes end of a word
    if (root.is_end_word):
        # current word is stored till the 'level' in the character array
        temp = ""
        for x in range(level):
            temp += word[x]
        result.append(temp)

    for i in range(26):
        if (root.children[i] is not None):
            # Non-null child, so add that index to the character array
            word[level] = chr(i + ord('a'))
            get_words(root.children[i], result, level + 1, word)


def sort_list(arr):
    result = []

    # Creating Trie and Inserting words from array
    trie = Trie()
    for word in arr:
        trie.insert(word)

    word = [''] * 20
    get_words(trie.root, result, 0, word)
    return result


if __name__ == "__main__":
    # Input keys (use only 'a' through 'z')
    keys = ["the", "a", "there", "answer", "any",
            "by", "bye", "their", "abc"]

    print(sort_list(keys))
