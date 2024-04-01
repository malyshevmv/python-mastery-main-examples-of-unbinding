from collections import defaultdict


# Створення defaultdict зі значенням за замовчуванням 0
counter = defaultdict(int)

# Список елементів
my_list = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1]

# Підрахунок кількості входжень кожного елемента
for element in my_list:
    counter[element] += 1

# Виведення результатів
for key, value in counter.items():
    print(f"{key}: {value}")
