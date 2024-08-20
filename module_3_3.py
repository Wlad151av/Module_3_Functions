def print_params(a=1,b='Строка',c=True):
    print(a,b,c)


print_params()
print_params(b=25)
print_params([1,2,3])
values_list = ['False',True,24.45]
print_params(*values_list)
values_dict = {'a':'dffs','b':3.54,'c':3}
print_params(**values_dict)
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)