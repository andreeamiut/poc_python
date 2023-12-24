menus = {
    'Breakfast' : ['Egg sandwich', 'Bagel', 'Coffee'],
    'Lunch': ['BLT', 'PB&J', 'Turkey Sandwich'],
    'Dinner': ['Soup', 'Salad', 'Spaghetti', 'Taco']
}

for item in menus:
    print(item)

for name, menu in menus.items():
    print(name, ":", menu)