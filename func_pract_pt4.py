# question 1
def max_num(a,b,c):
    return max(a,b,c)

print(max_num(12,24,3))

# question 3
def mult_list(*list):

    if len(list) == 0:
        return 0
    else:
        product = list[0]
        for i in list:
            product = product * i

    return product
        
print(mult_list())
print(mult_list(3,4,5))

# question 3
def rev_string(str):
    
    if len(str) <= 1:
        return str
    else:
        return str[::-1]

print(rev_string('term'))

# question 4
def num_within(a,b,c):
    if b <= a <= c:
        return True
    else:
        return False

print(num_within(3,1,3))
print(num_within(10,2,5))

