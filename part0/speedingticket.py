"""
Authors: Deepesh K, Dhaiwat K
Creation date: 09/03/2025
Speeding Ticket
"""

def calculate_ticket(sl, ds):
    #0 speed
    #20 over
    #50 over
    #negetive speed
    if ds <= 0 or sl <= 0:
        return "Please give a positive speed"
    elif (sl - ds) >= 10:
        return 50
    elif (ds - sl) >= 6 and (ds - sl) <= 20:
        return 75
    elif (ds - sl) >= 21 and (ds - sl) <= 40:
        return 150
    elif (ds - sl) >= 41:
        return 300
    else:
        return 0

def main():
    sl = int(input("Enter Speed limit: "))
    ds = int(input("Enter Driving speed: "))
    result = calculate_ticket(sl, ds)
    print(result)

# Test cases
print("Test case (40, 50):", calculate_ticket(40,50))
print("Test case (60, 65):", calculate_ticket(60, 65))
print("Test case (50, 100):", calculate_ticket(50, 100))
print("Test case (0, 30):", calculate_ticket(0, 30))

if __name__ == "__main__":
    main()