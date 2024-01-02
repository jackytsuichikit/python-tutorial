'''
LEGB
Local, Enclosing, Global, Built in
'''

#import builtins

#print(dir(builtins))

#def my_min():
#    pass

#m = min([5, 1, 4, 2, 3]) #minimum numb is 1
#print(m)

#x = 'globe x' #alr stated

#def test():
    #y = 'local y'
    #x = 'global x'
    #print(y)
    #print(x)

#test()    
#print(x)

def outer():
    x = 'outer x'

    def inner():
        nonlocal x
        x = 'inner x'
        print(x)

    inner()
    print(x)   
    