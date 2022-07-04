
# ZADANIE 1. GENERATOR KODÓW POCZTOWYCH
# przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi

# Result
# 1. I got rid off '-' in input strings
# 2. then turned it into int
# 3. I used list comprehension to show all elements between input1 and input2 as strings
# 4. I added '-' between numbers
# 5. Returned list of postall codes


def postal_code_generator(input_str1,input_str2):
    return [(x[:2]+'-'+ x[2:]) for x in [str(element) for element in range(int("".join(input_str1[:2]+input_str1[3:])), int("".join(input_str2[:2]+input_str2[3:])))]]

print(postal_code_generator("79-900","80-155"))



# ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1-n. NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE
# 1-n = [1,2,3,4,5,...,10]
# np. n=10
# wejście: [2,3,7,4,9], 10
# wyjście: [1,5,6,8,10]

# Result
# 1. I generated list of all numbers 1-n without '0' and numbers from input
# 2. I used this list for comprehension of results

def missing_args(input,n):
    return [x for x in [x for x in range(n+1)][1:] if x not in input]
    

input = [2,3,7,4,9]
n = 10
print(missing_args(input,n))


# ZADANIE 3. NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5, DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL.
# Wszystkie programy proszę zrealizować w postaci funkcji, bez interfejsu i walidacji danych.

# Result
# 1. I used numpy to import arange which provides working with floats
# 2. Then I used Decimal class to represent all results as decimal values in list
# I'm really curious if that's a point :)

from numpy import arange as ar
from decimal import Decimal

def float_list_generator(start,stop,step):    
    return [Decimal(x) for x in ar(start, stop+0.5, step, dtype=float)]
    

start = 2
stop = 5.5
step = 0.5

print(float_list_generator(start=start,stop=stop,step=step))

