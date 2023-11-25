import random

class RockPaperScissorsGame:
    def __init__(self):
        self.player_score = 0
        self.opponent_score = 0

    def play_round(self):
        print("Choose rock, paper, or scissors:")
        player_choice = input().lower()

        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            return

        opponent_choice = random.choice(["rock", "paper", "scissors"])
        print(f"Opponent chose: {opponent_choice}")

        result = self.determine_winner(player_choice, opponent_choice)

        if result == "win":
            self.player_score += 1
            print("You win!")
        elif result == "lose":
            self.opponent_score += 1
            print("You lose.")
        else:
            print("It's a tie!")

    def determine_winner(self, player_choice, opponent_choice):
        rules = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

        if player_choice == opponent_choice:
            return "tie"
        elif rules[player_choice] == opponent_choice:
            return "win"
        else:
            return "lose"

    def start_game(self):
        while True:
            self.play_round()

            print(f"Score: Player {self.player_score} - {self.opponent_score} Opponent")

            print("Do you want to play again? (yes/no)")
            play_again = input().lower()

            if play_again != "yes":
                print("Game over. Thanks for playing!")
                break

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.start_game()
