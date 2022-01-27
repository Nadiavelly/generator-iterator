nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

class FlatIterator():
    my_list = []
    for i in nested_list:
        for k in i:
            my_list.append(k)

    def __init__(self, nested_list):
        self.nested_list = nested_list

    def __iter__(self):
        self.counter = -1
        return iter(self.my_list)

    def __next__(self):
        self.counter += 1
        if self.counter == len(self.my_list):
            raise StopIteration
        return


for item in FlatIterator(nested_list):
    print(item)
    print(type(item))

print("-"*50)
flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)




