import numpy as np
import matplotlib.pyplot as plt


def sort(elements):
    operations = 0
    for i in range(1, len(elements)):
        j = i
        operations += 1
        while j > 0 and elements[j] < elements[j - 1]:
            operations += 1
            elements[j], elements[j - 1] = elements[j - 1], elements[j]
            j -= 1
    return elements, operations


def main():
    elements = list()
    operations_list = list()
    best_list = list()
    worst_list = list()
    for i in range(1, 500, 5):
        numbers = np.random.randint(0, 100, size=i)
        best = numbers.copy()
        best.sort()
        worst = best.copy()
        worst = worst[::-1]
        _, operations = sort(numbers)
        _, op = sort(best.copy())
        _, op2 = sort(worst.copy())
        best_list.append(op)
        worst_list.append(op2)
        operations_list.append(operations)
        elements.append(i)

    squares = list(map(lambda x: (x ** 2) / 4, elements))

    plt.xlabel("No. of elements")
    plt.ylabel("No. operations")
    plt.plot(elements, operations_list, color="b", label="experiment: average case")
    plt.plot(elements, best_list, color="g", label="experiment: best case")
    plt.plot(elements, worst_list, color="r", label="experiment: worst case")
    plt.plot(elements, squares, color="y", label="theoretical (~N^2/4)")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
