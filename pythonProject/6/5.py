def remove_odd_numbers(numbers):
    return [luku for luku in numbers if luku % 2 == 0]

numbers = [1, 2, 3, 21, 22, 23, 24, 100]
deleted_numbers = remove_odd_numbers(numbers)
print("Alkuperäinen lista:", numbers)
print("Karsittu lista:", deleted_numbers)
