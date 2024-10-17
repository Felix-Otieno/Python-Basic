dict1 = {'Jessa': 70, 'Arul': 80, 'Emma': 55}
dict2 = {'Kelly': 68, 'Harry': 50, 'Emma': 66}

# join two dictionaries with some common items
dict1.update(dict2)
# printing the updated dictionary
print(dict1['Emma'])
# Output 66