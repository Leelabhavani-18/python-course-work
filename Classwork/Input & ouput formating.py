# -------------------------------
#  Basic Input Examples
# -------------------------------

# String input
name = input("Enter the name: ")
print("Name:", name)

# Integer input
age = int(input("Enter the age: "))
print("Age:", age)

# Float input
discount = float(input("Enter the discount: "))
print("Discount:", discount)

# Multiple strings input (as a single string)
names = input("Enter multiple names: ")
print("Names:", names)

# Multiple strings → list
names = input("Enter multiple names: ").split()
print("Names list:", names)

# Multiple integers using map()
nums = list(map(int, input("Enter integer values: ").split()))
print("Integer list:", nums)

# Multiple floats using map()
nums_float = list(map(float, input("Enter float values: ").split()))
print("Float list:", nums_float)

# Tuple of strings
names_tup = tuple(input("Enter names: ").split())
print("Tuple of names:", names_tup)

# Tuple of integers
nums_tup = tuple(map(int, input("Enter integers: ").split()))
print("Tuple of integers:", nums_tup)

# Set of integers
nums_set = set(map(int, input("Enter integers for set: ").split()))
print("Set of integers:", nums_set)

# Using eval() for list/dict/string inputs
d = eval(input("Enter a dict/list/string using eval: "))
print("Output from eval:", d)

# Taking two inputs (name & email)
name, email = input("Enter name and email: ").split()
print("Name:", name)
print("Email:", email)

# Taking two integers
a, b = list(map(int, input("Enter two integers: ").split()))
print("a:", a)
print("b:", b)

# -------------------------------
#  Printing Examples
# -------------------------------
a, b, c = 10, 23.4, "string"

# Basic print
print("a=", a, "b=", b, "c=", c)

# Newline and tab
print(f"a={a}\nb={b}\nc={c}")
print(f"a={a}\tb={b}\tc={c}")

# % formatting
print('a=%d\nb=%f\nc=%s' % (a, b, c))
print('a=%d\nb=%.2f\nc=%s' % (a, b, c))

# .format() method
print('a={}\tb={}\tc={}'.format(a, b, c))
print('a={2}\tb={1}\tc={0}'.format(a, b, c))