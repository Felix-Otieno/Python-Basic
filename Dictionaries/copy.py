dict1 = {'Jessa': 70, 'Emma': 55}

# Copy dictionary using copy() method
dict2 = dict1.copy()
# printing the new  dictionary
print(dict2)
# output {'Jessa': 70, 'Emma': 55}

# Copy dictionary using dict() constructor
dict3 = dict(dict1)
print(dict3)
# output {'Jessa': 70, 'Emma': 55}

# Copy dictionary using the output of items() methods
dict4 = dict(dict1.items())
print(dict4)
# output {'Jessa': 70, 'Emma': 55}