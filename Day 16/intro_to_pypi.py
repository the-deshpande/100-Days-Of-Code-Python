from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemon Name',['Pikachu','Charmander'])
table.add_column('Pokemon Types',['Electric','Fire'])
table.add_row(['Squirtle','Water'])

table.align = 'l'

print(table)