import collections

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4, 'e': 5}

chainmap = collections.ChainMap(dict1, dict2)
print(chainmap) # ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4, 'e': 5})
print(chainmap['a'], chainmap['e']) # 1 5
print(chainmap.maps) # [{'a': 1, 'b': 2}, {'c': 3, 'd': 4, 'e': 5}]

chainmap2 = chainmap.new_child({'f': 6})
print(chainmap2.maps) # [{'f': 6}, {'a': 1, 'b': 2}, {'c': 3, 'd': 4, 'e': 5}]
print(chainmap2.parents) # ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4, 'e': 5})

chainmap3 = chainmap2.new_child({'f': 7})
print(chainmap3.maps) # [{'f': 7}, {'a': 1, 'b': 2}, {'c': 3, 'd': 4, 'e': 5}]
print(chainmap3.parents) # ChainMap({'f': 6}, {'a': 1, 'b': 2}, {'c': 3, 'd': 4, 'e': 5})
print(chainmap3.pop('f')) # 7
print(chainmap3.maps) # [{}, {'f': 6}, {'a': 1, 'b': 2}, {'c': 3, 'd': 4, 'e': 5}]
