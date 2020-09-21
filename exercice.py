#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute() -> float:
    num = float((input('Please input a number: ')))
    if(num < 0):    
        num = -num
    return num


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOP', 'ack'
    noms = []
    for prefix in prefixes:
        nom = prefix + suffixes
        noms.append(nom)
    return noms


def prime_integer_summation() -> int:
    n=1
    num = 1
    sumofprimes = 0
    while n<=100:
        isPrime = True
        for n in range(2, num//2):
            if (num%n) == 0:
                isPrime=False

        if isPrime:
            sumofprimes+=num
            n += 1
            # print(f'{n} {num} {sumofprimes}')

        num+=2
    return sumofprimes


def factorial(number: int) -> int:
    fact=1
    for n in range(1, number):
        fact *= n
    return fact


def use_continue() -> None:
    for i in range(1, 11):
        if i==5: continue
        else: print(i)
    return 0


def main() -> None:
    # print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")

    use_continue()


if __name__ == '__main__':
    main()
