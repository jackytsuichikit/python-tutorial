print('Import my_module...')

def test():
    return 'Test String'

def find_index(to_search, target):
    #find_the_index_of_a_value_in_a_sequesnce
    for i, value in enumerate(to_search):
    #enumerate = count
        if value == target:
            return i
        
    return -1

'''
docstring  (comment block)

video-13.py#23-25
my_module.py::find_index()

html5 css3 YouTube
'''