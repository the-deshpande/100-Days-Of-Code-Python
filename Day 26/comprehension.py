import random

name = 'Angela'

new_list = [n for n in name]

print(new_list)


names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
scores = {name: random.randint(1, 100) for name in names}
print(scores)

passed_students = {name: score for name,score in scores.items() if score> 50}
print(passed_students)
