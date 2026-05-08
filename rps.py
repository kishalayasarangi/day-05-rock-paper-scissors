import random

def get_winner(player, computer):
    if player == computer:
        return "tie"
    wins = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    return "player" if wins[player] == computer else "computer"

def display_score(scores):
    print(f"\n  You: {scores['player']}  |  Computer: {scores['computer']}  |  Ties: {scores['tie']}")

def game():
    choices = ["rock", "paper", "scissors"]
    scores = {"player": 0, "computer": 0, "tie": 0}

    print("=" * 35)
    print("   Rock Paper Scissors")
    print("=" * 35)

    while True:
        print("\n1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")

        pick = input("\nYour choice (1-4): ").strip()

        if pick == "4":
            print("\nFinal Score:")
            display_score(scores)
            print("\nThanks for playing!")
            break

        if pick not in ["1", "2", "3"]:
            print("Invalid choice!")
            continue

        player = choices[int(pick) - 1]
        computer = random.choice(choices)

        print(f"\nYou chose:      {player.upper()}")
        print(f"Computer chose: {computer.upper()}")

        result = get_winner(player, computer)

        if result == "player":
            print("You WIN! 🎉")
            scores["player"] += 1
        elif result == "computer":
            print("You LOSE! 💀")
            scores["computer"] += 1
        else:
            print("It's a TIE! 🤝")
            scores["tie"] += 1

        display_score(scores)

game()