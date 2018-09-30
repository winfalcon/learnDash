def spam(div):
    try:
        return 42/div
    except ZeroDivisionError:
        print('ERROR: invalid agrument')

print(spam(2))
print(spam(0))
