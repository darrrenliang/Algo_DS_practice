''' Total Number of Words in a Trie '''

from Trie import Trie
from TrieNode import TrieNode


# TrieNode => {children, is_end_word, char}
def total_words(root):
    count = 0

    if root.is_end_word:
        count += 1

    for letter in root.children:
        if letter:
            count += total_words(letter)
    return count


if __name__ == "__main__":
    # Input keys (use only 'a' through 'z')
    keys = ["the", "a", "there", "answer", "any",
            "by", "bye", "their", "abc"]

    t = Trie()

    # Construct Trie
    for words in keys:
        t.insert(words)

    print(total_words(t.root))
