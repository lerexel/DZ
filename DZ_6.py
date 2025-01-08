result = []

def divider(a, b):
    if a < b:
        raise ValueError(f"ValueError: a={a} < b={b}")
    if b > 100:
        raise IndexError(f"IndexError: b={b} > 100")
    return a / b

data = {11: 2, 2: 5, "521488": 101, 74: 0, (1,12): 82, 52: 61}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except Exception as e:
        print(f"Появилася ошибка ключа={key}, значеніє={data[key]}: {e}")

print(result)

