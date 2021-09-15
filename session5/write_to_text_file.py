# modes
# 'r': read
# 'w': write - overwrite
# 'a': append

with open('people.txt', 'w') as text_file_handle:
    data = 'Jessica\nSusan\nTrisha'
    text_file_handle.write(data)


