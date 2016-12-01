

class Players:
    participants = []



class Player_one(Players):
    def __init__(self):
        self.name = 'Player One'
        self.points = 0
        Players.participants.append(self)


class Player_two(Players):
    def __init__(self):
        self.name = 'Player Two'
        self.points = 0
        Players.participants.append(self)


p1 = Player_one()
p2 = Player_two()

