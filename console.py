from presenter import Presenter
from menu import Menu


class Console:

    def __init__(self):
        self.presenter = Presenter()
        self.menu = Menu()
        self.work = True

    def start_menu(self):
        while self.work:
            self.presenter.show_notes()
            self.menu.print()
            choice = input("Ваш выбор: ")
            if int(choice) == 1:
                self.add_note()
            elif int(choice) == 2:
                self.edit_note()
            elif int(choice) == 3:
                self.delete_note()
            elif int(choice) == 4:
                self.exit()
                self.work = False
            else:
                print("Неверный выбор!")

    def set_title(self):
        title = input("Title: ")
        return title

    def set_text(self):
        text = input("Text: ")
        return text

    def add_note(self):
        self.presenter.add_note(self.set_title(), self.set_text())

    def edit_note(self):
        id = input("Введите порядковый номер заметки: ")
        self.presenter.edit_note(id)

    def delete_note(self):
        id = input("Введите порядковый номер заметки: ")
        self.presenter.delete_note(id)

    def exit(self):
        print("Работа с заметками завершена!")

    def test(self):
        self.presenter.test()