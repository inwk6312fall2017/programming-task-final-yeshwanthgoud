my_file = open('running-config.cfg')

my_dict = {}
list_of_access = []
for line in  my_file:
    words = line.strip()
    words = words.split()
    for word in words:
        if word == "access-list":
            list_of_access.append(words)

