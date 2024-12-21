result = []

def divider(a, b):
    if a < b:
        raise ValueError("A менше за b")
    if b > 100:
        raise IndexError("B більше 100")
    return a / b

# Виправлений словник
data = {10: 2, 2: 5, "123": 4, 18: 0, (): 15, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except (ValueError, IndexError, ZeroDivisionError, TypeError) as e:
        print(f"Виняток: {e}")

print(result)
