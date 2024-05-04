from view import Add
from view import Delete
from view import Edit
from view import Exit


class Menu:

    def __init__(self, add=Add(), edit=Edit(), delete=Delete(), exit=Exit()):
        self.list = list()
        list.append(self.list, add)
        list.append(self.list, edit)
        list.append(self.list, delete)
        list.append(self.list, exit)


    def print(self):
        print("Вам доступны следующие действия:\n")
        for i in range(1, len(self.list)+1):
            print("{0}.\t{1}".format(i, self.list[i-1].print()))