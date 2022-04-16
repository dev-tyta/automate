# Sandwich Maker

import pyinputplus as pyip

bread_choice = ["Wheat", "White", "Sourdough"]
bread_type = pyip.inputMenu(choices=bread_choice, prompt="Pick Bread Choice")

protein_choice = ["Chicken", "Turkey", "Ham", "Tofu"]
protein_type = pyip.inputMenu(protein_choice, prompt="What type of protein would you like?")

cheese = pyip.inputYesNo("DO you want Cheese?")
if cheese.lower() == "yes":
    cheese_choice = ["Cheddar", "Swiss", "Mozzarella"]
    cheese_type = pyip.inputMenu(choices=cheese_choice, prompt="How would you love the cheese?")

ma_let = pyip.inputYesNo("Would you love: Mayo, Mustard, Lettuce or Tomato?")
if ma_let.lower() == "yes":
    ma_let_choice = ["Mayo", "Mustard", "Lettuce", "Tomato"]
    ma_let_type = pyip.inputMenu(choices=ma_let_choice, prompt="Which would you love?")

num_pizza = pyip.inputInt("How many Pizza(s) would you like? ")

# total_cost
