from sys import argv

print("Total argument passed :", len(argv))
print(type(argv))

print("All command line inputs")
for value in argv:
    print(value)

    print('Argument one:')
print('Argument Two:')
add = int(argv[1]) + int(argv[2])
print('Addition is:', add)
