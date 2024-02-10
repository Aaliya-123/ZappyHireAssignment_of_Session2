my_list = [1, "hello", 3.14, True, [1, 2, 3]]
result = {}
for item in my_list:
    item_type = type(item)
    if item_type not in result:
        result[item_type] = []
    result[item_type].append(item)
print(result)
