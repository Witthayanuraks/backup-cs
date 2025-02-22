import random
import time

WAIT = 60  # Timeout in seconds

flag = "[REDACTED]"
hands = ["rock", "paper", "scissors"]
loses = ["paper", "scissors", "rock"]
wins = 0


def tgetinput(prompt, timeout=WAIT):
    """Simulate the tgetinput function with timeout"""
    try:
        # This will allow the player to input within a timeout period
        start_time = time.time()
        player_input = input(prompt)

        while time.time() - start_time < timeout and player_input.strip() == '':
            player_input = input(prompt)

        if player_input.strip() == '':
            print("Timed out waiting for user input. Press Ctrl-C to disconnect")
            exit(0)

        return player_input.strip()

    except KeyboardInterrupt:
        print("\nGoodbye!")
        exit(0)


def play():
    global wins
    player_turn = tgetinput("Please make your selection (rock/paper/scissors): ")
    computer_turn = random.choice(hands)

    print(f"You played: {player_turn}")
    print(f"The computer played: {computer_turn}")

    if player_turn == loses[hands.index(computer_turn)]:
        print("You win! Play again?")
        return True
    else:
        print("Seems like you didn't win this time. Play again?")
        return False


def main():
    global wins
    print("Welcome challenger to the game of Rock, Paper, Scissors")
    print("For anyone that beats me 5 times in a row, I will offer up a flag I found")
    print("Are you ready?")

    while True:
        print("Type '1' to play a game")
        print("Type '2' to exit the program")
        command = tgetinput("Your choice: ")

        if command == '1':
            print("\n\n")
            if play():
                wins += 1
            else:
                wins = 0

            if wins >= 5:
                print("Congrats, here's the flag!")
                print(flag)
                wins = 0  # Reset after giving flag
        elif command == '2':
            print("Goodbye!")
            break
        else:
            print("Please type either 1 or 2")


if _name_ == "_main_":
    main()