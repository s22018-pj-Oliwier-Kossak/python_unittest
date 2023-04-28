amount = -1000
tax_rate = -0.15

assert amount >=0, 'amount should not be negative'
assert tax_rate >= 0 and tax_rate < 1, 'tax rate should be between 0 and 1'
