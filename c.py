list = []

while True:
    print("1. Додати")
    print("2. Показати")
    print("3. Виконано")
    print("4. Видалити")
    print("5. Вихід")

    x = input("Ваш вибір: ")

    if x == "1":
        t = input("Нове завдання:")
        list.append([t, False])
    elif x == "2":
        for i in range(len(list)):
            z = list[i]
            done = "x" if z[1] else " "
            print(i+1, "[{}]".format(done), z[0])
    elif x == "3":
        n = int(input("Номер:"))
        list[n-1][1] = True
    elif x == "4":
        n = int(input("Номер:"))
        list.pop(n-1)
    elif x == "5":
        break
