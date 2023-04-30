def calc_tax(amount, tax_rate):
    """the functions return amount of income tax"""

    if not (isinstance(amount, (float, int))):
        raise TypeError("amount  must be a number")

    if not ( isinstance(tax_rate, (float, int))):
        raise TypeError(" tax rate must be a number")

    if amount < 0 :
        raise ValueError("amount and must be greater than 0")

    if not 0 < tax_rate < 1:
        raise ValueError("tax rate must be between 0 and 1")

    return amount * tax_rate