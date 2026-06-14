"""
Mergesort Algorithmus.
Teilt die Liste rekursiv in zwei Hälften, sortiert diese und führt sie zusammen.
"""

import matplotlib.pyplot as plt


def mergesort(array):
    """Sortiert eine Liste in-place mit dem Mergesort-Algorithmus."""

    if len(array) <= 1:
        return

    # Liste aufteilen
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    # Hälften rekursiv sortieren
    mergesort(left)
    mergesort(right)

    # Sortierte Hälften zusammenführen
    li, ri, i = 0, 0, 0

    while li < len(left) and ri < len(right):
        if left[li] <= right[ri]:
            array[i] = left[li]
            li += 1
        else:
            array[i] = right[ri]
            ri += 1
        i += 1

    while li < len(left):
        array[i] = left[li]
        li += 1
        i += 1

    while ri < len(right):
        array[i] = right[ri]
        ri += 1
        i += 1


def plot_list(array, title):
    """Zeigt die Liste als Balkendiagramm."""
    fig, ax = plt.subplots()
    ax.bar(range(len(array)), array)
    ax.set_title(title)
    ax.set_xlabel("Index")
    ax.set_ylabel("Wert")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    plot_list(my_list, "Vor dem Sortieren")
    mergesort(my_list)
    plot_list(my_list, "Nach dem Sortieren")
