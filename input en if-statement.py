a = int(input("Waarde a? "))
b = int(input("Waarde b? "))

min = b
max = a


if a > b:
    max = a
    print("a is het grootste getal: " + str(max))

elif a < b:
    min = a
    print("a is het kleinste getal: " + str(min))

else:   print("a en b zijn even groot")



print("het minimum is " + str(a) + " het maximum is " + str(b))


