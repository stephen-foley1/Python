a = [789, -4, 10, 20, 30, 50, 60, 80, 23]

# Initialize variables to store the minimum and maximum values
min_num = a[0]
max_num = a[0]

# Iterate through the list to find the minimum and maximum values
for num in a:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num

# Print the results
print("Smallest number:", min_num)
print("Largest number:", max_num)
