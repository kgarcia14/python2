meal = {
    "drink": "red wine",
    "appetizer": "salad",
    "entree": "steak",
    "dessert": "ice cream"
}

print(meal)

meal["water"] = "fizzy"
meal ["bread"] = False

print(meal)

if "bread" in meal and "bread" == True:
    print("Kurtis had bread")
else: 
    print("Kurtis did not have bread")