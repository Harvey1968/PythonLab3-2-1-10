#3.2.1.10 LAB: The continue statement - the Ugly Vowel Eater

# Prompts the user to enter a word
print('"Why hello human I am the Ugly Vowel Eater, and I need feeding!"', """
        _   _
       (.)_(.)
    _ ( \___/ ) _
   / \/`-----'\/ \\
 __\ ( (     ) ) /__
 )   /\ \._./ /\   (
  )_/ /|\   /|\ \_(
""")#art credit - www.asciiart.eu/

# and assigns it to the 'user_word' variable.
user_word = input("Now enter a word: ")
# Returns a string where all Characters are in upper case. Symbols and Numbers are ignored. 
user_word = user_word.upper()

# A 'for' loop that skips certain Characters entered by user
print('\n"nom nom nom, that was yummy thanks!"\n"But you can have these back:"')
for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        # All Characters, Symbols and Numbers that were NOT skipped are output
        print(letter)
print()
