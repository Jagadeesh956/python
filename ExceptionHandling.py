def spam(divisor):
    try:
        return 42/divisor
    except ZeroDivisionError:
      print("Division by zero")
print(spam(2))
print(spam(0))