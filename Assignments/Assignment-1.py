print("----- Enter Myntra Product Details -----\n")

# Basic Product Details
product_id = int(input("Enter Product ID: "))
brand_name = input("Enter Brand Name: ")
product_name = input("Enter Product Name: ")
price = float(input("Enter Price (₹): "))

# Categories (List)
categories_input = input("Enter Categories (comma-separated): ")
categories = [c.strip() for c in categories_input.split(",")]

# Sizes (List)
sizes_input = input("Enter Available Sizes (comma-separated): ")
available_sizes = [s.strip().upper() for s in sizes_input.split(",")]

# Stock (Tuple)
available_stock = int(input("Enter Available Stock: "))
sold_stock = int(input("Enter Sold Stock: "))
stock_details = (available_stock, sold_stock)

# Discount (Float)
discount_percentage = float(input("Enter Discount Percentage (%): "))

# Product Features (Set)
features_input = input("Enter Key Features (comma-separated): ")
product_features = set(f.strip() for f in features_input.split(","))

# Seller Details (Dictionary)
seller_name = input("Enter Seller/Store Name: ")
seller_rating = float(input("Enter Seller Rating (out of 5): "))
seller_location = input("Enter Seller Location: ")

seller_details = {
    "name": seller_name,
    "rating": seller_rating,
    "location": seller_location
}

# Price After Discount
final_price = price - (price * discount_percentage / 100)
