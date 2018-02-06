'''
How to write a class and create objects.
Couple of magic methods.
'''

class Fighter(object):
    def __init__(self, name, health, kick_dmg, punch_dmg):
        self.name = name
        self.max_health = health
        self.kick_dmg = kick_dmg
        self.punch_dmg = punch_dmg
        self.health = health

    def __str__(self):
        return '%s: %s/%s' % (self.name, self.health, self.max_health)

    def __repr__(self):
        return '<%s: %s>' % (type(self).__name__, str(self))

    def rest(self):
        self.health = self.max_health

    def win(self):
        raise GameOverError('Game over, winner: %s'%str(self), self)

    def kick(self, other):
        other.health -= self.kick_dmg
        if other.health <= 0:
            self.win()

    def punch(self, other):
        other.health -= self.punch_dmg
        if other.health <= 0:
            self.win()

    def assault(self, other, punches, kicks):
        for i in range(punches):
            self.punch(other)
        for i in range(kicks):
            self.kick(other)


kane = Fighter('Kane', 800, 60, 50)
bigshow = Fighter('Big Show', 900, 60, 50)
fighters = {
    'kane': kane,
    'bigshow': bigshow,
}


class GameOverError(Exception):
    def __init__(self, message, winner):
        self.message = message
        self.winner = winner


class Game(object):
    def __init__(self, available):
        you = raw_input('Who are you?\n%s\n: '%'\n'.join(available.keys()))
        self.you = available[you]
        computer = raw_input('Who is computer?\n%s\n: '%'\n'.join(available.keys()))
        self.computer = available[computer]

    def you_play(self):
        kicks, punches = (int(i) for i in raw_input('Your turn. Kicks, Punches: ').split())
        self.you.assault(self.computer, punches, kicks)

    def computer_play(self):
        kicks, punches = (int(i) for i in raw_input('Computer"s turn Kicks, Punches: ').split())
        self.computer.assault(self.you, punches, kicks)

    def display(self):
        print 'You: %s' % self.you
        print 'Computer: %s' % self.computer

    def play(self):
        while True:
            try:
                self.you_play()
                self.display()
                self.computer_play()
                self.display()
            except GameOverError as e:
                winner = e.winner
                if winner == self.you or (hasattr(self.you, 'teammate') and winner == self.you.teammate):
                    print 'Congrats, %s wins.' % self.you
                else:
                    print 'Better luck next time, %s is too dangerous' % self.computer
                break
        self.you.rest()
        self.computer.rest()


if __name__ == '__main__':    
    Game(fighters).play()
