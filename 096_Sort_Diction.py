dict = [{'name': 'Prince', 'age':19},
        {'name': 'Maurya', 'age':19},
        {'name': 'Nobita', 'age':15}]

sorted_dict = sorted(dict, key = lambda x: x['age'])
print('Sorted Dictionaries :', sorted_dict)