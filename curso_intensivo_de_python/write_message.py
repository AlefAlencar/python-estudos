filename = 'programming.txt'

'''with open(filename, 'w') as file_object:  # 'w' = modo de escrita.
    file_object.write("I love programming.\n")
'''  # cria o arquivo automaticamente, se não existir.
with open(filename, 'a') as file_object:  # 'a' = modo de concatenação
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
