import matplotlib.pyplot as plt


def mergeSort(list_to_sort_by_merge):
    if (
        len(list_to_sort_by_merge) > 1
        and len(list_to_sort_by_merge) != 0
    ):
        mid = len(list_to_sort_by_merge) // 2
        left = list_to_sort_by_merge[:mid]
        right = list_to_sort_by_merge[mid:]

        mergeSort(left)
        mergeSort(right)

        l = 0
        r = 0
        i = 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=left, j=l)
                l += 1
            else:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=right, j=r)
                r += 1
            i += 1

        while l < len(left):
            list_to_sort_by_merge[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            list_to_sort_by_merge[i] = right[r]
            r += 1
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