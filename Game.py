import random
from typing import Dict, List, Protocol


class RuleSet(Protocol):
    #Game Rules defining interface. This helps to define a clear contract that every RuleSet should contain. So any new game variant also needs to have the same 3 methods.

    def get_choices(self) -> List[str]:
        ...

    def get_winner(self, choice1: str, choice2: str) -> str:
        ...

    def get_name(self) -> str:

        ...


class ClassicGameRules:
    #Rules for classic rock, paper, scissor game

    def __init__(self):
        # What each choice beats
        self._beats = {
            'rock': ['scissors'],
            'paper': ['rock'],
            'scissors': ['paper']
        }

    def get_choices(self) -> List[str]:
        return list(self._beats.keys())

    def get_winner(self, choice1: str, choice2: str) -> str:
        if choice1 == choice2:
            return 'tie'
        elif choice2 in self._beats[choice1]:
            return 'win'
        else:
            return 'lose'

    def get_name(self) -> str:
        return "Classic"


class ExtendedGameRules:
    #Rules for extended game version

    def __init__(self):
        # Which beats what
        self._beats = {
            'rock': ['scissors',
                     'lizard'],  # Rock crushes lizard, rock hits scissors
            'paper':
            ['rock',
             'spock'],  # Paper wraps around rock, paper disproves spock
            'scissors':
            ['paper',
             'lizard'],  # Scissors cut paper, scissors decapitate lizard
            'lizard': ['spock',
                       'paper'],  # Lizard poisons Spock, lizard eats paper
            'spock': ['scissors',
                      'rock']  # Spock smashes scissors, Spock vaporizes rock
        }

    def get_choices(self) -> List[str]:
        return list(self._beats.keys())

    def get_winner(self, choice1: str, choice2: str) -> str:
        if choice1 == choice2:
            return 'tie'
        elif choice2 in self._beats[choice1]:
            return 'win'
        else:
            return 'lose'

    def get_name(self) -> str:
        return "Extended"


class Player:

    def __init__(self, name: str):
        self.name = name
        self.score = 0

    def reset_score(self):
        self.score = 0

    def add_point(self):
        self.score += 1


class HumanPlayer(Player):

    def get_choice(self, valid_choices: List[str]) -> str:
        print(f"\nChoices: {', '.join(valid_choices)}")
        while True:
            choice = input("Your choice: ").lower().strip()
            if choice in valid_choices:
                return choice
            print(f"Invalid choice. Pick from: {', '.join(valid_choices)}")


class ComputerPlayer(Player):

    def get_choice(self, valid_choices: List[str]) -> str:
        choice = random.choice(valid_choices)
        print(f"Computer chooses: {choice}")
        return choice


class Game:
    #Class to manage the game logic using strategy pattern

    def __init__(self, rules: RuleSet, target_score: int = 3):
        self.rules = rules
        self.target_score = target_score
        self.human = HumanPlayer("You")
        self.computer = ComputerPlayer("Computer")

    def play_turn(self) -> bool:
        #returns True if round counted-no tie
        choices = self.rules.get_choices()

        human_choice = self.human.get_choice(choices)
        computer_choice = self.computer.get_choice(choices)

        result = self.rules.get_winner(human_choice, computer_choice)

        print(f"\nYou: {human_choice} | Computer: {computer_choice}")

        if result == 'tie':
            print("Tie! Playing again...")
            return False
        elif result == 'win':
            print("You win this round!")
            self.human.add_point()
        else:
            print("Computer wins this round!")
            self.computer.add_point()

        print(
            f"Score: {self.human.score} (You) vs. {self.computer.score} (Computer)"
        )
        return True

    def play(self):
        
        print(f"\n=== {self.rules.get_name()} Mode ===")
        print(f"First to {self.target_score} wins!")

        self.human.reset_score()
        self.computer.reset_score()

        while max(self.human.score, self.computer.score) < self.target_score:
            self.play_turn()

        #winner declared
        if self.human.score > self.computer.score:
            print("\nYou win the game!!!")
        else:
            print("\nComputer wins the game! :( Better luck next time!")


def get_rule_set() -> RuleSet:
    #get game variant from player
    print("\nGame Modes:")
    print("1. Classic (Rock, Paper, Scissors)")
    print("2. Extended (+ Lizard, Spock)")

    while True:
        choice = input("Choose mode (1 or 2): ").strip()
        if choice == '1':
            return ClassicGameRules()
        elif choice == '2':
            return ExtendedGameRules()
        else:
            print("Please enter 1 or 2")


def get_target_score() -> int:
    #Get target score from player
    while True:
        try:
            score = int(
                input("Play to how many points? (default 3, max 10): ") or "3")
            if score < 1:
                print("Please enter a positive number from 1 to 10")
            elif score > 10:
                print("Maximum 10 points allowed for a reasonable game length")
            else:
                return score
        except ValueError:
            print("Please enter a valid number")


def main():

    print("Let's Go!! Rock Paper Scissors!!")

    while True:
        try:
            rules = get_rule_set()
            target = get_target_score()
            game = Game(rules, target)
            game.play()

            if input("\nPlay again? (y/n): ").lower() not in ['y', 'yes']:
                break

        except KeyboardInterrupt:
            print("\nThanks for playing!")
            break
    print("\nThanks for playing! Till next time!")
    print("Bye bye!")


if __name__ == "__main__":
    main()
