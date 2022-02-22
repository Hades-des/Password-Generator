
import string
import secrets

symblos = int(input("Введите кол-во символов в пароле:"))
apl = string.ascii_letters + string.digits + string.punctuation

try:
 symblosRam = int(symblos)
except ValueError:
    print("Это не числовое значение")

password = ''.join(secrets.choice(apl) for i in range(symblosRam))

print(password)