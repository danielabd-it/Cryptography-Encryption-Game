# Cryptography Encryption Game

An object-oriented Python application that demonstrates multiple classical and modern cryptographic algorithms through an interactive command-line game.

The program accepts messages from the user and randomly selects an encryption algorithm to transform the plaintext into ciphertext. Users can continue entering messages until they enter `Stop`, at which point the program displays a summary of all encrypted messages and the algorithms that were used.

## Features

- Interactive command-line interface
- Random selection of encryption algorithms
- Six implemented encryption techniques:
  - Caesar Cipher
  - Substitution Cipher
  - Playfair Cipher
  - Transposition Cipher
  - Product Cipher
  - RSA
- Displays original plaintext and resulting ciphertext
- Maintains a history of encrypted messages
- Object-oriented class structure
- Inheritance between message types
- Encapsulation through class properties and methods
- Operator overloading
- Exception handling and input validation

## Technologies

- **Python 3**
- Object-Oriented Programming (OOP)
- Classical Cryptography
- RSA Encryption
- Randomization
- Exception Handling

## How It Works

The program follows an object-oriented design centred around message objects.

A `Message` class provides common functionality for handling messages, with specialized classes for plaintext and ciphertext.

## Encryption Algorithms

The project also makes use of:

- **Inheritance**
- **Encapsulation**
- **Properties**
- **Method abstraction**
- **Operator overloading**
- **Exception handling**
- **Modular class design**

## Usage

```text
Enter Your Message (Type 'Stop' to End The Games): garden
Enter Your Message (Type 'Stop' to End The Games): zombies
Enter Your Message (Type 'Stop' to End The Games): plants
Enter Your Message (Type 'Stop' to End The Games): brain
Enter Your Message (Type 'Stop' to End The Games): peashooter
Enter Your Message (Type 'Stop' to End The Games): sunflower
Enter Your Message (Type 'Stop' to End The Games): large lawnmower
Enter Your Message (Type 'Stop' to End The Games): stop

Original Text: garden
Encrypted Text: lfwijs
Decrypted Text: garden
Cipher Used: Substitution

Original Text: zombies
Encrypted Text: ozmibes
Decrypted Text: zombies
Cipher Used: Transposition

Original Text: plants
Encrypted Text: lpatns
Decrypted Text: plants
Cipher Used: Transposition

Original Text: brain
Encrypted Text: rbani
Decrypted Text: brain
Cipher Used: Transposition

Original Text: peashooter
Encrypted Text: dsogvcchsf
Decrypted Text: peashooter
Cipher Used: Caesar

Original Text: sunflower
Encrypted Text: wyrjpsaiv
Decrypted Text: sunflower
Cipher Used: Caesar

Original Text: large lawnmower
Encrypted Text: ozfsu ozkabcskf
Decrypted Text: large lawnmower
Cipher Used: Product
```

## Disclaimer

This project is intended for educational purposes. The cryptographic implementations demonstrate the underlying concepts of different encryption techniques and should not be considered production-ready cryptographic software.
