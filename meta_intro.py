'''
A basic metaclass example
'''
from instances_types import *


# class MarkInt(int):
#     def __str__(self):
#         return '|' * self
# Let's implement this in a diffrent way

def look_diffrent(self):
    return  '|' * self

# class MarkInt(int):
#     __str__ = look_diffrent
#     __repr__ = look_diffrent

# kane = Fighter('Kane', 800, 60, 50)
# Means create a Fighter called with 'Kane' as name and 800, 60, 50 as other parameters, bind variable kane to this fighter

# mark_four = MarkInt(4)
# Means create a MarkInt with 4 as value and bind it to variable called mark_four

# MarkInt = type(<something>)
# MarkInt = type(name, bases, attrs)


# Another way to create class ie create a type
NewMarkInt = type(
    'NewMarkInt',
    (int, ),
    {'__str__': look_diffrent, '__repr__': look_diffrent}
)


print MarkInt
print type(MarkInt)
print isinstance(MarkInt, type)
print isinstance(MarkInt, int)        # False
print MarkInt.mro()

print NewMarkInt
print type(NewMarkInt)
print isinstance(NewMarkInt, type)
print isinstance(NewMarkInt, int)     # False
print NewMarkInt.mro()

new_mark_four = NewMarkInt(4)
new_mark_five = NewMarkInt('5')
new_mark_nine = NewMarkInt(9)


# new_mark_four and new_mark_five are NewMarkInts
print isinstance(new_mark_four, NewMarkInt)
print isinstance(new_mark_five, NewMarkInt)
# They are also ints
print isinstance(new_mark_four, int)
print isinstance(new_mark_five, int)
# All NewMarkInts are ints!!  Because NewMarkInt is a child of int


# MarkInt is a child of int.  All MarkInts are ints.
# But they are not just ints.  They have some additional features.
# Using inheritance we are able to create things which are ints with extra features

# TeamLeader is a child of Fighter.  All TeamLeaders are Fighters.
# But they are not just Fighters.  They have some additional features.
# Using inheritance we are able to create things which are Fighters with extra features


# What if we inherit type?
# We can create types with extra features, classes with extra features that other classes doesn't have

# We already did
# NewMarkInt = type(
#     'NewMarkInt',
#     (int, ),
#     {'__str__': look_diffrent}
# )


class MyMetaClass(type):
    # Do something
    pass

NewMarkInt = MyMetaClass(
    'NewMarkInt',
    (int, ),
    {'__str__': look_diffrent}
)


print type(NewMarkInt)
print isinstance(NewMarkInt, MyMetaClass)
print isinstance(NewMarkInt, type)
del NewMarkInt


class NewMarkInt(int):
    __metaclass__ = MyMetaClass
    __str__ = look_diffrent
print type(NewMarkInt)
print isinstance(NewMarkInt, MyMetaClass)
print isinstance(NewMarkInt, type)


# This NewMarkInt is not just a type like MarkInt, we can put extra features into it, using MyMetaClass


class MyMetaClass(type):
    def __str__(self):
        return '%s, child of [%s]' % (self.__name__, ', '.join(i.__name__ for i in self.mro() if i != self))
    __repr__ = __str__

NewMarkInt = MyMetaClass(
    'NewMarkInt',
    (int, ),
    {'__str__': look_diffrent}
)


# Check what is NewMarkInt
class NewMarkInt(int):
    __metaclass__ = MyMetaClass
    __str__ = look_diffrent
    __repr__ = look_diffrent

    def __call__(self):
        for i in range(self):
            print 'Hello World'
            
print NewMarkInt
new_zero = NewMarkInt(0)
# Check what is NewMarkInt
# Also checkout __call__
