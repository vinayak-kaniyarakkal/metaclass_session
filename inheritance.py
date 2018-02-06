'''
Inheritance, overriding, calling overrided function. "super" function
'''
from class_example import *


class TeamLeader(Fighter):
    def __init__(self, name, teammate, *args, **kwargs):
        Fighter.__init__(self, name, *args, **kwargs)
        # super(TeamLeader, self).__init__(*args, **kwargs)
        self.teammate = teammate

    def kick(self, other):
        # Fighter.kick(self, other)
        super(TeamLeader, self).kick(other)
        self.teammate.kick(other)

    def punch(self, other):
        Fighter.punch(self, other)
        # super(TeamLeader, self).punch(other)
        self.teammate.punch(other)


undertaker = TeamLeader('The Undertaker', kane, 700, 60, 40)
brock = TeamLeader('Brock Lessner', bigshow, 800, 55, 50)
leaders = {
    'undertaker': undertaker,
    'brock': brock,
}

if __name__ == '__main__':
    Game(leaders).play()
