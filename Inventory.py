#Start of the Product Class
class product:

    #Starting the Constructor
    def __init__(self):
        self.h = 0
        self.code = []
        self.name = []
        self.price = []
    #End of the Constructor
        
    
    #Start of Inserting the Product in the inventory
    def enter(self):
        self.h += 1
        self.code.append(0)
        self.name.append(0)
        self.price.append(0)
        try:
            self.a = input("Enter the name of the product: ")
            self.b = int(input("Enter the MRP of the product: "))
            for i in range(0, self.h):
                self.c = int(input("Enter the code number of the product: "))
                if(self.c == self.code[i]):
                    print("Enter a unique code number.")
                    i -= 1
                else:
                    self.code[i] = self.c
                    self.name[i] = self.a
                    self.price[i] = self.b
        except Exception:
            print("Invalid Input.")
    #End of Inserting the Product in the Inventory


    #Start of Searching the Product in the Inventory
    def search(self):
        try:
            self.x = int(input("Enter the code number of the product you want to search: "))
            for i in range(0, self.h):
                if(self.x == self.code[i]):
                    print("The product is found: \n", "Name: ", self.name[i], " Price: Rs.", self.price[i], " Code: ", self.code[i])
                    break
            else:
                print("The product is not in the inventory.")
        except Exception:
            print("Invalid Input.")
    #End of Searching the Product in the Inventory


    #Start of Deleting the Product from the Inventory
    def delete(self):
        try:
            self.y = int(input("Enter the code number of the product you want to delete: "))
            for i in range(0, self.h):
                if(self.y == self.code[i]):
                    del self.code[i]
                    del self.name[i]
                    del self.price[i]
                    self.h -= 1
                    print("The product is deleted from the inventory.")
                    break
                else:
                    print("The product is not in the inventory.")
        except Exception:
            print("Invalid Input.")
    #End of Deleting the Product from the Inventory


    #Start of Displaying the Inventory
    def inventory(self):
        print("All the products in the inventory are as below: ")
        for i in range(0, self.h):
            print("Name: ", self.name[i], "  Rs.", self.price[i], " Code number: ", self.code[i])
    #End of Displaying the Inventory


#End of the Product Class

#Start of the Menu
def menu():
    obj = product()
    c = 'y'
    while(c == 'y'):
        print("1. Enter a Product in the Inventory.")
        print("2. Search a Product in the Inventory.")
        print("3. Delete a Product in the Inventory.")
        print("4. Display the Inventory.")
        try:
            choice = int(input("Enter your Choice: "))
            if(choice == 1):
                obj.enter()
            elif(choice == 2):
                obj.search()
            elif(choice == 3):
                obj.delete()
            elif(choice == 4):
                obj.inventory()
            else:
                print("Wrong Input")
            d = input("Do you want to continue: ")
            c = d.lower()
        except Exception:
            print("Invalid Input.")
#End of the Menu


#Main Function

menu()

#Function End
