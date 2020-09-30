
"""
@author: Sultan Alazemi
Panther Id : 6185762
"""

class MySetOperation:
    def _init_(self, set_obj):
        self.obj = set_obj

    def _str_(self):
        return str(self.obj)

    def is_empty(self):
        if len(self.obj) == 0:
            return True
        else:
            return False

    def disjoint(self, set_b):
        """
        This function check, is two sets are disjoint?
        :param set_b:
        :return:
        """
        for x in self.obj:  # iterating through  first set
            if x in set_b:  # checking the value  is in set b or not
                return True
        return False

    def intersection(self, set_b):
        """
        This function return intersection of two sets (comman element)
        :param set_b:
        :return:
        """
        new_set = set()
        for x in self.obj:  # iterating through  first set
            if x in set_b:  # checking the value  is in set b or not
                new_set.add(x)
        return new_set

    def union(self, set_b):
        """
        This function return union  of two sets  as new set
        :param set_b:
        :return:
        """
        new_set = set()
        for x in self.obj:
            new_set.add(x)

        for x in set_b:
            new_set.add(x)
        return new_set

    def difference(self, set_b):
        """
        This function will give  A difference B means (A-B)
        :param set_b:
        :return:
        """
        new_set = set()
        for x in self.obj:
            if x not in set_b:
                new_set.add(x)
        return new_set

    def symmetric_difference(self, set_b):
        """
        THis function will return symmetric difference between two sets
        :param set_b:
        :return:
        """

        new_set = set()
        for x in self.obj:
            if x not in set_b:
                new_set.add(x)

        for x in set_b:
            if x not in self.obj:
                new_set.add(x)
        return new_set


A = MySetOperation({1, 2, 3, 4})
C = MySetOperation(set())
B = {5, 6, 1, 7, 2, 9}
print("Set A:", A)
print("Set B:", B)
print("Set C:", C)
print("IS set C is empty:", C.is_empty())
print("Is A and B is disjoint:", A.disjoint(B))
print("A intersection B:", A.intersection(B))
print("A union B:", A.union(B))
print("A difference B:", A.difference(B))
print("A symmetric difference B:", A.symmetric_difference(B))