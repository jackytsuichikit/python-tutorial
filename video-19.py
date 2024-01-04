
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# list[start:end:step]

print(my_list[5]) #the 5+1 number in the list
print(my_list[0:5]) #the 0+1 number to the 5+1 number on the list
#- = counting from behind
print(my_list[2:7:2])# skipps every 2nd value
print(my_list[2:7:-1])# count from behind (literally)
#
#
#
sample_url = 'https://replit.com/~'
print(sample_url)
print(sample_url[::-1])# reverse the url
print(sample_url[7:])# get part of the url