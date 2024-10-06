def print_params(a = 1, b = 'строка',c = True):
    print(a,b,c)

print_params(1), print_params(2, 2), print_params(3, 'Катя', False)
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = ['строка', 42, True]
values_dict = {'a': 52, 'b': "это не int", 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']

print_params(*values_list_2, 42)