# question 1
def arb_args(*items):
    for i in items:
        print(i)

arb_args('garb', 'garb1', 'garb2')

# question 2
def inner_func(a, b):

    def add_func(a,b):
        return a + b
    
    def mult_func(a,b):
        return a * b
    
    add_val = add_func(a,b)
    mult_val = mult_func(a,b)

    return print(add_val + mult_val)

inner_func(3,2)

# question 3
def lunch_lady(name, lunch='Mystery Meat'):
    return print(f'My name is {name}, and I like {lunch}')

lunch_lady('Tanner')
lunch_lady('Andrew', 'Pizza')

# question 4
def sum_n_product(a, b):

    add_val = a + b
    mult_val = a * b

    return print(f'The sum is {add_val} and the product is {mult_val}')

sum_n_product(2, 8)

# question 5
alias_arb_arg = arb_args

alias_arb_arg('Same', 'Same')

# question 6
def arb_mean(*nums):

    sum_nums = sum(nums)
    avg = sum_nums / len(nums)
    return print(avg)

arb_mean(3, 4, 5)

# question 7
def arb_longest_string(*str):

    longest_index = 0
    longest_str = ''
    
    for s in str:
        if len(s) > longest_index:
            longest_index = len(s)
            longest_str = s
    
    return print(longest_str)

arb_longest_string('abs', 'horses', 'cows', 'ice cream', 'burger')