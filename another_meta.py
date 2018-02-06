'''
Some more metaclass
'''
from meta_intro import *


# kane = Fighter('Kane', 800, 60, 50)
# bigshow = Fighter('Big Show', 900, 60, 50)
# fighters = {
#     'kane': kane,
#     'bigshow': bigshow,
# }
# Wet, not good

# undertaker = TeamLeader('The Undertaker', kane, 700, 60, 40),
# brock = TeamLeader('Brock Lessner', bigshow, 800, 55, 50),
# leaders = {
#     'undertaker': undertaker,
#     'brock': brock,
# }
# Also Wet, not good

# Many more subclass of Fighter?  More ugly


class FighterMeta(type):
    def __new__(cls, name, bases, attrs):
        cls = type.__new__(cls, name, bases, attrs)
        cls.all = {}
        return cls

    def __call__(cls, *args, **kwargs):
        self = type.__call__(cls, *args, **kwargs)
        self.all[self.name.replace(' ', '').lower()] = self
        return self


# new_mark_five() call of NewMarkInt
# Fighter() call of FighterMeta, __new__ and __init__ is internal part of __call__ of meta


class NewFighter(Fighter):
    __metaclass__ = FighterMeta


NewFighter('Batista', 850, 50, 50)
NewFighter('HBK', 700, 40, 20)


batista = NewFighter.all['batista']
hbk = NewFighter.all['hbk']


print NewFighter.all


class NewTeamLeader(NewFighter, TeamLeader):
    pass


NewTeamLeader('HHH', batista, 700, 40, 40)
NewTeamLeader('Goldberg', hbk, 800, 40, 80)


hhh = NewTeamLeader.all['hhh']
goldberg = NewTeamLeader.all['goldberg']


Game(NewTeamLeader.all).play()
