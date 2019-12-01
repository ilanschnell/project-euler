from num2words import num2words

print(sum(sum(c.isalpha() for c in num2words(i)) for i in range(1, 1001)))
