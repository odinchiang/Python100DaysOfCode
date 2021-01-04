piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

# [start_index : stop_index(not include) : step]

print(piano_keys[2:5])  # ['c', 'd', 'e']
print(piano_tuple[2:5])  # ('mi', 'fa', 'so')

print(piano_keys[2:])  # ['c', 'd', 'e', 'f', 'g']
print(piano_keys[:5])  # ['a', 'b', 'c', 'd', 'e']
print(piano_keys[2:5:2])  # ['c', 'e']
print(piano_keys[::2])  # ['a', 'c', 'e', 'g']

# [::-1] 相當於倒序
print(piano_keys[::-1])  # ['g', 'f', 'e', 'd', 'c', 'b', 'a']



