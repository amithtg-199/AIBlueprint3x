# def add(*args):
'''Unlimited Positional Arguments'''
#     print(args[0])
#     print(args[1])
#     print(args[5])

# def add(*args):
'''type tuple'''
#     print(type(args))
#     print(args)

def add(*args):
    '''args function'''
    total = 0
    for n in args:
        total += n
    print(total)

add(1,2,3,4,5,6,7,8,9,10)