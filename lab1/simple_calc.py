op = input("""Choose from the following operators:
+ addition
- subtraction
* multiplication
/ float division
// integer division
% remainder
op = """)

a = int(input("a = "))
b = int(input("b = "))

if op == '+':
    print("{} + {} = {}".format(a, b, a + b))
elif op == '-':
    print("{} - {} = {}".format(a, b, a - b))
elif op == '*':
    print("{} * {} = {}".format(a, b, a * b))
elif (op == '/' or op == '//' or op == '%') and b == 0:
    print("Error! Division by zero!")
elif op == '/':
    print("{} / {} = {:.2f}".format(a, b, a / b))
elif op == '//':
    print("{} // {} = {}".format(a, b, a // b))
elif op == '%':
    print("{} % {} = {}".format(a, b, a % b))
else:
    print("Wrong operator!")
