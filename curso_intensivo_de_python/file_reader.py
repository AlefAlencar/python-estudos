filename = 'pi_digits.txt'
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

with open(filename) as file_object:
    for line in file_object:
        print(line, end='')

# preserva o conteúdo para fora do bloco 'with'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
