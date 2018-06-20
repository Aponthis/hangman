'''A classic game of life or death! The user attempts to guess the phrase based
on what letters they have left and what letters have appeared in the phrase.'''

from random import randint

available_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                        'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                        'W', 'X', 'Y', 'Z'] # the letters available to be used
guessed_letters = [] #the letters that were previously guessed

random_phrase = "DEFAULT PHRASE" #An all-caps phrase that is randomly selected.

possible_phrases = ["A BIRD IN THE HAND IS WORTH TWO IN THE BUSH", #the list of phrases for the game
                    "ALL WORK AND NO PLAY MAKES JACK A DULL BOY",
                    "IT'S A LOVELY TIME TO BE ALIVE",
                    "SCORE ONE FOR THE LITTLE GUY",
                    "I AM RUNNING OUT OF RANDOM PHRASES TO TYPE"]

printed_phrase = ""

def randomizePhrase():
    global random_phrase
    random_phrase = possible_phrases[randint(0, (len(possible_phrases) -1))] #generates a random phrase from the list

def showPhrase():
    '''Shows the phrase in all its glory, with underscores for unguessed
    letters.'''

    global printed_phrase
    printed_phrase = random_phrase

    for x in available_letters:
        printed_phrase = printed_phrase.replace(x, "_")

    print(chr(27) + "[2J") #creates a new line
    print("Hangman! Enter a letter to guess it.")
    print(printed_phrase)

    if("_" in printed_phrase): #if there are no blanks left
        return False
    else:
        return True

guesses_remaining = 5

def getInput():
    '''Gets the next user-input letter. '''
    global printed_phrase
    global random_phrase
    global guesses_remaining

    while(1):
        print("\nLetters still available: {}\n" .format(available_letters))
        print("Incorrect guesses remaining: {}\n" .format(guesses_remaining))
        input_data = raw_input("What letter would you like to guess next?\n")
        input_letter = input_data.upper()

        if(input_letter in available_letters):
            available_letters.remove(input_letter) #removes the guessed letter from the available letters
            guessed_letters.append(input_letter)
            if(random_phrase.count(input_letter) == 0):
                guesses_remaining -= 1
            break
        elif(input_letter in guessed_letters):
            print(chr(27) + "[2J")
            print("You already guessed that letter.")
            print(printed_phrase)
        else:
            print(chr(27) + "[2J")
            print("Sorry, that's not a valid response. Please type a single letter.")
            print(printed_phrase)

randomizePhrase()

while(1):
    if(showPhrase()):
        break
    if(guesses_remaining == 0):
        break
    getInput()

print(chr(27) + "[2J")
if(guesses_remaining == 0):
    print("Uh oh! You ran out of guesses. Correct phrase: {}" .format(random_phrase))
else:
    print("You won! Completed phrase: {}" .format(random_phrase))
