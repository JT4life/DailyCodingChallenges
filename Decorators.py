import random

TRAP_ARTISTS = [
    'Jayz','Future','CJ'
]
class TrapArtist:

    _hits = [
        'Money','Candy','Girls'
    ]

    def __init__(self, name):
        self._name = name

    @property # can refer to name without ()
    def name(self):
        return self._name

    @name.setter # set what is allowed name
    def name(self, name):
        if name not in TRAP_ARTISTS:
            raise ValueError(' is not a trap artist', name)
        self._name = name

    @staticmethod
    def random_artist():
        # Does not take self, normal func attach to a class, don't need instance of obj class,
        # static method is good for implementing Factory functions, functions that generate instance of a class
        return TrapArtist(random.choice(TRAP_ARTISTS))

    @classmethod # refers to the class, not the instance of self, linked to the class definition
    def hits(cls):
        return cls._hits

    def regular_hits(self):
        return self._hits


rr = TrapArtist('CJ')
# rr.__class__._hits = ['Purple', 'Traps'] # by adding __class__ you can change the _hits
rr._hits = ['Purple', 'Traps']
print(rr.regular_hits()) # will change _hits to defined hits on object
# print(rr.hits())

randomGuy = TrapArtist.random_artist()
# print(randomGuy.name)

# trapGuy = TrapArtist("Rick Ross")
# print(trapGuy.name)
#
# # change name
# trapGuy.name = "Future"
# print(trapGuy.name)