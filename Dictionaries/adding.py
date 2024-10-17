details = {
    "name":"Kavarenge",
    "age":35,
    "status":"married",
    "occupation":"engineer",
    "country":"Kenya"
}

details["hobby"] = "watching football"
details["age"] = 49

print(details)

for keys, values in details.items():
    print(f"{keys}: {values}")

