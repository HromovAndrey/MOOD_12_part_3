# Завдання 3
# Розробіть додаток, який дозволяє зберігати інформацію
# про логіни і паролі користувачів. Кожному користувачеві
# відповідає пара «логін — пароль». При старті додатку
# відображається меню:
# ■ Додати нового користувача;
# ■ Видалити існуючого користувача;
# ■ Перевірити, чи існує такий користувач;
# ■ Змінити логін існуючого користувача;
# ■ Змінити пароль існуючого користувача.
# Для реалізації завдання обов’язково застосуйте одну
# із структур даних. При виборі структури керуйтеся постановкою завдання.
# Практичне завдання

class UserDatabase:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if username not in self.users:
            self.users[username] = password
            print("Користувача успішно додано.")
        else:
            print("Користувач з таким логіном вже існує.")

    def delete_user(self, username):
        if username in self.users:
            del self.users[username]
            print("Користувача успішно видалено.")
        else:
            print("Користувач з таким логіном не існує.")

    def check_user(self, username):
        if username in self.users:
            print("Користувач з таким логіном існує.")
        else:
            print("Користувача з таким логіном не існує.")

    def change_username(self, old_username, new_username):
        if old_username in self.users:
            self.users[new_username] = self.users.pop(old_username)
            print("Логін користувача успішно змінено.")
        else:
            print("Користувача з таким логіном не існує.")

    def change_password(self, username, new_password):
        if username in self.users:
            self.users[username] = new_password
            print("Пароль користувача успішно змінено.")
        else:
            print("Користувача з таким логіном не існує.")

def display_menu():
    print("Меню:")
    print("1. Додати нового користувача")
    print("2. Видалити існуючого користувача")
    print("3. Перевірити, чи існує такий користувач")
    print("4. Змінити логін існуючого користувача")
    print("5. Змінити пароль існуючого користувача")
    print("0. Вихід")

user_db = UserDatabase()

while True:
    display_menu()
    choice = input("Оберіть операцію: ")

    if choice == '1':
        username = input("Введіть логін нового користувача: ")
        password = input("Введіть пароль нового користувача: ")
        user_db.add_user(username, password)
    elif choice == '2':
        username = input("Введіть логін користувача для видалення: ")
        user_db.delete_user(username)
    elif choice == '3':
        username = input("Введіть логін користувача для перевірки: ")
        user_db.check_user(username)
    elif choice == '4':
        old_username = input("Введіть старий логін користувача: ")
        new_username = input("Введіть новий логін користувача: ")
        user_db.change_username(old_username, new_username)
    elif choice == '5':
        username = input("Введіть логін користувача: ")
        new_password = input("Введіть новий пароль для користувача: ")
        user_db.change_password(username, new_password)
    elif choice == '0':
        print("Дякую за користування! Завершення програми.")
        break
    else:
        print("Некоректний вибір. Спробуйте ще раз.")


