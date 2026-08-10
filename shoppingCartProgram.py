#shopping cart program

def calculate_total (prices):
    sum = 0
    for i in prices:
        sum += i
    return sum

cart = []
prices = []

is_continue = True
print("---Shopping Cart Program---")
print("Start Entering Products now...")
while is_continue:
    item = input("Enter a Product (e to exit): ")
    if (item == "e" or item == "E"):
        is_continue = False
    else:
        price = int(input(f"Enter the price of {item}: P"))
        cart.append(item)
        prices.append(price)
        print()

print("\n---Cart---")
if cart:
    total = calculate_total(prices)
    n = 0
    for i in cart:
        print(f"{n + 1}. {i} - P{prices[n]}")
        n += 1
    print(f"The total price is P{total}")
else:
    print("\n---Cart is Empty---")
    print("Thank you for purchasing")
close = input()