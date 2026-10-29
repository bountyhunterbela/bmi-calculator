# mini_inventory=["apples","milk","bread"]
# print(f"Current shopping list:{mini_inventory}")
# print(len(mini_inventory))
# new_item=str(input("Enter item you want to add:"))
# item_to_remove=str(input("Do you want to remove item:(yes/no)"))
# if new_item in mini_inventory:
#     print(f"Item is already in the list!")    
# else:
#     mini_inventory.append(new_item)
# if item_to_remove =="yes":
#     tell_removable=(str(input("Enter the item you want to remove:"))
#     mini_inventory.remove(tell_removable)
# else:
#     pass
# print(mini_inventory)


mini_inventory = ["apples", "milk", "bread"]
print(f"Current shopping list: {mini_inventory}")
print(f"Total items: {len(mini_inventory)}")

new_item = input("Enter item you want to add: ")

if new_item in mini_inventory:
    print(f"'{new_item}' is already in the list!")    
else:
    mini_inventory.append(new_item)
    print(f"Successfully added! Current list: {mini_inventory}")

# .lower() ensures "Yes", "YES", or "yes" all work
remove_choice = input("Do you want to remove an item? (yes/no): ").lower()

if remove_choice == "yes":
    item_to_remove = input("Enter the item you want to remove: ")
    if item_to_remove in mini_inventory:
        mini_inventory.remove(item_to_remove)
        print(f"Removed! Final list: {mini_inventory}")
    else:
        print(f"'{item_to_remove}' is not in the list, so nothing was removed.")
else:
    print(f"Final list: {mini_inventory}")