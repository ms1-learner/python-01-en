def convert():
    temp = int(input("Please enter the temperature degree:"))
    unit = input("Please enter f for Fahrenheit and c for Celsius: ")

    if unit == "f":
        temp = (temp - 32) * 5 / 9

    elif unit == "c":
        temp = (temp * 9 / 5) + 32

    return temp
