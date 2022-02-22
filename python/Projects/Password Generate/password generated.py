import string
import secrets
from typing import Final

try:
    symblos = int(input("Введите кол-во символов в пароле:"))
    symbolsNum = int(symblos)
    apl = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(apl) for i in range(symbolsNum))
    print(password)
except ValueError :
    print("Нужно ввести числовое значение")
finally:
    print("Блок проверки завершил выполнение")
    print("Завершение программы")
