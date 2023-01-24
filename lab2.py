#lab2
surname = str(input('surname:')) #вводим фамилию
name = str(input('name:')) #вводим имя
email = str(input('email:')) #вводим имэйл
n = int(input('n:'))
if n > 50: #если n больше чем 50 то выводим name
    print(name)
elif n == 0: # если же n равно нулю то выводим surname
    print(surname)
else: #в противном случае выводим email
    print(email)

