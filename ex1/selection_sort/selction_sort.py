import numpy as np
import matplotlib.pyplot as plt


def sort(elements):
    operations = 0
    for i in range(len(elements)):
        min = i
        for j in range(i + 1, len(elements)):
            operations += 1
            if elements[j] < elements[min]:
                min = j
        elements[i], elements[min] = elements[min], elements[i]
    return elements, operations


def main():
    elements = list()
    operations_list = list()
    for i in range(1, 8000, 100):
        numbers = np.random.randint(0, 100, size=i)
        sorted, operations = sort(numbers)
        operations_list.append(operations)
        elements.append(i)

    squares = list(map(lambda x: (x ** 2) / 2, elements))
    print(squares)

    plt.xlabel("No. of elements")
    plt.ylabel("No. operations")
    plt.plot(elements, operations_list, color="b", label="experiment")
    plt.plot(elements, squares, color="r", label="theoretical")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
