def exerc1(saud, name):
    print(saud, name)


exerc1("Olá", "Pedro")


def exerc2(num1, num2, num3):
    print(num1 + num2 + num3)


exerc2(3, 5, 9)


def exerc3(num1, num2):
    print(num1 + num1 * num2 / 100)


exerc3(100, 10)


def exerc4(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'Fizzbuzz'
    if num % 3 == 0:
        return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'
    return num


print(exerc4(15))
