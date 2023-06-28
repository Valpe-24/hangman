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
play_game = True
for _ in range(len(word)):
    blank_line += "_"

while play_game:
    guess = input("Guess a letter: ")

    for space_idx in range(len(word)):
        letter = word[space_idx]

        if letter == guess:
            blank_line[space_idx] = letter

    print(''.join(blank_line))

