''' Find All Words Stored in Trie '''

from Trie import Trie
from TrieNode import TrieNode


# Create Trie => trie = Trie()
# TrieNode => {children, is_end_word, char}
# Insert a Word => trie.insert(key)
# Search a Word => trie.search(key) return true or false
# Delete a Word => trie.delete(key)
def get_words(root, result, level, word):
    if root.is_end_word:
        temp = ""
        for x in range(level):
            temp += word[x]
        result.append(str(temp))

    for i in range(26):
        if root.children[i]:
            word[level] = chr(i+ ord('a'))
            get_words(root.children[i], result, level + 1, word)

def find_words(root):
    result = []
    word = [None] * 20  # assuming max level is 20
    get_words(root, result, 0, word)
    return result



if __name__ == "__main__":
    # Input keys (use only 'a' through 'z')
    keys = ["the", "a", "there", "answer", "any",
            "by", "bye", "their", "abc"]

    t = Trie()

    # Construct Trie
    for words in keys:
        t.insert(words)

    print(find_words(t.root))
