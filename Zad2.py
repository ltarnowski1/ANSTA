#ZADANIE 2. Podana jest lista zawierająca elementy o wartościach 1-n.
#Napisz funkcję, która sprawdzi, jakich elementów brakuje


def which_numbers_missing(list, n):

    list_1_n = []
    for i in range(1, n+1):
        list_1_n.append(i)

    return set(list_1_n).difference(set(list))

