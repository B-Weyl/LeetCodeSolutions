a = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
new_list = []
for item in a:
    new_list.append(item[::-1])

new_new_list = []
for thing in new_list:
    for value in thing:
        new_new_list.append(1 if value == 0 else 0)

print(new_new_list)
