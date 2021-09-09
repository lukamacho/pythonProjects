

class Game:
    def __init__(self, id):
        self.id = id
        self.p1Went = False
        self.p2Went = False
        self.ready = False
        self.moves = [None, None]
        self.wins = [0, 0]
        self.ties = 0

    def get_player_move(self, player):
        return self.moves[player]

    def connected(self):
        return self.ready

    def play(self, player, move):
        self.moves[player] = move
        if player == 1:
            self.p1Went = True
        else:
            self.p2Went = True

    def both_ready(self):
        return self.p1Went and self.p2Went

    def reset_game(self):
        self.p2Went = False
        self.p1Went = False

    def winner(self):

        first_ch = self.moves[0].upper()[0]
        second_ch = self.moves[0].upper()[0]

        if first_ch == second_ch:
            return -1
        elif first_ch == 'R' and second_ch == 'S':
            return 0
        elif first_ch == 'R' and second_ch == 'P':
            return 1
        elif first_ch == 'S' and second_ch == 'R':
            return 1
        elif first_ch == 'S' and second_ch == 'P':
            return 0
        elif first_ch == 'P' and second_ch == 'R':
            return 0
        elif first_ch == 'P' and second_ch == 'S':
            return 1

        return -1