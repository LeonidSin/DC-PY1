list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
MAX = max(list_numbers)
temp = list_numbers[-1]
for pos, value in enumerate(list_numbers, start=0): # TODO Оформить решение
    if value == MAX:
        #print(pos, value)
        list_numbers[pos] = temp
        list_numbers[-1] = value
print(list_numbers)
