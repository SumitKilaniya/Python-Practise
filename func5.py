def discount_price(original_price,discount_percent):
    discount_amount=(discount_percent/100)*original_price
    final_amount=original_price-discount_amount
    print(f"final_amount is {final_amount}")

o=int(input("enter original price: "))
d=int(input("discount percent: "))
discount_price(o,d)