# Завдання 1
# Створіть клас черги для роботи із символьними значеннями. Ви маєте створити реалізації для операцій над
# елементами:
# ■ IsEmpty — перевірка, чи черга пуста;
# ■ IsFull — перевірка черги на заповнення;
# ■ Enqueue — додати новий елемент до черги;
# ■ Dequeue — видалення елемента з черги;
# ■ Show — відображення на екрані всіх елементів черги.
# На старті додатка відобразіть меню, в якому користувач може вибрати необхідну операцію.

class CharQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.max_size

    def enqueue(self, char):
        if not self.is_full():
            self.queue.append(char)
        else:
            print("Черга повна")

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Черга порожня")
            return None

    def show(self):
        print("Елементи черги:", self.queue)

def display_menu():
    print("Меню:")
    print("1. Перевірити, чи черга порожня")
    print("2. Перевірити, чи черга повна")
    print("3. Додати новий елемент до черги")
    print("4. Видалити елемент з черги")
    print("5. Відобразити елементи черги")
    print("0. Вихід")

max_size = 5
queue = CharQueue(max_size)

while True:
    display_menu()
    choice = input("Оберіть операцію: ")

    if choice == '1':
        print("Черга порожня:", queue.is_empty())
    elif choice == '2':
        print("Черга повна:", queue.is_full())
    elif choice == '3':
        char = input("Введіть символ для додавання до черги: ")
        queue.enqueue(char)
    elif choice == '4':
        dequeued_char = queue.dequeue()
        if dequeued_char is not None:
            print("Видалений елемент з черги:", dequeued_char)
    elif choice == '5':
        queue.show()
    elif choice == '0':
        print("Дякую за користування! Завершення програми.")
        break
    else:
        print("Некоректний вибір. Спробуйте ще раз.")

