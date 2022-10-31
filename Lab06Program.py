def numbers(x, y, operand):
    if operand == "+":
        return x + y
    elif operand == "-":
        return x - y

x = float(input())
y = float(input())
operand = str(input())
print(numbers(x, y, operand))