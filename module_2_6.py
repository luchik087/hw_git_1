def get_password(n):
    password = ''
    for i in range(1,n):
        for j in range(n):
            if j <= i:
                continue
            if n % (i + j) == 0:
                password += f'{i}'+f'{j}'
    return password

n = int(input('Введите число от 3 до 20: '))

result = get_password(n)
print('Пароль:', result)
