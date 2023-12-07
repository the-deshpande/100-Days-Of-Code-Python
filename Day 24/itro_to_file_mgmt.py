with open('my_text_file.txt') as file:
    content = file.read()
    print(content)

with open('my_text_file.txt', 'a') as file:
    file.write('new text right here.')

with open('my_text_file.txt') as file:
    content = file.read()
    print(content)