details = {
    "name": "John",
    "age": 25,
    "occupation": "secretary",
    "hobby": "politics",
    "tribe": "kisii"
}

print(details.keys())
print(details.values())
print(details.items())

print(type(details.keys()))
print(type(details.values()))
print(type(details.items()))


for key, value in details.items():
  print(f"{key}: {value}")