# Created by Lucas Stoltman
# Program 3
# April 16th, 2022
# CSS 340 A, Dimpsey
# Version: 1.0


class BigO:
    # The unsorted list is searched linearly to see if the val is in the list
    @staticmethod
    def find1(self, val: int):
        for i in self:
            if i == val:
                return True
        return False

    # # TODO
    # # A deep copy is made of the list; the copied list is then sorted using
    # # the "sort" built- in function and then a binary search is performed on
    # # the list to find if the val is in the list
    # @staticmethod
    # def find2(self, val: int):
    #     result = copy.deepcopy(self)
    #
    #     return True

    #
    # TODO
    # The "in" built-in is used to determine if the val is in the unsorted list
    @staticmethod
    def find3(self, val: int):
        return val in self
    #
    # # TODO
    # # This function requires the list to be sorted before it is called. A binary search is
    # # performed on the pre-sorted list to find val.
    # def find4(self, list_input: list, val: int = 0):
    #     return True
