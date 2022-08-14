# 1. Write a Python-script that displays the message “Hello world”.
print('Hello, world!', '\n')

# 2. Rewrite the first script to display three any messages.
print('Hello,', end=' ')
print('Pyton!')
print('I\'m begginer!', '\n')

# 3. Write a Python-script to reads values for the length and width of a rectangle and returns the area of the rectangle.
print("3. Input two sides of rectangle:")
a = int(input('Input a: '))
b = int(input('Input b: '))

print('S = ', a*b, '\n')

# 4. Write a program that requests the user to enter two numbers and prints the sum, product, difference and quotient of the two numbers.
print("4. Input two numbers: ")
a = int(input('Input a: '))
b = int(input('Input b: '))

print('Result:\n', "a + b =", a+b, '\n', "a - b =", a-b, '\n',
      "a * b =", a*b, '\n', "a / b =", a/b, '\n', sep=None)

# 5. Write a program that reads in the radius of a circle and prints the circle’s diameter, circumference and area. Use the constant value 3.14159 for π. Do these calculations in output statements.
r = int(input("5. Input r: "))
pi = 3.14159

print(" d =", r*2, '\n', "C =", 2*pi*r,
      '\n', "S =", pi*r**2, sep=None, end="")
