my_file = open('running-config.cfg')

my_dict = {}
list_of_access = []
for line in  my_file:
    words = line.strip()
    words = words.split()
    for word in words:
        if word == "access-list":
            list_of_access.append(words)

for index in range(len(list_of_access)):
    my_dict[tuple(list_of_access[index][2:])] = list_of_access[index]

print (my_dict)


