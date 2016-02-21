class Trie(object):
    def __init__(self, is_num=False):
        self.children = [None for _ in range(10)]
        self.is_num = is_num

def add_to_trie(root, word):
    """Returns False if it encounters a word, otherwise adds to the trie and returns true"""
    cur = root
    i = 0
    n = len(word)
    while i < n:
        j = ord(word[i]) - 48
        if cur.children[j] is not None:
            cur = cur.children[j]
            # Check if we just shadowed a word
            if cur.is_num or i == n - 1:
                return False
        else:
            cur.children[j] = Trie(i == n - 1)
            cur = cur.children[j]
        i += 1
    return True

t = int(raw_input())
for _ in range(t):
    n = int(raw_input())
    root = Trie()
    out = "YES"
    changed = False
    for __ in range(n):
        x = raw_input()
        if not changed and not add_to_trie(root, x.strip()):
            out = "NO"
            changed = True
    print out
