list_of_dicts =  [{'make': ' Google ', 'model': 216, 'color': 'Black'}, {'make': 'MiMax', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# highest model number?

print(list_of_dicts[0]['model'])
sorted_list = sorted(list_of_dicts, key=lambda item: int(item['model']), reverse=True)
print(sorted_list)