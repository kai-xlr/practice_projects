apple_quantity = 23
apple_price = 1.49
apple_review = int((823 + 52) / 10)
apple_location = 'F'
day = 7
price_apple = round((apple_price * .9), 2)

day += 3

if (day % 7 == 3 or apple_quantity < 10):
    print(f"Sale on apples today, today only they are: ${price_apple}")
print(f"An apple costs: ${apple_price}, there are {apple_quantity} in inventory found in section: {apple_location} and your customers gave it an average review of {apple_review}%!")