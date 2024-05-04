from note import Notebook

class Presenter:

    def __init__(self):
        self.note = Notebook()

    def add_note(self, title, text):
        self.note.add_note(title, text)

    def show_notes(self):
        self.note.show_notes()

    def delete_note(self, id):
        self.note.delete_note(id)

    def edit_note(self, id):
        self.note.edit_note(id)

    def test(self):
        self.note.test()