4
premteams = ['man city', 'man united', 'arsnel', 'liverpool']  
print(premteams[0:3])

premteam_inferior = ['chelsea', 'hotspurs']
premteams.extend(premteam_inferior)
print('extended:', premteams, len(premteams))
premteams.append(premteam_inferior)
print("appended: ", premteams,  len(premteams))

for index, premteams in enumerate(premteams, start=1):
   print(index, premteams)
premteams_str = ' - '.join(premteams)   
new_premteams = premteams_str.split(' - ')
print(premteams_str)


# import numpy as np 
# x = np.linspace(1, 10)
# print(type(x))
# print(x)


