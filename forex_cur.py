from forex_python.converter import CurrencyRates, CurrencyCodes

c = CurrencyRates()

print(c.get_rate('USD','INR'))
print(c.convert('USD','INR',20))

curr = CurrencyCodes()
print(curr.get_symbol('INR'))
print(curr.get_currency_name('INR'))