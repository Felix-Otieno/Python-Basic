dictionary = {
    "name": "John",
    "age": 25,
    "occupation": "secretary",
    "hobby": "politics",
    "tribe": "kisii",
    "telephone": 1178, 
    "weight": 50, 
    "height": 6
}

print(dictionary.pop("height"))
print(dictionary)

del dictionary["age"]
print(dictionary)

dictionary.clear()
print(dictionary)
