"""
Authors: Deepesh K, Dhaiwat K
Creation date: 09/03/2025
Heating cooling
"""

def temp_checker():
    heating_days = 0
    cooling_days = 0

    while True:
        try:
            temp = int(input("Enter the average daily temperature: "))
        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue

        if temp < -459:
            break

        if temp < 60:
            heating_days += 1
        elif temp > 80:
            cooling_days += 1

    print(f"Heating days: {heating_days}")
    print(f"Cooling days: {cooling_days}")


if __name__ == "__main__":
    temp_checker()