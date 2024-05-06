# question 1
def flatten_dict(d):
    result = dict()

    for i in d.keys():
        if type(d[i]) == dict:
            for k,v in d[i].items():
                new_k = i + '.' + k
                result[new_k] = v
        else:
            result[i] = d[i]
    return result

print(flatten_dict({'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}))

# question 2
def unflatten_dict(d):
    result = dict()

    for i in d.keys():
        if '.' in i:
            new_key, sep, inner_key = i.partition('.')
            if new_key not in result.keys():
                result[new_key] = dict()
            result[new_key][inner_key] = d[i]
        else:
            result[i] = d[i]
    return result

print(unflatten_dict({'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}))

# question 3
def treemap(func, lst):
    for i in range(len(lst)):
        if type(lst[i]) == list:
            lst[i] = treemap(func, lst[i])
        else:
            lst[i] = func(lst[i])

    return lst

print(treemap(lambda i: i*i, [1, 2, [3, 4, [5]]]))