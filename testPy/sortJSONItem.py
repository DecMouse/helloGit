import json

order_data = {
    "order_id": "12345",
    "customer_name": "John Doe",
    "items": [
         {
            "item_id": "003",
            "item_name": "Keyboard",
            "quantity": 1,
            "price": 49.99
        },
        {
            "item_id": "001",
            "item_name": "Laptop",
            "quantity": 1,
            "price": 999.99
        },
        {
            "item_id": "002",
            "item_name": "Mouse",
            "quantity": 2,
            "price": 25.50
        }
       
    ],
    "total_amount": 1100.98
}

print(order_data)
def sort_items_by_id(order_data):
    order_data['items'] = sorted(order_data['items'], key=lambda x: x['item_id'])

def sort_items_by_name(order_data):
    order_data['items'] = sorted(order_data['items'], key=lambda x: x['item_name'].lower())

# sort_items_by_id(order_data)
sort_items_by_name(order_data)
print(json.dumps(order_data, indent=4))
