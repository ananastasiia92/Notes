import datetime


class Notebook:

    def __init__(self):
        self.id = None

    def id_counter(self):
        with open('Notes.txt', 'r', encoding='utf8') as temp:
            data = temp.readlines()
            if len(data) == 0:
                self.id = 1
            else:
                line = data[len(data) - 4]
                num = int(line[1])
                self.id = num + 1

    def show_notes(self):
        with open('Notes.txt', 'r', encoding='utf8') as file:
            line = file.read()
            if len(line) == 0:
                print("У вас пока нет заметок...\n")
            else:
                print('Ваши заметки:\n')
                print(line)

    def add_note(self, title, text):
        self.id_counter()
        with open('Notes.txt', 'a', encoding='utf8') as file:
            date = datetime.datetime.today().strftime("%Y-%m-%d")
            file.write("№{0}.\tTitle: {1}\n\tText: {2}\n\tDate: {3}\n\n".format(self.id, title, text, date))

    def delete_note(self, id):
        with open('Notes.txt', 'r', encoding='utf8') as file:
            temp = file.readlines()
        work_file = open('Notes.txt', 'w', encoding='utf8')
        inp = "№" + id
        count = 0
        for line in temp:
            if str(inp) in str(line):
                del temp[count:count + 4]
                result = "".join(temp)
                work_file.write(result)
                break
            else:
                count += 1
        if count == len(temp):
            print('Данные не найдены!')
        work_file.close()

    def edit_note(self, id):
        with open('Notes.txt', 'r', encoding='utf8') as file:
            temp = file.readlines()
        work_file = open('Notes.txt', 'w', encoding='utf8')
        inp = "№" + id
        count = 0
        for line in temp:
            if str(inp) in str(line):
                del temp[count:count + 4]
                title = input('Title: ')
                text = input('Text: ')
                date = datetime.datetime.today().strftime("%Y-%m-%d")
                line = ("№{0}.\tTitle: {1}\n\tText: {2}\n\tDate: {3}\n\n".format(id, title, text, date))
                temp.insert(count, line)
                result = "".join(temp)
                work_file.write(result)
                break
            else: count += 1
        if (count == len(temp)):
            print('Данные не найдены!')

    def test(self):
        with open('Notes.txt', 'r', encoding='utf8') as file:
            temp = file.read()
            print(temp)