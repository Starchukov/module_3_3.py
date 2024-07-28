def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(1,25)
print_params(1,'строка', [1,2,3])

value_list = [52, False, 'no']
value_dict = {'a': 1, 'b': True, 'c': 'yes'}

print_params(*value_list)
print_params(**value_dict)

values_list_2 = [67, False]
print_params(*values_list_2, 42)

