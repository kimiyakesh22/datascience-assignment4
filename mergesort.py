#import matplotlib.pyplot as plt # Import nach PEP8 an den Anfang der Datei verschoben
import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

def merge_sort(values): # Funktionsname in snake_case umbenannt (PEP8)
    """ Sortiert eine Liste mithilfe des Merge-Sort-Algorithmus.
    Der Algorithmus teilt die Liste rekursiv in kleinere Teillisten, sortiert diese und fügt sie anschließend in der richtigen Reihenfolge wieder zusammen.
    Nach dem Divide and conquer, dabei ist left_values, die linke Seite des Arrays, analog right_values für rechts, sprich hier teilen wir das Array auf.
    Weil wir die zwei Werte aus dem separierten Teil miteinader vergleichen wollen, brauchen wir einen Index, dieser ist startend bei 0, um den ersten Wert mit dem weiteren zuvergleichen, umzuschauen, welcher groesser bzw. kleiner ist und wie man was hinkriegen soll:
    wir sortieren aufsteigend, also links die kleineren Werte und die groessern nach rechts. Wichitg ist zu notieren, das diese Sortierung nur solange laufen wird bis nur noch ein Wert enthalten ist, weil wir immer zwei Werte miteinader vergleichen wollen.
    Die Liste in-place sortiert, d.h. wir muessen nicht zusaetzlich eine Liste initializieren, in der die veraenderten Werte reinkommen"""
    

    if len(values) > 1: # Bedingung vereinfacht für bessere Lesbarkeit

        middle = len(values) // 2
        left_values = values[:middle]
        right_values = values[middle:] # Aussagekräftigere Variablenname, welche genau sagen, was ich der jeweiligen Variable zuweise, hier Werte Betrachtung

        merge_sort(left_values)
        merge_sort(right_values)

        left_index = 0
        right_index = 0
        merged_index = 0 # Aussagekräftigere Variablenname, welche genau sagen, was ich der jeweiligen Variable zuweise, hier Index Betrachtung

        while left_index < len(left_values) and right_index < len(right_values):
            if left_values[left_index] <= right_values[right_index]:

                values[merged_index] = left_values[left_index]
                # Direkte Zuweisung statt unnötiger ASSIGNMENT()-Hilfsfunktion

                left_index += 1
            else:
                values[merged_index] = right_values[right_index] # Direkte Zuweisung statt unnötiger ASSIGNMENT()-Hilfsfunktion

                right_index += 1

            merged_index += 1

        while left_index < len(left_values):
            values[merged_index] = left_values[left_index]
            left_index += 1
            merged_index += 1

        while right_index < len(right_values):
            values[merged_index] = right_values[right_index]
            right_index += 1
            merged_index += 1


def plot_values(values, title):
    """
    Erstellt ein Balkendiagramm der Werte.
    """

    plt.figure(figsize=(8, 4))
    plt.bar(range(len(values)), values)

    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Value")

    plt.grid(True)
    plt.show()

if __name__ == "__main__":

    my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    plot_values(my_list, "Unsorted Values")

    merge_sort(my_list)

    plot_values(my_list, "Sorted Values")

