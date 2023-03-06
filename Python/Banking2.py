# To Study OOP using Python Languaage 
# All Concept are Explained in it.
# Instance variable:- Name,Account,Address,AccountNo
# Instance Method :- CreateAccount,Display_Account_Info
# class Variable :- Bank_Name, ROI_ON_FD

class Bank_Account:

    Bank_Name = "HDFC Bank PVT LTD"
    ROI_ON_FD = 6.7


    def __init__(self):
        self.Name = ""
        self.Amount = 0
        self.Address = ""
        self.AccountNo = 0 
    
    def CreateAccount(self):
        print("Enter your Name:-")
        self.Name = input()

        print("Enter your Initial Amount:-")
        self.Amount = int(input())
        
        print("Enter your Address:-")
        self.Address = input()
        
        print("Enter your Account Number:-")
        self.AccountNo = int(input())

    def Display_Account_Info(self):    
        print("-----------------Your Account Information is as below--------------")
        print("Name of Account Holder :- ",self.Name)
        print("Account Number :- ",self.AccountNo)
        print("Adddress of Account Holder :- ",self.Address)
        print("Current Amount in Account :- ",self.Amount)
def main():
    print("Name of Bank :-",Bank_Account.Bank_Name)
    print("Rate of Interest on Fixed Deposit :-",Bank_Account.ROI_ON_FD)    
    
    User1 = Bank_Account()
    User2 = Bank_Account()

    print("Creating the first Account")
    User1.CreateAccount()
    print("Creating the Second Account")
    User2.CreateAccount()

    User1.Display_Account_Info()
    User2.Display_Account_Info()

if __name__ == "__main__":
    main()