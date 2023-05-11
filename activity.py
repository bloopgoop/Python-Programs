rain = input("Is it raining?: ").upper()
temp = float(input("What is the temperature?: "))

if rain == "NO":
    if temp >= 80:
        print("Beach volleyball")
    elif temp < 32:
        print("Ice Fishing")
    else:
        print("Running")

if rain == "YES":
    if temp >= 80:
        print("Movie")
    elif temp < 32:
        print("Skiing")
    else:
        print("Racquetball")
