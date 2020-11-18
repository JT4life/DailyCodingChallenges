# write a method to reverse a driplist without modifying the
# driplist class your reverse method should return an instance of driplist

class DripList:
    def __init__(self, *values):
        self.values = list(values)

    @property
    def head(self):
        return self.values[0]

    @property
    def tail(self):
        return DripList(*self.values[1:])

    def push(self, item):
        return DripList(*[x for x in self.values + [item]])

    def __len__(self):
        return len(self.values)

    def __str__(self):
        return str(self.values)


def reverse(drip_list):
    if len(drip_list) == 1:
        return drip_list
    if len(drip_list) > 1:
        return drip_list[::-1]


test_list = DripList(1, 2, 3, 4, 5)
reversed = reverse(test_list)
print(reversed)
print(type(test_list))

'''Given a DripList
If the list is of length 1, return the list
If the list is longer than 1, reverse the tail and push the head on the reversed tail'''