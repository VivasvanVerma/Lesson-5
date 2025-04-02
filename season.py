temp = int(input("Enter the temperature in Celcius: "))
humidity = int(input("Enter humidity percentage: "))
if temp>=30:
    if humidity<=50 and humidity>=30:
        print("It is likely summer.")
elif temp<30 and temp>=25:
    if humidity>50:
        print("It is likely Monsoon")
elif temp<25:
    if humidity<30:
        print("It is likely Winter")