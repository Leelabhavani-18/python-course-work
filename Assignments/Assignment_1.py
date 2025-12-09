data = {
    'App ID': 303,
    'App name': 'Instagram',
    'Version': '315.1.0',
    'Price': 0.00,
    'Discount': 0.00,
    'Categories': ['Social Media', 'Photos', 'Videos'],
    'Downloads and Users': (5000000000, 2500000000),
    'Features': ('Reels', 'Stories', 'Messaging', 'Live', 'Photo Sharing'),

    'Developer_details': {
        'Developer_name': 'Meta Platforms, Inc.',
        'Contact': 'support@instagram.com',
        'Location': 'Menlo Park, California, USA'
    }
}

print("\nSample Instagram Data:\n")

for key, value in data.items():
    if key == 'Developer_details':
        for k1, v1 in value.items():
            print(f"{k1}: {v1}")
    print(f"{key}: {value}")

print('\n' * 2)

# Inputs
id = int(input("Enter the App ID: "))
name = input("Enter Name of the App: ")
version = input("Enter the version of the App: ")
price = float(input("Enter Subscription cost (if not, enter 0): "))
discount = float(input("Enter discount percent: "))
cat = list(map(str.strip, input("Enter the App categories (comma-separated): ").split(',')))
users = tuple(map(str.strip, input("Enter Downloads and Users (space-separated): ").split()))
features = set(map(str.strip, input("Enter the features (comma-separated): ").split(',')))

developer_details = {
    'Developer_name': input("Enter developer name: "),
    'Contact': input("Enter developer contact: "),
    'Location': input("Enter developer location: ")
}

print('\n' * 2)

print("App ID:", id)
print("Name:", name)
print("Price of Subscription:", price)
print("Discount for subscription: %.2f" % discount)
print("App Version: %s" % version)

print(f'Categories: {", ".join(cat)}')
print(f'Downloads: {users[0]}')
print(f'Users: {users[0]}')
print("Features: {}".format(', '.join(features)))

for key, value in developer_details.items():
    print(f"{key}: {value}")

