def count_common_elements(*lists):
    # Преобразуем первый список в множество
    common_elements = set(lists[0])

    # Перебираем остальные списки
    for lst in lists[1:]:
        # Находим пересечение с текущим списком
        common_elements.intersection_update(lst)

    # Возвращаем количество общих элементов
    return len(common_elements)


# Ввод количества списков
n = int(input("Введите количество списков: "))
lists = []

# Ввод списков
for i in range(n):
    lst = input(f"Введите элементы списка {i + 1} через пробел: ").split()
    lists.append(lst)

# Вычисление и вывод результата
result = count_common_elements(*lists)
print(f"Количество одинаковых элементов: {result}")