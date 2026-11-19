# Shopping list with price estimates (US-based example)
shopping_list = {
    "Milk (1L)": 1.50,
    "Bread (loaf)": 2.00,
    "Eggs (dozen)": 2.50,
    "Apples (1kg)": 3.00,
    "Rice (5kg)": 5.00,
    "Butter (250g)": 3.50,
    "Cheese (200g)": 4.00,
    "Bananas (1kg)": 2.50,
    "Chicken (1kg)": 6.00,
    "Yogurt (500g)": 2.75
}

# Calculate total
total_cost = sum(shopping_list.values())

print("=== SHOPPING LIST ===")
for item, price in shopping_list.items():
    print(f"{item}: ${price:.2f}")

print(f"\nTotal Estimated Cost: ${total_cost:.2f}")