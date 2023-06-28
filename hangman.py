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


word = 'empanada'
blank_line = []
# add a guessed list to tell the user when a letter was already guessed
play_game = True
lives = 8

print("WELCOME TO HANGMAN")
for _ in range(len(word)):
    blank_line += "_"

print(lives_ascii[0])

while play_game:
    print(f"Lives: {lives}")
    guess = input("Guess a letter: ")


    for space_idx in range(len(word)):
        letter = word[space_idx]

        if letter == guess:
            blank_line[space_idx] = letter

    if '_' not in blank_line:
        play_game = False
        print('''
          -------------------------
          |  YOU WON THE GAME!!!! |
          -------------------------
        ''')

    print(' '.join(blank_line))

