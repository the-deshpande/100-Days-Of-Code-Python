letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

print(letters)

print(letters[0]) #Indexing maintained in lists and begins with 0

letters[1] = 'bee'
print(letters)

letters.append('aa')
print(letters)

letters.extend(['ab','ac','ad'])
print(letters)

dirty_dozen = ['Strawberries','Spinach','Kale','Nectarines','Apples','Grapes','Peaches','Cherries','Pears','Tomatoes','Celery','Potatoes']

fruits = ['Strawberries','Nectarines','Apples','Grapes','Peaches','Cherries','Pears']
vegetables = ['Spinach','Kale','Tomatoes','Celery','Potatoes']
dirty_dozens = [fruits,vegetables]
print(dirty_dozens)

