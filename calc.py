def discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        discounted_price = price - discount
        return discounted_price
    else:
        return price

price = float(input("Enter the price: "))
discount_percent = float(input("Enter the discount percentage: "))

discounted_price = discount(price, discount_percent)
print(f"The discounted price is: {discounted_price}")