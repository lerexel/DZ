import colorama
import inspect
colorama.init()

attributes = dir(colorama)
methods = [attr for attr in attributes if callable(getattr(colorama, attr))]
non_methods = [attr for attr in attributes if not callable(getattr(colorama, attr))]

print("Всі атрибути колорами:")
print(attributes)

print("\nМетоди:")
print(methods)

print("\nАтрибути (не методи):")
print(non_methods)

print("\nОпис методів та атрибутів:")
for method in methods[:5]:
    print(f"\nМетод: {method}")
    print(inspect.getdoc(getattr(colorama, method)))

colorama.deinit()

