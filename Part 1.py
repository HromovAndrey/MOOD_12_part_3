# Завдання 2
# Створіть клас черги з пріоритетами для роботи із
# символьними значеннями.
# Ви маєте створити реалізації для операцій над елементами черги:
# ■ IsEmpty — перевірка, чи черга пуста;
# ■ IsFull — перевірка черги на заповнення;
# ■ InsertWithPriority — додати елемент з пріоритетом у
# чергу;
# Практичне завдання
# 1
# ■ PullHighestPriorityElement — видалення елемента з
# найвищим пріоритетом із черги;
# ■ Peek — повернення найбільшого за пріоритетом елемента. Зверніть увагу, що елемент не видаляється з
# черги;
# ■ Show — відображення на екрані всіх елементів черги.
# Показуючи елемент, також необхідно вказати і його
# пріоритет.
# На старті додатка відобразіть меню, в якому користувач може вибрати необхідну операцію.

class PriorityQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.max_size

    def insert_with_priority(self, char, priority):
        if not self.is_full():
            self.queue.append((char, priority))
            self.queue.sort(key=lambda x: x[1], reverse=True)
        else:
            print("Черга повна")

    def pull_highest_priority_element(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Черга порожня")
            return None

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Черга порожня")
            return None

    def show(self):
        print("Елементи черги з пріоритетами:")
        for char, priority in self.queue:
            print(f"Елемент: {char}, Пріоритет: {priority}")

def display_menu():
    print("Меню:")
    print("1. Перевірити, чи черга порожня")
    print("2. Перевірити, чи черга повна")
    print("3. Додати елемент з пріоритетом до черги")
    print("4. Видалити елемент з найвищим пріоритетом з черги")
    print("5. Подивитися найбільш пріоритетний елемент")
    print("6. Відобразити елементи черги")
    print("0. Вихід")

max_size = 5
priority_queue = PriorityQueue(max_size)

while True:
    display_menu()
    choice = input("Оберіть операцію: ")

    if choice == '1':
        print("Черга порожня:", priority_queue.is_empty())
    elif choice == '2':
        print("Черга повна:", priority_queue.is_full())
    elif choice == '3':
        char = input("Введіть символ для додавання до черги: ")
        priority = int(input("Введіть пріоритет: "))
        priority_queue.insert_with_priority(char, priority)
    elif choice == '4':
        pulled_element = priority_queue.pull_highest_priority_element()
        if pulled_element is not None:
            print(f"Видалений елемент з найвищим пріоритетом: {pulled_element[0]}, Пріоритет: {pulled_element[1]}")
    elif choice == '5':
        highest_priority_element = priority_queue.peek()
        if highest_priority_element is not None:
            print(f"Найбільш пріоритетний елемент: {highest_priority_element[0]}, Пріоритет: {highest_priority_element[1]}")
    elif choice == '6':
        priority_queue.show()
    elif choice == '0':
        print("Дякую за користування! Завершення програми.")
        break
    else:
        print("Некоректний вибір. Спробуйте ще раз.")
