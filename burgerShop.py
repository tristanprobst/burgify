class FoodItem:    
    #constructor
    def __init__(self, name, itemType, price):        
        #following attributes are common for all classes
        self.itemName = name
        self.foodType = itemType
        self.price = float(price)    
    #common methods
    def getItemName(self):
        return self.itemName    
    def getPrice(self):
        return self.price    
    def getItemType(self):
        return self.foodType
        
#now we implement the item classes by deriving them from the FoodItem class
class Burger(FoodItem):    
    def __init__(self, name, itemType, price, toppings):
        super().__init__(name, itemType, price)        
        self.toppings = toppings
    def getToppings(self):
        return self.toppings
        
class Drink(FoodItem):    
    def __init__(self, name, itemType, price, size):        
        super().__init__(name, itemType, price)        
        self.size = size
    def getSize(self):
        return self.size
        
class Side(FoodItem):    
    def __init__(self, name, itemType, price, size):        
        super().__init__(name, itemType, price)        
        self.size = size
    def getSize(self):
        return self.size
        
class Combo(FoodItem):    
    def __init__(self, burger, drink, side):        
        self.comboBurger = burger
        self.comboDrink = drink
        self.comboSide = side       
        self.totalPrice = self.comboBurger.getPrice() + self.comboDrink.getPrice() + self.comboSide.getPrice()        
        super().__init__("Combo", "combo", self.totalPrice)
    def getBurger(self):
        return self.comboBurger
    def getDrink(self):
        return self.comboDrink
    def getSide(self):
        return self.comboSide
        
class Order:    
    def __init__(self, name):       
        self.userName = name        
        self.orderedItems = [] #this list stores the ordered items    
    def add(self, item): #this method adds new item in ordered items list
        self.orderedItems.append(item)    
    def orderTotal(self): #this method is used to calculate the total price of all items in the orderedItems list
        total = 0        
        for item in self.orderedItems:            
            total += item.getPrice()        
        return total    
    def printOrderedItems(self):        
        print("\nUser name: ", self.userName)
        print("\n{:<20} {:<20} {:<20} {:<20}".format("Item No. ", "Item Name", "Item type", "Price"))        
        count = 0
        for item in self.orderedItems: 
            count += 1        
            print("\n{:<20} {:<20} {:<20} {:<20.2f}".format(count, item.getItemName(), item.getItemType(), item.getPrice()))
            if item.getItemType() == "burger":
                for topping in item.getToppings():
                    print("{:<22} {:<20}".format("", topping))
            elif item.getItemType() == "combo":
                print("{:<22} {:<20} {:<20} {:<20.2f}".format("", item.getBurger().getItemName(), item.getBurger().getItemType(), item.getBurger().getPrice()))
                for topping in item.getBurger().getToppings():
                    print("{:<24} {:<20}".format("", topping))
                print("{:<22} {:<20} {:<20} {:<20.2f}".format("", item.getSide().getItemName(), item.getSide().getItemType(), item.getSide().getPrice()))
                print("{:<24} {:<20}".format("", item.getSide().getSize()))
                print("{:<22} {:<20} {:<20} {:<20.2f}".format("", item.getDrink().getItemName(), item.getDrink().getItemType(), item.getDrink().getPrice()))
                print("{:<24} {:<20}".format("", item.getDrink().getSize()))
            else:
                print("{:<22} {:<20}".format("", item.getSize()))
			
#following methods used to create a food item object by taking inputs from the user  
def user_input_burger():    
    burgerPrices = {
        "hamburger": 1.00,
        "cheeseburger": 2.00,
        "baconburger": 3.00,
        "veggieburger": 4.00
    }
    burgerType = input("\nPlease select burger type: \nhamburger \ncheeseburger \nbaconburger \nveggieburger \n\n")
    while burgerType.lower() not in burgerPrices.keys():
        if burgerType.lower() == "x":
            print("Your order has been cancelled. Thanks for visiting Burgify!")
            exit()
        print("Not a valid choice.")
        burgerType = input("Please select burger type: ")        
    print(burgerType, " ", burgerPrices[burgerType])
    price = burgerPrices[burgerType] 
    toppingPrices = {
        "ketchup": 0.50,
        "mayo": 0.50,
        "mustard": 0.50,
    }
    toppingsList=[]    
    toppingCount = 0
    print("\nPlease select up to 3 toppings(enter d when done): \nketchup \nmayo \nmustard\n")
    while toppingCount < len(toppingPrices.keys()):
        topping = input("")
        if topping == "d":
            break
        elif topping.lower() == "x":
            print("Your order has been cancelled. Thanks for visiting Burgify!")
            exit()
        elif topping.lower() not in toppingPrices.keys():
            print("Not a valid choice.")
        else:
            toppingsList.append(topping)
            toppingCount += 1
            
    for topping in toppingsList:
        price += toppingPrices[topping]  
    b = Burger(burgerType, "burger", price, toppingsList)
    return b
    
def user_input_drink():
    drinkPrices = {
        "sprite": (1.00, 1.50),
        "coke": (1.25, 1.75),
        "diet pepsi": (1.50, 2.00)
    }
    
    drinkType = input("\nChoose a drink: \nsprite\ncoke\ndiet pepsi\n\n")
    while drinkType.lower() not in drinkPrices.keys():
        if drinkType.lower() == "x":
            print("Your order has been cancelled. Thanks for visiting Burgify!")
            exit()
        print("Invalid selection.")
        drinkType = input("\nChoose a drink: \nsprite\ncoke\ndiet pepsi\n\n")
    drinkSize = input("\nChoose a size: \nsmall\nlarge\n\n")
    while drinkSize.lower() not in ["small", "large"]:
        if drinkSize.lower() == "x":
            print("Your order has been cancelled. Thanks for visiting Burgify!")
            exit()
        print("Invalid selection.")
        drinkSize = input("\nChoose a size: \nsmall\nlarge\n\n")
    d = Drink(drinkType, "drink", drinkPrices[drinkType][0] if drinkSize == "small" else drinkPrices[drinkType][1], drinkSize)    
    return d
    
def user_input_side():
    sidePrices = {
        "fries": (1.75, 3.00),
        "onion rings": (2.00, 3.25),
        "salad": (3.45, 5.00)
    }
    sideType = input("\nChoose a side: \nfries\nonion rings\nsalad\n\n")
    while sideType.lower() not in sidePrices.keys():
        if sideType.lower() == "x":
            print("Your order has been cancelled. Thanks for visiting Burgify!")
            exit()
        print("Invalid selection.")
        sideType = input("\nChoose a side: \nfries\nonion rings\nsalad\n\n")
    sideSize = input("\nChoose a size: \nsmall\nlarge\n\n")
    while sideSize.lower() not in ["small", "large"]:
        if sideSize.lower() == "x":
            print("Your order has been cancelled. Thanks for visiting Burgify!")
            exit()
        print("Invalid selection.")
        sideSize = input("\nChoose a size: \nsmall\nlarge\n\n")
    s = Side(sideType, "side", sidePrices[sideType][0] if sideSize == "small" else sidePrices[sideType][1], sideSize)
    return s
    
def user_input_combo():
    #a combo must include one burger, one side, and one drink
    print("\nA combo includes one burger, one side, and one drink.")
    c = Combo(user_input_burger(), user_input_drink(), user_input_side()) #ask user for input and store it in combo object
    return c
    
def take_order():    
    userName = input("\nPlease enter your name: ")
    if userName.lower() == "x"    :
        print("Your order has been cancelled. Thanks for visiting Burgify!")
        exit()
    myOrder = Order(userName)   
    while True:
        myOrder.printOrderedItems() 
        print("\n\nMenu: \n1. Burger \n2. drink \n3. Side \n4. Combo \n5. Order")        
        userChoice = input("\nEnter your choice from above: ")        
        if userChoice == "1":            
            myOrder.add(user_input_burger())       
        elif userChoice == "2":            
            myOrder.add(user_input_drink())        
        elif userChoice == "3":            
            myOrder.add(user_input_side())        
        elif userChoice == "4":            
            myOrder.add(user_input_combo())        
        elif userChoice == "5":
            break
        elif userChoice.lower() == "x":
            print("Your order has been cancelled. Thanks for visiting Burgify!")
            exit()        
        else:
            print("Please enter a valid option.")    
    print("\nYour ordered Items are: ")
    myOrder.printOrderedItems()    
    isOrder = input("\nEnter 1 to confirm your order or 0 to cancel: ")    
    if isOrder == "1":        
        print(f"\nOrder confirmed.\n\nTotal: ${myOrder.orderTotal()}\n")    
    elif isOrder == "0" or isOrder == "x":        
        print(f"\nYour order has been cancelled. Thanks for visiting Burgify!\n")
        exit()
    else:
        print("\nPlease enter a valid option.")
        take_order()    #display a thank you message
    print(f"\nThanks for ordering from Burgify!\n")
    
print("Welcome to burgify!")
print("Enter 'x' at any time to exit.")
take_order()