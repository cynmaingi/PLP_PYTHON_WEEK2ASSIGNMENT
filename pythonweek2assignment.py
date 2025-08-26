# Start with an empty list
my_list = []

# Add some numbers to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Put 15 in the second position (between 10 and 20)
my_list.insert(1, 15)

# Add more numbers at the end of the list
my_list.extend([50, 60, 70])

# Remove the last number (70)
my_list.pop()

# Arrange the list from smallest to biggest
my_list.sort()

# Find where number 30 is in the list
position = my_list.index(30)
print("30 is found at position:", position)
