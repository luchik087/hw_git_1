my_dict = {'кошка': 'cat','собака':'dog', 'книга':'book'}
print('Был словарь:',my_dict)
print('Значение по существующему ключу:',my_dict['кошка'])
my_dict['огурец']='cucumber'
print('Значение по отсутствующему ключу:',my_dict['огурец'])
my_dict['крыса']='rat'
my_dict['глаз']='eye'
book = my_dict.pop('книга')
print('Удаленное значение:',book)
print('Что с ним стало:',my_dict)


my_set = {True, True, 1.1,1.1, 'c', 'c'}
print('Было множество:',my_set)
my_set.add(False)
my_set.add('Eminem')
my_set.remove(1.1)
print('Стало множество:',my_set)
