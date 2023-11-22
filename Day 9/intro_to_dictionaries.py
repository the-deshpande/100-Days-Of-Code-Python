programming_dictionary = {
    'Bug':'An error in a program that prevents the program from running as expected',
    'Function':'A piece of code that you can easily call over and over again',
}
print(programming_dictionary['Bug'])
programming_dictionary['Loop'] = 'The act of doing something over and over again'

for key in programming_dictionary:
    print(programming_dictionary[key])

# Nesting
capitals = {
    'France':'Paris',
    'Germany':'Berling'
}

travel_log = {
    'France':['Paris','Lille','Dijon'],
    'Germany':['Berlin','Hamburg','Stuttgart']
}

students_marks = {
    'Harry':{'Sub-A':10,'Sub-B':20,'Sub-C':30},
    'Sejal':{'Sub-A':10,'Sub-B':20,'Sub-C':30}
}
