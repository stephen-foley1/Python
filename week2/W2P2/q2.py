a = [10,20,30,20,10,50,60,40,80,50,40]
b = []

for item in a:
    if item not in b:
        b.append(item)

print("The New list is : ")
print(b)

if len(a) == 0:
    print("The list is empty")
else:
    print("The list is not empty")
