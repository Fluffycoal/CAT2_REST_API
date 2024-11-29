import requests

API_URL = 'http://127.0.0.1:8000/products/'

def add_product(name, description, price):
    product_data = {
        'name': name,
        'description': description,
        'price': price
    }
    response = requests.post(API_URL, json=product_data)
    if response.status_code == 201:
        print("Product added:", response.json())
    else:
        print("Failed to add product:", response.json())

def get_products():
    response = requests.get(API_URL)
    if response.status_code == 200:
        print("Products list:", response.json())
    else:
        print("Failed to retrieve products:", response.json())

if __name__ == '__main__':
    # Add some products
    add_product("Laptop", "A high performance laptop", 999.99)
    add_product("Mouse", "Wireless mouse", 25.50)

    # Retrieve and print all products
    get_products()