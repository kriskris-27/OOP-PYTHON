class AtmMachine:
    
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()
        
    
    def menu(self):
        user_input = input(
            """
            Hi how can i help you?
            1.1 to create pin
            2.2 to change pin
            3.3 to check balance
            4.4 to withdraw
            5.Anything to exit
            """
        )
        
        if user_input == "1":
            self.create_pin()
            #create pin
        elif user_input == "2":
            self.change_pin()
            #change pin
            
        elif user_input == "3":
            self.check_balance()
            #check balance
           
        elif user_input == "4":
            #withdraw
            self.withdraw()
            pass
        else:
            exit
        
        
    def create_pin(self):
        user_pin = input("Enter the pin to create: ")
        self.pin = user_pin
        
        user_balance = int(input("Enter balance: "))
        self.balance = user_balance
        print("Pin succesfully created")
        self.menu()
    
    
    def change_pin(self):
        old_pin = input("Enter user old pin:")
        if(old_pin == self.pin):
            new_pin = input("Enter new pin : ")
            self.pin=new_pin
            print("New pin created succesfully")
            self.menu()
        else:
            print("Invalid pin")
            self.menu()


    def check_balance(self):
        user_pin = input("Enter your pin:")
        if(user_pin == self.pin):
            print("balance:",self.balance)
            self.menu()
        else:
            print("Enter valid pin")
            self.menu()
            
    def withdraw(self):
        user_pin = input("Enter your pin:")
        if(user_pin == self.pin):
            amount = int(input("Enter the amount to withdraw: "))
            if amount <= self.balance:
                self.balance=self.balance - amount
                print("withdraw succesful,remaining balance ",self.balance)
            else:
                print("Enter amount lesser or equal to balance : ",self.balance)
        else:
            print("Enter valid pin")
            
        self.menu()
            
obj = AtmMachine()
obj.menu()
        
        
        
        
        