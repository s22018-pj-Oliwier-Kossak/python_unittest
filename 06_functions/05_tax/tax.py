def calc_tax(amount, tax_rate, age):
    if not isinstance(amount, (float, int)):
        raise TypeError("amount must be a number")
    if not amount >= 0:
        raise ValueError("the amount value must be greater than 0")

    if not isinstance(tax_rate, (float, int)):
        raise TypeError("tax_rate must be a number")
    if not 0 < tax_rate < 1:
        raise ValueError("tax rate must be beetwen 0 and 1")

    if not isinstance(age, (float, int)):
        raise TypeError("age must be a number")
    if not age > 0:
        raise ValueError("the age value must be greater than 0")

    if age <= 18:
        return int(min(amount + tax_rate, 5000))
    elif age <= 65:
        return int(amount * tax_rate)
    else:
        return int(min(amount + tax_rate, 8000))

