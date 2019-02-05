#ZADANIE 3. Należy wygenerować listę liczb od 2 do 5.5 ze skokiem co 0.5.
#Dane wynikowe muszą być typu decimal.

from decimal import Decimal


def list_of_decimal_numbers(first, last, step):

    list = []

    while (first<=last):
        list.append(Decimal(first))
        first = first + step
    return list
