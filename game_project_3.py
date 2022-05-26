import random

# there are three different moves the player can make
# rock, paper, scissors
moves = ['rock', 'paper', 'scissors']

# The Function to decide who win whom


def win(one, two):

    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

# The Player class is the parent class for all of the Players in this game


class Player:

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

# Chooses its move at random and it returns 'rock','paper', or 'scissors'

# randum 
class RandomPlayer(Player):

    def move(self):
        return random.choice(moves)

# What move the opponent played last round
# and plays that move in the next round


class ReflectPlayer(Player):

    def __init__(self):
        # First round is a random choice
        self.previous_move2 = random.choice(moves)

    def move(self):
        return self.previous_move2

    def learn(self, my_move, their_move):
        self.previous_move2 = their_move

# It remembers what move _it_ played last round time
# and cycles through the different moves


class CyclePlayer(Player):

    def __init__(self):
        self.previous_move1 = random.choice(moves)

    # Rotate moves until it restarts with rock again
    def move(self):
        moves_available = moves.index(self.previous_move1)
        if moves_available == 2:
            return moves[0]
        else:
            return moves[moves_available + 1]

    # Sets up the player to recall its own previous move
    def learn(self, my_move, their_move):
        self.previous_move1 = my_move


# Asks the player to choose the move
class selfPlayer(Player):
    def move(self):
        your_move = ""

        while True:
            your_move = input('Choose a move: (rock / paper / scissors)\n')
            if your_move.lower() == 'r' or your_move.lower() == 'rock':
                your_move = 'rock'
                break
            elif your_move.lower() == 'p' or your_move.lower() == 'paper':
                your_move = 'paper'
                break
            elif your_move.lower() == 's' or your_move.lower() == 'scissors':
                your_move = 'scissors'
                break
            else:
                print("Try again!")
        return your_move


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.player_one = 0
        self.player_two = 0
        self.tiegame = 0
        self.rounds_played = 0

    # Print the game header when the game starts
    def game_header(self):
        print(
            "\n"
            "🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨\n"
            "Rock, Paper, Scissors\n"
            "📝📝📝📝📝📝📝📝📝📝📝📝\n"
            "Rules:\n"
            " Scissors cuts Paper\n"
            " Paper covers Rock\n"
            " Rock crushes Scissors\n"
            "✂️✂️✂️✂️✂️✂️✂️✂️✂️✂️✂️✂️\n"
            "Ready!\n"
            "--------------------------\n")

    def select_mode(self):
        while True:
            rounds_num = input("how many number of rounds you would "
                               "like to play (1-10): ")
            # Checking for valid number 1-10. If not, loop back.
            if rounds_num.isnumeric():
                rounds_num = int(rounds_num)
                if rounds_num >= 0 and rounds_num <= 10:
                    print("-----------------------------")
                    print("Great! Let's play {0} rounds!".format(rounds_num))
                    print("-----------------------------")
                    self.rounds_played = rounds_num
                    break
                else:
                    print("That's not a number between 1 to 10, try again.")

    # Choose the opponent
    def opposite_player(self):
        print(
            "Select your opponent:\n"
            "\n[B]asic  - 'rock' 🪨 is played by opponent every round"
            "\n[R]andom - opponent plays random choice"
            "\n[M]imic  - opponent mimics your move next round"
            "\n[C]ycle  - remembers what was played and cycles through moves"
            "\ne[X]it   - quits the game"
            "\n ")
        while True:
            opponent = (input("Choose your opponent: "))
            if opponent.lower() == "b" or opponent.lower() == "basic":
                self.p2 = Player()
                break
            elif opponent.lower() == "r" or opponent.lower() == "random":
                self.p2 = RandomPlayer()
                break
            elif opponent.lower() == "m" or opponent.lower() == "mimic":
                self.p2 = ReflectPlayer()
                break
            elif opponent.lower() == "c" or opponent.lower() == "cycle":
                self.p2 = CyclePlayer()
                break
            elif opponent.lower() == "x" or opponent.lower() == "exit":
                print("You have chosen to leave the game :(")
                self.rounds_played = 0
                break
            else:
                print("That's not one of the options 🪨📝✂️, try again.")

    def outcome(self, first_play, second_play):

        if win(first_play, second_play):
            # Player one wins
            self.player_one += 1
            print("move '{0}' win '{1}'. First Player won round!"
                  .format(first_play, second_play))
            print("Score:")
            print("First player: {0}".format(self.player_one))
            print("Second player: {0}".format(self.player_two))
            print("Ties: {0}".format(self.tiegame))

        elif win(second_play, first_play):
            # Opponent wins
            self.player_two += 1
            print("move {0} win {1}. Second Player won round!"
                  .format(second_play, first_play))
            print("Score:")
            print("First player: {0}".format(self.player_one))
            print("Second player: {0}".format(self.player_two))
            print("Ties: {0}".format(self.tiegame))

        else:
            # It's a tie
            self.tiegame += 1
            print("Nobody won, it's a tie")
            print("Score:")
            print("First player: {0}".format(self.player_one))
            print("Second player: {0}".format(self.player_two))
            print("Ties: {0}".format(self.tiegame))

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print("Player 1: {0}  Player 2: {1}".format(move1, move2))
        self.outcome(move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def battle(self):
        if self.rounds_played >= 1:
            print("\n----------------------------------")
            print("Prepare to FIGHT")
            for round in range(0, self.rounds_played):
                print("----------------------------------\n")
                print("Round {" + str(round + 1) + "}: ")
                self.play_round()

    def game_results(self):
        # Results of the game
        if self.rounds_played >= 1:
            print("\n----------------------------------")
            print("Overall score:")
            print("Player One won: {0}".format(self.player_one))
            print("Player Two won: {0}".format(self.player_two))
            print("Ties: {0}".format(self.tiegame))
            print("----------------------------------")
            if self.player_one > self.player_two:
                print("Player One won!")
            elif self.player_one < self.player_two:
                print("Player Two won!")
            else:
                print("It's a tie!")

            print("Thank you for playing.")
            print("----------------------------------")

    def play_game(self):
        self.game_header()
        self.select_mode()
        self.opposite_player()
        self.battle()
        self.game_results()


if __name__ == '__main__':
    game = Game(selfPlayer(), RandomPlayer())
    game.play_game()