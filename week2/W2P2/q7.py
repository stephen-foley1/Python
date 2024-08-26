a = [2023, "setu", "Carlow"]
b = ["kilkenny road", "Co Carlow"]


a.extend(b)
a.insert(1, "R93 V960")

last_item = a.pop()

print("Removed item:", last_item)

setu_index = a.index("setu")


setu_count = a.count("setu")

c = a.copy()


print("Modified list a:", a)


print("Index of 'setu':", setu_index)


print("Count of 'setu' in list a:", setu_count)


print("Copy of list a (c):", c)
