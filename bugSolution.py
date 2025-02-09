def function(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return a + b
    else:
        try:
            a = int(a)
            b = int(b)
            return a + b
        except ValueError:
            return "TypeError: Unsupported operand types for +" 

result = function(5, '10')
print(result)
result2 = function(5, 10)
print(result2)
result3 = function('5', '10')
print(result3)
result4 = function('hello', 10)
print(result4)