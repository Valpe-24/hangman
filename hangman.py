import random
lives_ascii = [
    '''
    --------
    |      |
    |
    |
    |
    |
    -
''',

    '''
    --------
    |      |
    |      O
    |
    |
    |
    -
''',

    '''
    --------
    |      |
    |      O
    |      |
    |
    |
    -
''',

    '''
    --------
    |      |
    |      O
    |      |
    |      |
    |
    -
''',

    '''
    --------
    |      |
    |      O
    |     \|
    |      |
    |
    -
''',


    '''
    --------
    |      |
    |      O
    |     \|/
    |      |
    |
    -
''',

    '''
    --------
    |      |
    |      O
    |     \|/
    |      |
    |      |
    -
''',

    '''
    --------
    |      |
    |      O
    |     \|/
    |      |
    |     /
    -
''',

    '''
    --------
    |      |
    |      O
    |     \|/
    |      |
    |     / \\
    -
''']

words = ['empanada', 'flower', 'code', 'watermelon', 'strawberry', 'mango', 'song']
word = random.choice(words)
blank_line = []
guessed_words = []
play_game = True
lives = 8

print("WELCOME TO HANGMAN")
for _ in range(len(word)):
    blank_line += "_"

print(lives_ascii[0])

while play_game:
    print(f"Lives: {lives}")
    print(''.join(blank_line))
    guess = input("Guess a letter: ")

    if guess in guessed_words:
        print(f''' 
        -------------------------------
         You already guessed {guess} 👯
        -------------------------------
        ''')

    for space_idx in range(len(word)):
        letter = word[space_idx]

        if letter == guess:
            blank_line[space_idx] = letter

    if guess not in word and guess not in guessed_words:
        lives -= 1
        print('''
          -----------------------------------------
          |  WRONG GUESS. You just lost a life 😭 |
          -----------------------------------------
        ''')

        print(lives_ascii[len(lives_ascii) - lives - 1])

    if lives == 0:
        print('''
          -----------------
          |☠️ GAME OVER ☠️|
          -----------------
        ''')
        play_game = False

    if '_' not in blank_line:
        play_game = False
        print('''
          --------------------------
          | 🎉 YOU WON THE GAME 🎉 |
          --------------------------
        ''')
    if guess in word and '_' in blank_line:
        print('''
          -------------------
          |  WELL DONE!! 💃 |
          -------------------
        ''')

    print(' '.join(blank_line))
    guessed_words += guess

