# implementation of sll using a stack structure with the head of the list as the top of the stack
class LinkedStack:
    """LIFO Stack implementation using a sll for storage"""

    # ---------Nested node class -------
    class Node:
        """Lightweight nonpublic class for storing a sll"""
        __slots__ = '_element', '_next'  # Streamline memory usage

        def __init__(self, element, next):
            self._element = element
            self._next = next

    # -------Stack methods --------
    def __init__(self):
        "Create an empty stack"
        self._head = None
        self._size = 0

    def __len__(self):
        "Return number of elements in the stack"
        return self._size

    def is_empty(self):
        "Return True if the stack is empty"
        return self._size == 0

    def push(self, e):
        "Add element to top of the stack"
        self._head = self.Node(e, self._head)
        self._size += 1

    def top(self):
        """Return but do not remove the element at the top of the stack.
        Raise Empty Exception if the stack is empty"""

        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def pop(self):
        "Remove and Return the top of the stack"
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer


LList = LinkedStack()


freq = {}
for piece in open('example.txt').read().lower().split():
    # only consider alphabetic character within this piece
    word = ''.join(c for c in piece if c.isalpha())

    if word:
        freq[word] = 1 + freq.get(word, 0)

    max_word = ''
    max_count = 0
    for (w, c) in freq.items():
        if c > max_count:
            max_word = w
            max_count = c

print(f"The most frequent word is {max_word}")
print(f"The number of occurence is {max_count}")


def insertion_sort(A):
    "Sort list of comparable elements in nondecreasing order"
    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j-1] > cur:
            A[j] = A[j - 1]
            j -= 1
        A[j] = cur


nums = [1, 7, 8, 4, 5, 2, 1, 3, 5, 6, 8, 12, 13, 11, 9]
insertion_sort(nums)
print(nums)


def merge(S1, S2, S):
    "Merge two sorted python lists"
    i = j = 0
    while i+j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i]
            i += 1
        else:
            S[i+j] = S2[j]
            j += 1
    return S


def merge_sort(S):
    "Sort a python list based on the merge-sort algorithm"
    n = len(S)
    if n < 2:
        return  # nothing to sort
    # divide
    mid = n // 2
    S1 = S[0: mid]
    S2 = S[mid: n]
    # conquer(with recursion)
    merge_sort(S1)
    merge_sort(S2)
    print(S1, S2)
    # merge results
    merge(S1, S2, S)


nums = [2, 1, 15, 11, 24, 21, 8, 0, 4, 32, 19, 5, 4, 7]
merge_sort(nums)
print(nums)
