# Sandwich Maker
import time
import pyinputplus as pyip

bread_choice = ["Wheat", "White", "Sourdough"]
bread_type = pyip.inputMenu(choices=bread_choice, prompt="Pick Bread Choice\n")

protein_choice = ["Chicken", "Turkey", "Ham", "Tofu"]
protein_type = pyip.inputMenu(protein_choice, prompt="What type of protein would you like?\n")

cheese = pyip.inputYesNo("Do you want Cheese?\n")
if cheese.lower() == "yes":
    cheese_choice = ["Cheddar", "Swiss", "Mozzarella"]
    cheese_type = pyip.inputMenu(choices=cheese_choice, prompt="How would you love the cheese?\n")
else:
    cheese_type = "None"
ma_let = pyip.inputYesNo("Would you love: Mayo, Mustard, Lettuce or Tomato?\n")
if ma_let.lower() == "yes":
    ma_let_choice = ["Mayo", "Mustard", "Lettuce", "Tomato"]
    ma_let_type = pyip.inputMenu(choices=ma_let_choice, prompt="Which would you love?\n")
else:
    ma_let_type = "None"
num_pizza = pyip.inputInt("How many Pizza(s) would you like?\n")
print("Order recorded:")

# total_cost
cost = {"Wheat": 0.5, "White": 0.5, "Sourdough": 0.5, "Chicken": 1.0, "Turkey": 1.0, "Ham": 0.7, "Tofu": 0.5,
        "Cheddar": 0.2, "Swiss": 0.2, "Mozzarella": 0.2, "Mayo": 0.1, "Mustard": 0.1, "Lettuce": 0.1, "Tomato": 0.1,
        "None": 0}

total_cost = (cost.get(bread_type) + cost.get(protein_type) + cost.get(cheese_type)+ cost.get(ma_let_type)) * num_pizza


time.sleep(5)

print(f"Total Cost of pizza = ${total_cost}")
