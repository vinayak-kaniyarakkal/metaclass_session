'''
more inheritance, instances and type
'''
from inheritance import *

print brock
print undertaker
print isinstance(kane, Fighter)
print isinstance(brock, TeamLeader)
print isinstance(brock, Fighter)
print isinstance(kane, TeamLeader)

print type(kane)
print type(brock)


one = 1
two = int('2')
three = one + two


class MarkInt(int):
    def __str__(self):
        return '|' * self
    def __repr__(self):
        return str(self)
    def __add__(self, other):
        return MarkInt(int(self)+int(other))


mark_four = MarkInt(4)
mark_five = MarkInt('5')
mark_nine = mark_four + mark_five


# one is an int
# two is an int
print type(one)
print type(two)
print isinstance(one, int)
print isinstance(two, int)
# but one and two are not MarkInt
print isinstance(one, MarkInt)
print isinstance(two, MarkInt)

# mark_four and mark_five are MarkInts
print isinstance(mark_four, MarkInt)
print isinstance(mark_five, MarkInt)
# They are also ints
print isinstance(mark_four, int)
print isinstance(mark_five, int)
# All MarkInts are ints!!  Because MarkInt is a child of int
#
#


# bigshow is a fighter
# kane is a fighter
print type(bigshow)
print type(kane)
print isinstance(bigshow, Fighter)
print isinstance(kane, Fighter)
# but they are not leaders
print isinstance(kane, TeamLeader)
print isinstance(bigshow, TeamLeader)

# brock and undertaker are TeamLeaders
print type(brock)
print type(undertaker)

print isinstance(brock, TeamLeader)
print isinstance(undertaker, TeamLeader)
# They are also Fighters
print isinstance(brock, Fighter)
print isinstance(undertaker, Fighter)
# All TeamLeaders are Fighters!!  Because TeamLeader is a child of Fighter
#
#


# brock    --> TeamLeader (also Fighter)
# kane     --> Fighter
# one      --> int
# mark_five --> MarkInt (also int)

# int      --> What?
# MarkInt  --> What?
# Fighter  --> What?
# TeamLeader   --> What?


print type(int)
print type(MarkInt)
print type(Fighter)
print type(TeamLeader)

# They are all types!!!

print isinstance(int, type)
print isinstance(MarkInt, type)
print isinstance(Fighter, type)
print isinstance(TeamLeader, type)


# Know the diffrence between bieng an instance and bieng a child

# All MarkInts are ints but MarkInt is not an int, it is type
print isinstance(MarkInt, type)
print isinstance(MarkInt, int)        # False
print isinstance(mark_five, type)       # False
print isinstance(mark_five, int)
print isinstance(mark_five, MarkInt)

# All TeamLeaders are Fighters but TeamLeader is not a Fighter, it is type
print isinstance(TeamLeader, type)
print isinstance(TeamLeader, Fighter)        # False
print isinstance(undertaker, type)       # False
print isinstance(undertaker, TeamLeader)
print isinstance(undertaker, Fighter)


# Fighter, TeamLeader, int, MarkInt: They are all types
# kane is a Fighter and Fighter is a type
# undertaker is a teamleader and also a fighter, fighter and teamleader are types, but undertaker is not a type
# mark_five is a markint and also an int, markint and int are types, but mark_five is not a type
