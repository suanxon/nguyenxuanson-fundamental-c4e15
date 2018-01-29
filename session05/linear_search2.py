nums = [7, 5, 10, 8, 200, 30]
num_to_find = int(input("Enter a number:"))

#1. Assumption/ Gia dinh ket qua:
found_index = -1

#2. Create a loop to test our assumption:
for index, num in enumerate(nums):
    if num == num_to_find:
        foun_index = index  # Update assumption
        break

if found_index == -1:
    print("Not found")
else:
    print("Found at index", found_index)
