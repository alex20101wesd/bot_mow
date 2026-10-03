import random


caracteres="2134567897oiujhqefsdgsfg"


def generar_password(longitud):

    password=""

    for i in range(longitud):
        password+=random.choice(caracteres)

    return password
