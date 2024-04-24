# TODO: create a function BMI
def calcluate_BMI(weight, height):
    return round((weight/(height)**2), 2)


def BMI():
    name = input("Enter your name:")
    weight = float(input("Enter your weight in kgs:"))
    height = float(input("Enter your height in meters:"))
    bmi = calcluate_BMI(weight=weight, height=height)
    print(f"\nName: {name}")
    print(f"Weight:{weight}")
    print(f"Height:{height}")
    if bmi < 18.5:
        print(f"BMI Category: under weight BMI:{bmi}")
    elif bmi >= 18.5 and bmi <= 24.9:
        print(f"BMI Category: Normal weight BMI:{bmi}")
    elif bmi >= 25 and bmi <= 29.9:
        print(f"BMI Category: Over weight BMI:{bmi}")

    else:
        print(f"BMI Category: Obesity BMI:{bmi}")
    print(f"{'-'*34}\n")
