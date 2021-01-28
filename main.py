# Main file

import functions  # Imports the functions.py file


# Asks the player if they would like to play rps. If yes, the program will continue onto the next loop.
while True:
    playGame = str(input('Would you like to play "Rock, Paper, Scissors"? (Y/n): '))

    if playGame == "y":
        while True:
            functions.playerChoice()
            functions.computerChoice()
            functions.playRps()
            if functions.quitGame == True:
                break

    elif playGame == "n":
        print("Terminating program...")
        quit()

    else:
        print("Unknown input. Please enter a valid answer.")
        continue