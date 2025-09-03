"""
Authors: Deepesh K, Dhaiwat K
Creation date: 09/03/2025
Countinput
"""

def countchars(st):
    if not st:  # Edge case: empty input
        return 0

    exclude = {' ', '.', '!', ','}
    return sum(1 for ch in st if ch not in exclude)

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    result = countchars(user_input)
    print(result)