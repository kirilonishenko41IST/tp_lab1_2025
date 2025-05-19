import random

words = ["ананас", "малина", "пальма", "машина", "школа", "сонце", "друзі", "горіхи", "компот", "печиво"]
word = random.choice(words)
hidden = ["_"] * len(word)
attempts = 7
used_letters = set()

print("Вітаємо у грі 'Вгадай слово'!")

while attempts > 0 and "_" in hidden:
    print("\nЗагадане слово:", " ".join(hidden))
    print(f"У вас є {attempts} спроб.")
    letter = input("Введіть літеру: ").lower()

    if letter in used_letters:
        print("Цю літеру ви вже вводили.")
        continue

    used_letters.add(letter)

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                hidden[i] = letter
    else:
        print("Немає такої літери.")
        attempts -= 1

if "_" not in hidden:
    print(f"Вітаємо! Ви вгадали слово \"{word}\"!")
else:
    print(f"На жаль, ви програли. Загадане слово було: \"{word}\".")
