def merge_sort(L):  # "разделяй"
    if len(L) < 2:  # если кусок массива меньше 2,
        return L[:]  # выходим из рекурсии
    else:
        middle = len(L) // 2  # ищем середину
        left = merge_sort(L[:middle])  # рекурсивно делим левую часть
        right = merge_sort(L[middle:])  # и правую
        return merge(left, right)  # выполняем слияние


def merge(left, right):  # "властвуй"
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return right # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


array = list(map(int, input("Введите числа через пробел").split()))

sequence = merge_sort(array)
print("Отсортированный список:", sequence)

while True:
    try:
        element = int(input("Введите любое положительное целое число из полученного списка: "))
        if element <= 0:
            raise Exception
        break
    except ValueError:
        print("Нужно ввести целое число!")
    except Exception:
        print("Нужно ввести положительное число!")
if element <= min(sequence) or element > max(sequence):
    print("Указанное число не входит в диапазон списка!")
else:
    print("Номер позиции", binary_search( sequence, element, 0,  len(array)))




