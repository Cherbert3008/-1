numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

len_numbers = len(numbers) #Количество элементов в списке

#Создание вспомогательного списка без пропущенного элемента
numbers_without_none = numbers[:4] + numbers[5:]

sum_numbers = sum(numbers_without_none) #Сумма чисел
average_numbers = sum_numbers / len_numbers #Среднее значение

#Замена пропущенного элемента средним арифметическим
numbers[4] = average_numbers

print("Измененный список:", numbers)
