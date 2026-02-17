a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a > b and a > c:
    print("Largest is", a)
elif b > c:
    print("Largest is", b)
else:
    print("Largest is", c)
