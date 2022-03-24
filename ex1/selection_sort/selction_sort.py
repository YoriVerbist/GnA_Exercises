import numpy as np


def sort(elements):
    for i in range(len(elements)):
        min = i
        for j in range(i + 1, len(elements)):
            if elements[j] < elements[min]:
                min = j
        elements[i], elements[min] = elements[min], elements[i]
    return elements


def main():
    numbers = np.random.randint(0, 100, size=50)
    print(numbers)
    print(sort(numbers))


if __name__ == "__main__":
    main()
