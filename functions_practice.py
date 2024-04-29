def hello():
    print('Greetings User!')

def pack(item1, item2, item3):
    return [item1, item2, item3]

def eat_lunch(my_list):
    if not my_list:
        print('my lunchbox is empty :(')
    else:
        for i in range(len(my_list)):
            if i == 0:
                print('First I eat', my_list[0])
            else:
                print('Next I eat', my_list[i])


hello()
print(pack("item a","item b","item c"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["wings"])
eat_lunch(["wings","fries","celery","brownie"])