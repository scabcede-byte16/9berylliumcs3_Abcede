year = int(input("Enter a year that is greater than or equal to 1900: "))
if year < 1900:
        print("Invalid, please enter a year that is greater than or equal to 1900.")
        exit()
zoediecs = ["Rat (鼠 / Shǔ)", "Ox (牛 / Niú)", "Tiger (虎 / Hǔ)", "Rabbit (兔 / Tù)", "Dragon (龙 / Lóng)", "Snake (蛇 / Shé)", "Horse (马 / Mǎ)", "Goat (羊 / Yáng)", "Monkey (猴 / Hóu)", "Rooster (鸡 / Jī)", "Dog (狗 / Gǒu)", "Pig (猪 / Zhū)"]
hi = (year - 1900) % 12
print(f"The zodiac sign for the year {year} is: {zoediecs[hi]}")
