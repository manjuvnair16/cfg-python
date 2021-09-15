
new_todo_item = input('Enter your todo item: ')

with open('todo.txt', 'a') as text_file_handle:
    text_file_handle.write(new_todo_item+ '\n')