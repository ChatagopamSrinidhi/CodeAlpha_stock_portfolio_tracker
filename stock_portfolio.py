# Step 1: Define stock prices (dictionary)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 320
}

# Step 2: Display stock list
print("Available stocks and prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

# Step 3: Take user input
total_investment = 0
portfolio = {}

while True:
    stock_name = input("\nEnter stock symbol (or 'done' to finish): ").upper()
    if stock_name == "DONE":
        break
    if stock_name not in stock_prices:
        print("Invalid stock symbol. Try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
        investment = stock_prices[stock_name] * quantity
        portfolio[stock_name] = portfolio.get(stock_name, 0) + investment
        total_investment += investment
    except ValueError:
        print("Please enter a valid number for quantity.")

# Step 4: Display total investment
print("\nYour Portfolio Summary:")
for stock, amount in portfolio.items():
    print(f"{stock}: ${amount}")
print(f"\nTotal investment value: ${total_investment}")

# Step 5: Optionally save to file
save_option = input("\nSave the result to a file? (y/n): ").lower()
if save_option == "y":
    with open("stock_portfolio.txt", "w") as f:
        for stock, amount in portfolio.items():
            f.write(f"{stock}: ${amount}\n")
        f.write(f"\nTotal investment value: ${total_investment}\n")
    print("Saved to stock_portfolio.txt successfully!")

