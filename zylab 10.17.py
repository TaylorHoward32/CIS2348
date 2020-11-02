#Taylor Howard
#11-01-2020
#CIS2348-14654
#Zylab 10.17

#Create a class
class ItemToPurchase:

    # Default constructor

    def __init__(self):

        # Initializing variables w/ default values

        self.item_name = "none"

        self.item_price = 0

        self.item_quantity = 0

        #print the items

    def print_item_cost(self):

        #Display the item name, quantity and price

        print(self.item_name + " " + str(self.item_quantity) + " @ $"

              + str(self.item_price) + " = $" + str( self.item_price * self.item_quantity ))

if __name__ == "__main__":

    # main function &print the item1

    print("Item 1")

    # Creating object

    item1 = ItemToPurchase()

    #Creating the object to the class

    item2 = ItemToPurchase()

    # prompt & Read  details from the users input

    item1.item_name = input('Enter the item name:\n')

    item1.item_price = int(input('Enter the item price:\n'))

    item1.item_quantity = int(input('Enter the item quantity:\n'))

    print("\nItem 2")

    #prompt and Read details from the user input again

    item2.item_name = input('Enter the item name:\n')

    item2.item_price = int(input('Enter the item price:\n'))

    item2.item_quantity = int(input('Enter the item quantity:\n'))

    print("\nTOTAL COST")

    # need to print

    item1.print_item_cost()

    item2.print_item_cost()

    # accumulate cost of items

    total = (item1.item_price*item1.item_quantity)+(item2.item_price * item2.item_quantity)

    # Display the cost

    print("\nTotal: $" + str(total))