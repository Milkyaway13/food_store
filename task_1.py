def generate_sequence(n):
    sequence = []
    number = 1

    while len(sequence) < n:
        sequence.extend([number] * number)
        number += 1

    return sequence[:n]


n = int(input("Введите количество элементов последовательности: "))
print(generate_sequence(n))
