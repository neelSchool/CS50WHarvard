import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except:
       print("Error invalid input.")
       sys.exit(1)

try:
    result = x / y
except:
      print("Error: It is not possible to divide by 0")
      sys.exit(1)

print(f"{x} / {y} = {result}")
