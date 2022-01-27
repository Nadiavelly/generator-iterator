nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]


def my_generator(nested_list):
    my_list = []
    for i in nested_list:
        for k in i:
            my_list.append(k)
    counter = 0
    while counter < len(my_list):
        yield my_list[counter]
        counter += 1


for item in my_generator(nested_list):
    print(item)
