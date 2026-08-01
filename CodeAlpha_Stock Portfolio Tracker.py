# Predefined stock prices
stock_prices = {
    "AAPL": 160,
    "TSLA": 250,
    "GOOGLE": 180,
    "AMZN": 140,
    "MSFT": 300
}

total_investment = 0

print("=== Stock Portfolio Tracker ===")

# Number of stocks
n = int(input("Enter number of stocks: "))

# File to save results
file = open("portfolio.txt", "w")

for i in range(n):

    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:

        price = stock_prices[stock_name]
        investment = price * quantity
        total_investment += investment

        print(stock_name, "Investment Value =", investment)

        file.write(f"{stock_name} - Quantity: {quantity}, Value: {investment}\n")

    else:
        print("Stock not found!")

# Display total investment
print("\nTotal Investment Value =", total_investment)

file.write(f"\nTotal Investment Value = {total_investment}")

file.close()

print("Portfolio details saved in portfolio.txt")
