immutable_var=('cat', 1, 2.5, [1,2,3,4,5], True)
print('Изначальный кортеж:',immutable_var)
#попытаемся изменить элемент кортежа
#immutable_var[4]=False
#У нас не получилось изменить кортеж, тк кортеж относится к неизменяемым объектам. Но элемент список, который является частью элементов кортежа, мы изменять можем к примеру ниже попытаемся изменить список:
immutable_var[3][2]='fox' 
print('Кортеж и измененным списком:',immutable_var)
mutable_list=[True,'rat',123.3]
print('Изначальный список:',mutable_list)
mutable_list[0:]=False,'dog',321
print('Измененный список:',mutable_list)

