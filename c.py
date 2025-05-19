tasks = []

def show_menu():
    print("\nОберіть дію:")
    print("1. Додати завдання")
    print("2. Переглянути завдання")
    print("3. Позначити як виконане")
    print("4. Видалити завдання")
    print("5. Вийти")

while True:
    show_menu()
    choice = input("Введіть номер дії: ")

    if choice == "1":
        task = input("Введіть опис завдання: ")
        tasks.append({"text": task, "done": False})
    elif choice == "2":
        if not tasks:
            print("Список завдань порожній.")
        else:
            print("Список завдань:")
            for i, task in enumerate(tasks, start=1):
                status = "[x]" if task["done"] else "[ ]"
                print(f"{i}. {status} {task['text']}")
    elif choice == "3":
        num = int(input("Введіть номер виконаного завдання: "))
        if 0 < num <= len(tasks):
            tasks[num - 1]["done"] = True
    elif choice == "4":
        num = int(input("Введіть номер завдання для видалення: "))
        if 0 < num <= len(tasks):
            tasks.pop(num - 1)
    elif choice == "5":
        print("Дякую за використання!")
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")
