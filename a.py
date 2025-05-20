print("Розрахунок витрат на поїздку")

km = input("Введіть відстань до пункту призначення(км):")
km = float(km)

liters = input("Введіть середню витрату пального(л/100км):")
liters = float(liters)

price = input("Введіть середню ціну пального(грн/л):")
price = float(price)

people = input("Введіть кількість пассажирів:")
people = int(people)

total = (km / 100) * liters * price
one_person = total / people

print("Загальна вартість пального:", total)
print("Загальна вартість на одного пассажира:", round(one_person, 2))
