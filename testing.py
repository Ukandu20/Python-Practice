class Pizza:
    def __init__(self, name, price, toppings):
        self.name = name
        self.price = price
        self.toppings = toppings

class Order:
    def __init__(self):
        self.pizzas = []
        self.total_price = 0

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)
        self.total_price += pizza.price

    def print_order(self):
        print("Order:")
        for pizza in self.pizzas:
            print(f"  {pizza.name} - ${pizza.price}")
        print(f"Total: ${self.total_price}")

def main():
    menu = {
        "Margherita": Pizza("Margherita", 12, ["tomato sauce", "mozzarella"]),
        "Pepperoni": Pizza("Pepperoni", 15, ["tomato sauce", "mozzarella", "pepperoni"]),
        "Veggie": Pizza("Veggie", 14, ["tomato sauce", "mozzarella", "onions", "bell peppers"]),
    }

    order = Order()
    while True:
        print("Pizza menu:")
        for name, pizza in menu.items():
            print(f"  {name}: ${pizza.price}")
        print("Enter 'q' to finish ordering.")
        choice = input("What would you like to order? ")
        if choice == 'q':
            break
        elif choice in menu:
            order.add_pizza(menu[choice])
        else:
            print("Invalid choice.")

    order.print_order()

if __name__ == "__main__":
    main()