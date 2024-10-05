#assignment operators
sum = 7
sum+=6
print(sum)

#given that your have two products a laptop and a mouse such that the price of the laptop is 300000 
#  and the price of the mouse is 50000, use a for loop to find the total sum of the products.
laptop_price=300000
mouse_price=50000
sum = 0
product_prices = [laptop_price,mouse_price,7000]
for price in product_prices:
    sum+=price
print(f"the total sum of the product is: {sum:,}") 

