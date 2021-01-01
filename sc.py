data = []

for i in range(10):
    data.insert(i // 2, i)


print(data)


class GameEntry:
    """Represents one entry of a list of high scores"""

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return "({0}, {1})".format(self._name, self._score)


class ScoreBoard:
    """Fixed length sequence of scores in nondecreasing order"""

    def __init__(self, capacity=10):
        "Initialize board with maximum capacity"
        self._board = [None] * capacity
        self._n = 0  # Number of actual entries

    def get_item(self, k):
        "Return items at index k"
        return self._board[k]

    def __str__(self):
        "Return string representation of the high scores"
        return '\n'.join(str(self._board[j] for j in range(self._n)))

    def add(self, entry):
        "Consider adding entries to high scores"
        score = entry.get_score()

        # Does entry qualify for leaderboard?
        # Answer is yes if board not full or score is higher than last entry
        good = self._n < len(
            self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):
                self._n += 1

            # Shift lower scores rightward to make room for new entry
            j = self._n - 1
            while j > 0 and self._board[j-1].get_score() < score:
                self._board[j] = self._board[j-1]
                j -= 1
            self._board[j] = entry


characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
              'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

class CaesarSipher:
    """Encryption and decryption class using caesar cipher"""
    def __init__(self, shift):
        "Construct Caesar cipher using given integer shift for rotation"
        encoder = [None] * 26
        decoder = [None] * 26
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)
        

    def encrypt(self, message):
        "Return an encrypted message"
        return self._transform(message, self._forward)
    
    def decrypt(self, secret):
        "Return decrypted message"
        return self._transform(secret, self._backward)

    def _transform(self, original, code):
        "Utility to perform transformation based on given code string"
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
        return ''.join(msg)


if __name__ == "__main__":
    cipher = CaesarSipher(3)
    message = "MR. BEAN IS IN THE HOUSE"
    coded = cipher.encrypt(message)
    print('Secret: ', coded)
    answer = cipher.decrypt(coded)
    print("message: ", answer)


matrix = [[0] * 3 for i in range(4)]
matrix[0][1]  =4
data = []
data.append(5)
print(matrix)
    
