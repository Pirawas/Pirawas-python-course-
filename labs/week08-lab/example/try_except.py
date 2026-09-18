try:
    Num1 = int(input("Enter a first Number: "))
    Num2 = int(input("Enter a second Number: "))
    signal = input("Enter signal: ")
    result = 0

    if signal == "+":
        result = Num1 + Num2
    elif signal == "-":
        result = Num1 - Num2
    elif signal == "*":
        result = Num1 * Num2
    elif signal == "/":
        result = Num1 / Num2
    else:
        raise ValueError
        print("Can Enter only signal + - * /")
        
    print(f"{Num1} {signal} {Num2} = {result}")

except ValueError:
    print("Can enter only Number")
except ZeroDivisionError:
    print("Can not Division by 0")
finally:
    print("End")