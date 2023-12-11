numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

left = numbers[:4]
right = numbers[5:]

mean_number = sum(left + right) / len(numbers)  # среднее число
numbers[4] = mean_number  # замена

print("Измененный список:", numbers)
