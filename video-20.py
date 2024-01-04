numb = [1,2,3,4,5,6,7,8,9,10]

## my_list = [] #make an empty list
# for n in numb:
#     my_list.append(n) #insert the list numb into my_list
#     print(my_list)

# my_list = [n for n in numb]
# print(my_list)

# my_list = [n*n for n in numb]
# print(my_list)

# my_list = map(lambda n: n*n, numb) #???
# print(my_list)

# my_list =[] #only show even numbers
# for n in numb:
#     if n%2 == 0:
#         my_list.append(n)
# print(my_list)

# my_list = [n for n in numb if n%2 ==0]   #only insert even numbers in my_list
# print(my_list) 

# my_list = [] #pair numbers with letter
# for letter in "abcd":
#     for num in range(4):
#         my_list.append((letter,num))
# print(my_list)   

# my_list = [(letter, num) for letter in "abcd" for num in range(4)]     #same but clearer and faster
# print(my_list)

# names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
# heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# # my_dict = {} #match name to it's corresponding hero
# # for name, hero in zip(names, heros):
# #     my_dict[name] = hero
# # print(my_dict)    

# my_dict = {name: hero for name, hero in zip (names, heros)}
# print(my_dict)

numb = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9] #only get unique values/ one value can only be chosen once
# my_set = set()
# for n in numb:
#     my_set.add(n)
# print(my_set)    

# my_set = {n for n in numb} #same but simpler
# print(my_set)

print(numb)