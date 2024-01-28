import csv


class bookmenager:
    booklist = []
    player = []

    @staticmethod
    def add_book(dat):
        with open('book.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(dat) 



bookm = bookmenager()

def get_book():
    bookm.booklist = []
    with open('book.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            bookm.booklist.append(row)
    return bookm.booklist

def selected(afd):
    if afd == 1:
        for row in bookm.booklist:
            print("{:<5} {:<10}".format(row[0], row[1]))
        
        print("Выберите книгу")
        idbook = input()
        print("Вы арендавали книгу необходимо ее вернуть через 14 дней")
        main()
    if afd == 2:
        print("Введите имя:")
        name = input()
        if checkuser(name) == True:
            print("Чтобы добавить книгу введите название")
            namebook = input()
            print("Введите цену аренды книги")
            pricebook = int(input())
            bookm.add_book([f"{namebook}", f"{pricebook}"])
        if checkuser(name) == False:
            print("Ты не пройдешь в систему!")
            main()
    if afd == 3:
        return

def get_user():
    bookm.player = []
    with open('users.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            bookm.player.append(row)
    return bookm.player

def checkuser(name):
    for row in bookm.player:
        if name in row:
            return True
    return False


def main():
    get_user()
    get_book()
    print("1. Арендавать книгу \n2. Авторизация \n Выйти")
    ab = int(input())
    selected(ab)


main()
import json
import csv

def save_data(data):
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)

def load_data():
    try:
        with open('data.json', 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return []

def delete_save(index):
    data = load_data()
    if index < len(data):
        data.pop(index)
        save_data(data)

def update_csv(data):
    with open('data.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Username', 'Score'])
        for user_data in data:
            writer.writerow([user_data['username'], user_data['score']])

# Пример использования функций
user1 = {'username': 'user1', 'score': 10}
user2 = {'username': 'user2', 'score': 15}

data = load_data()
data.append(user1)
data.append(user2)
save_data(data)

for i, user_data in enumerate(data):
    print(f"{i+1}. {user_data['username']}: {user_data['score']}")

delete_save(0)  # Удаление первого сохранения

data = load_data()
update_csv(data)
