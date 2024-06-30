immutable_var = ('Привет', 1, 2, True)
print(immutable_var)
#immutable_var[0][0] = 'Пока' # Кортеж не изменяемый меняется только список, но в кортеж можно добавить список
immutable_var = (['Привет'], 1, 2, True)
immutable_var[0][0] = 'Пока'
print(immutable_var)
mutable_list = [1, 2, 3, 'четыре', 'пять']
mutable_list[0] = 'один'
mutable_list.append(6)
print(mutable_list)