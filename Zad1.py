# ZADANIE 1. GENERATOR KODÓW POCZTOWYCH
# przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi


def list_of_codes(first, last):
    start = int(first.split('-')[0] + first.split('-')[1])
    end = int(last.split('-')[0] + last.split('-')[1])

    list = []
    for i in range(start, end):
        number = str(i)
        list.append(number[:2] + '-' + number[2:])
    return list