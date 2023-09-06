import order_manager


def display_menu():
  print("Kibo Menu:")
  for index, item in enumerate(order_manager.get_menu_items()):
    print(f"{index+1}. {item['name']} : ${item['price']} ")
  print("0. Submit Order\n")


def is_valid_choice(choice):
  try:
    return 0 < int(choice) > 0 and int(choice) <= len(order_manager.get_menu_items())
  except:
    return False


def submit_order():
  # Calculate and display the final order total
  order_total = order_manager.get_order_total()
  print(f"Your order total is: ${order_total:.2f}")
  print("Order Submitted Successfully!")


def create_order():
  print("Welcome to the Food Ordering App!")
  display_menu()

  while True:

    #TODO  handle invliad input
    choice = int(input("Enter your choice (or 0 to submit order): "))

    if choice == 0:
      submit_order()
      break

    if not is_valid_choice(choice):
      print("Invalid Choice!")
      continue

    item = order_manager.get_menu_items()[choice - 1]
    
    if not item["available"]:
      print("Item not available!")

    else:
      quantity = int(input(f"How many {item['name']}s do you want to order? "))

      if quantity > 0:
        order_manager.add_order_item(item, quantity)
        
      else:
        print("Invlaid Quanitity")


if __name__ == "__main__":
  create_order()
