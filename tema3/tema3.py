# dupa ce ati citit articolul vreau sa incercati sa calculati recursiv seria 1^2+2^2+3^2...
# folosind o functie scrisa de voi ce primeste ca argument doar numarul de ordine
# exemplu de logica 1^2+2^2 este 1^2+(1^2+1^2)^2

def sum_of_square(n: int):
    if n < 2:
        return 1
    else:
        return n ** 2 + sum_of_square(n - 1)


print(sum_of_square(10))


# sctrieti o functie care calculeaza n! fara sa folositi recursivitatea


def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact


print(factorial(10))


# creati o functie care primeste un string ca argument si returneaza un tuple aplicand urmatoarele actiuni:
# - string-ul initial este impartit dupa primul spatiu si in contiunuare vom modifica doar ce este dupa spatiu
# - tate caracterele care nu sunt litere mici vor fi inlocutite cu _
# tuple-ul returnat contine prima parte de text (pana la primul spatiu) si partea modificata
# exemplu (1234567A Text de te5t > (1234567A, _ext_de_te_t))

def process_text(text: str):
    lst = text.split(' ', 1)
    text1 = lst[1]
    text2 = ''
    for letter in text1:
        if not ((ord(letter) >= 97) and (ord(letter) <= 122)):
            text2 = text1.replace(letter, '_')
            text1 = text2

    lst[1] = text2
    return tuple(lst)


print(process_text('1234567a Text de te5t'))
