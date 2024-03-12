def calcFactorial(n):
    if (n == 0 ):
        return 1
    elif not (1 <= n <= 100):
        return "out of range"
    else:
        result = 1
        for ii in range(1, n+1):
            result *= ii
        return result

num = int(input("Input num: "))
result = calcFactorial(num)
if result == ("out of range"):
    print("out of range")
else:
    print(f"{num} factorial is {result}")
