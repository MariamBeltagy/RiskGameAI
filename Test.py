list = [1, 2, 3]
list2 = [1, 3, 2]

for x in list:
    for y in list2:
        if (x == y):
            list2.remove(x)
            continue
list.extend(list2)
print(list)
