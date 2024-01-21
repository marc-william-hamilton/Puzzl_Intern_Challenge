from random import choice

# a dictionary where key beats value
roshambo = {"rock": "scissors", "paper": "rock", "scissors": "paper"}


def get_player_choice():
    # r, p, and s representation for typing convenience
    player_choice = input('Type "r", "p", or "s" to play ')

    # repeat until player makes a valid choice
    while player_choice not in ["r", "p", "s"]:
        print(f"\n{player_choice} is not an option, try again please")
        player_choice = input('Type "r", "p", or "s" to play ')

    # rock, paper, scissors representation under the hood for readability
    match player_choice:
        case "r":
            player_choice = "rock"
        case "p":
            player_choice = "paper"
        case "s":
            player_choice = "scissors"

    return player_choice


def get_opponent_choice():
    return choice(list(roshambo))


def determine_winner(player_choice, opponent_choice):
    if player_choice == opponent_choice:
        return "You drew 🤠"
    elif roshambo[player_choice] == opponent_choice:
        return "You won 🎉"
    else:
        return "You lost 😓"


def display_result(player_choice, opponent_choice, result):
    print(f"\nYou chose {player_choice} and your opponent chose {opponent_choice}")
    print(result)


def finalise():
    play_again = input("Play again? [y/n] ")
    # repeat until player makes a valid choice
    while play_again not in ["y", "n"]:
        print(f"\n{play_again} is not an option, try again please")
        play_again = input("Play again? [y/n] ")

    if play_again == "y":
        main()
    else:
        print("\nThanks for playing! ✨")
        exit(0)


def main():
    print("\nWelcome to this (R)ock (P)aper (S)cissors Game!")
    player_choice = get_player_choice()
    opponent_choice = get_opponent_choice()
    result = determine_winner(player_choice, opponent_choice)
    display_result(player_choice, opponent_choice, result)
    finalise()


if __name__ == "__main__":
    main()
