# Hardcoded dictionary of stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 320,
    "GOOGL": 140,
    "AMZN": 130
}

portfolio = {}
total_value = 0

print("Welcome to the Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))

# User inputs stock names and quantities
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Invalid symbol. Please choose from:", ", ".join(stock_prices.keys()))
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Calculate total investment value
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    value = qty * stock_prices[stock]
    total_value += value
    print(f"{stock}: {qty} shares -> Value = ${value}")

print("\nTotal Investment Value = $", total_value)

#Optional: Save results to a file
save = input("Do you want to save this portfolio to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio.txt", "w") as f:
        f.write("Stock Portfolio Summary\n")
        for stock, qty in portfolio.items():
            f.write(f"{stock}: {qty} shares ->Value = ${qty * stock_prices[stock]}\n")
        f.write(f"\nTotal Investment Value = ${total_value}\n")
    print("Portfolio saved to portfolio.txt")
