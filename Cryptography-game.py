###### Daniel Borrell Diaz  ######## 100909286

"""I Daniel Borrell Diaz 100909286 Group 2 have not given, received,
or used any unauthorized assistance."""

##################### Program 1: Final_Project.py##############################

import random
from math import ceil


class Message:  # The main parent class
    def __init__(self, text):
        self.text = text

    def Randomizer(self):  # Returns a random encryption class
        return random.choice(
            [
                Substitution(self.text),
                Playfair(self.text),
                Caesar(self.text),
                Transposition(self.text),
                Product(self.text),
                RSA(self.text),
            ]
        )

    def display(
        self, messages
    ):  # Prints the cipher used, original text, encrypted text, and decrypted text
        for msg in messages:
            print(f"\nOriginal Text: {msg['Original Text']}")
            print(f"Encrypted Text: {msg['Encrypted Text']}")
            print(f"Decrypted Text: {msg['Decrypted Text']}")
            print(f"Cipher Used: {msg['Cipher Used']}")


class plaintextMsg(
    Message
):  # This class calls the encrypt method of the randomly selected encryption class which is a child class of Message
    def __init__(self, text, rand):
        super().__init__(text)
        self.rand = rand

    def process(self):  # Calls the encrypt of the random class
        return self.rand.encrypt()


class ciphertextMsg(
    Message
):  # This class calls the decrypt method of the randomly selected decryption class which is a child class of Message
    def __init__(self, text, rand):
        super().__init__(text)
        self.rand = rand

    def process(self, encrypted_text):  # Calls the decrypt of the random class
        return self.rand.decrypt(encrypted_text)


class Substitution(Message):  # The substition class which is a child class of Message
    def __init__(self, text):
        super().__init__(text)

    def encrypt(self):  # encryption of the substitution class
        word_list = "abcdefghijklmnopqrstuvwxyz"
        encryptword = ""

        global sub_key

        sub_key = random.randint(1, 16)

        for x in self.text:
            if x.isalpha():
                upper = x.isupper()
                x = x.lower()

                if x in word_list:
                    index = (word_list.index(x) + sub_key) % 26
                    encryptx = word_list[index]

                    if upper:
                        encryptx = encryptx.upper()

                    encryptword = encryptword + encryptx
                else:
                    encryptword = encryptword + x
            else:
                encryptword = encryptword + x

        return encryptword

    def decrypt(self, encrypted_text):  # decryption of the substitution class
        word_list = "abcdefghijklmnopqrstuvwxyz"
        decryptword = ""

        for x in encrypted_text:
            if x.isalpha():
                upper = x.isupper()
                x = x.lower()

                if x in word_list:
                    index = (word_list.index(x) - sub_key) % 26
                    decryptx = word_list[index]

                    if upper:
                        decryptx = decryptx.upper()

                    decryptword = decryptword + decryptx
                else:
                    decryptword = decryptword + x
            else:
                decryptword = decryptword + x

        return decryptword


class Playfair(Message):  # The Playfair class which is a child class of Message
    def __init__(self, text):
        super().__init__(text)
        self.key_matrix = [
            ["S", "K", "A", "M", "E"],
            ["Q", "U", "I", "C", "K"],
            ["B", "R", "O", "W", "N"],
            ["F", "O", "X", "J", "U"],
            ["L", "Y", "D", "G", "H"],
        ]

    def encrypt(self):  # encryption of the Playfair class
        plaintext = self.text.upper().replace("J", "I")
        encrypted_text = ""
        for i in range(0, len(plaintext), 2):
            pair = plaintext[i : i + 2]
            encrypted_text += self.encrypt_pair(pair)
        return encrypted_text

    def decrypt(self, encrypted_text):  # decryption of the Playfair class
        decrypted_text = ""

        if len(encrypted_text) % 2 != 0:
            encrypted_text += "X"

        for i in range(0, len(encrypted_text), 2):
            pair = encrypted_text[i : i + 2]
            decrypted_text += self.decrypt_pair(pair)

        decrypted_text = decrypted_text.rstrip("X")

        return decrypted_text

    def encrypt_pair(self, pair):  # encryption pair of the Playfair class
        if len(pair) == 1:
            pair += "X"

        char1, char2 = pair[0], pair[1]
        position1 = self.get_position(char1)
        position2 = self.get_position(char2)

        if position1 is not None and position2 is not None:
            row1, col1 = position1
            row2, col2 = position2

            if row1 == row2:
                return self.get_char(row1, (col1 + 1) % 5) + self.get_char(
                    row2, (col2 + 1) % 5
                )
            elif col1 == col2:
                return self.get_char((row1 + 1) % 5, col1) + self.get_char(
                    (row2 + 1) % 5, col2
                )
            else:
                return self.get_char(row1, col2) + self.get_char(row2, col1)
        else:
            return pair

    def decrypt_pair(self, pair):  # decryption pair of the Playfair class
        char1, char2 = pair[0], pair[1]
        position1 = self.get_position(char1)
        position2 = self.get_position(char2)

        row1, col1 = position1
        row2, col2 = position2

        if row1 == row2:
            decrypted_text = self.get_char(row1, (col1 - 1) % 5) + self.get_char(
                row2, (col2 - 1) % 5
            )
        elif col1 == col2:
            decrypted_text = self.get_char((row1 - 1) % 5, col1) + self.get_char(
                (row2 - 1) % 5, col2
            )
        else:
            decrypted_text = self.get_char(row1, col2) + self.get_char(row2, col1)

        return decrypted_text

    def get_position(self, char):  # Gets the position from the key matrix
        char = char.upper()
        if char == "J":
            char = "I"
        for i in range(5):
            for j in range(5):
                if self.key_matrix[i][j] == char:
                    return i, j
        return 0, 0

    def get_char(self, row, col):
        return self.key_matrix[row][col]


class Caesar(Message):  # The Caesar class which is a child class of Message
    def __init__(self, text):
        super().__init__(text)

    def encrypt(self):  # encryption of the Caesar class

        global shift

        shift = random.randint(1, 16)

        encrypted_text = ""

        for i in self.text:
            if i.isalpha():
                upper = i.isupper()
                i = i.lower()
                index = (ord(i) - ord("a") + shift) % 26
                encrypted_i = chr(index + ord("a"))

                if upper:
                    encrypted_i = encrypted_i.upper()

                encrypted_text += encrypted_i
            else:
                encrypted_text += i

        return encrypted_text

    def decrypt(self, encrypted_text):  # decryption of the Caesar class
        decrypted_text = ""

        for i in encrypted_text:
            if i.isalpha():
                upper = i.isupper()
                i = i.lower()
                index = (ord(i) - ord("a") - shift) % 26
                decrypted_i = chr(index + ord("a"))

                if upper:
                    decrypted_i = decrypted_i.upper()

                decrypted_text += decrypted_i
            else:
                decrypted_text += i

        return decrypted_text


class Transposition(
    Message
):  # The Transposition class which is a child class of Message
    def __init__(self, text):
        super().__init__(text)
        self.key = [2, 1, 3]

    def encrypt(self):  # encryption of the Transposition class
        num_cols = len(self.key)
        num_rows = ceil(len(self.text) / num_cols)

        matrix = [
            list(self.text[i : i + num_cols])
            for i in range(0, len(self.text), num_cols)
        ]

        if len(matrix[-1]) < num_cols:
            matrix[-1].extend([""] * (num_cols - len(matrix[-1])))

        rearranged_matrix = [[""] * num_cols for _ in range(num_rows)]
        for i, col in enumerate(self.key):
            for j in range(num_rows):
                rearranged_matrix[j][col - 1] = matrix[j][i]

        encrypted_text = "".join("".join(row) for row in rearranged_matrix)

        return encrypted_text

    def decrypt(self, encrypted_text):  # decryption of the Transposition class
        num_cols = len(self.key)
        num_rows = ceil(len(encrypted_text) / num_cols)

        matrix = [[""] * num_cols for _ in range(num_rows)]

        index = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if index < len(encrypted_text):
                    matrix[i][j] = encrypted_text[index]
                    index += 1

        rearranged_matrix = [[""] * num_cols for _ in range(num_rows)]
        for i, col in enumerate(self.key):
            for j in range(num_rows):
                rearranged_matrix[j][col - 1] = matrix[j][i]

        decrypted_text = "".join("".join(row) for row in rearranged_matrix)

        return decrypted_text


class Product(Message):  # The Product class which is a child class of Message
    def __init__(self, text):
        super().__init__(text)

    def encrypt(self):  # encryption of the Product class
        caesar_cipher = Caesar(self.text)
        transposition_cipher = Transposition(caesar_cipher.encrypt())
        encrypted_text = transposition_cipher.encrypt()

        return encrypted_text

    def decrypt(self, encrypted_text):  # decryption of the Product class
        transposition_cipher = Transposition(self.text)
        decrypted_transposition = transposition_cipher.decrypt(encrypted_text)

        caesar_cipher = Caesar(decrypted_transposition)
        decrypted_text = caesar_cipher.decrypt(decrypted_transposition)

        return decrypted_text


class RSA(Message):  # The RSA class which is a child class of Message
    def __init__(self, text):
        super().__init__(text)

    def encrypt(self):  # encryption of the RSA class
        p = 61
        q = 53
        n = p * q
        e = 17
        encrypted_text = [pow(ord(i), e, n) for i in self.text]

        return encrypted_text

    def decrypt(self, encrypted_text):  # encryption of the RSA class
        p = 61
        q = 53
        n = p * q
        d = 2753

        decrypted_integers = [pow(i, d, n) for i in encrypted_text]
        decrypted_text = "".join([chr(integer) for integer in decrypted_integers])

        return decrypted_text


print("Welcome To The Cipher Game\n")

messages = []

while True:  # Checks for errors mainly input errors from the user
    try:
        text = input("Enter Your Message (Type 'Stop' to End The Games): ")

        if (
            text.lower() == "stop"
        ):  # If the user enters stop or Stop or STOP it will stop the program
            rand.display(messages)
            break

        if text.isdigit():  # If the user inputted a number raise a ValueError
            raise ValueError

        rand = Message(text).Randomizer()  # Rand equals a random encryption class

        encrypt = plaintextMsg(text, rand)  # Encrypts the word with the random class
        decrypt = ciphertextMsg(text, rand)  # Decrypts the word with the random class

        encrypt_text = encrypt.process()
        decrypt_text = decrypt.process(encrypt_text)

        cipher_name = type(rand).__name__

        messages.append(  # Appends the continuous messages from the display method to the messages list
            {
                "Original Text": text,
                "Encrypted Text": encrypt_text,
                "Decrypted Text": decrypt_text,
                "Cipher Used": cipher_name,
            }
        )

        decrypt_cipher = globals()[cipher_name](text)
        decrypt_text = decrypt_cipher.decrypt(encrypt_text)

    except ValueError:  # If the user inputted a string this will run
        print("Wrong Input Only Strings Are Accepted")
        break
    except (
        IndexError
    ):  # If the user inputed nothingt the transposition class gives this error
        print("Wrong Input Only Strings Are Accepted")
        break
    except NameError:  # If the user inputs stop first this runs
        break

##################### end #############################################
