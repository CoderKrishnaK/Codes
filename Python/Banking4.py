# To Study OOP using Python Languaage 
# All Concept are Explained in it.
# 1) Instance variable:- Name,Account,Address,AccountNo
# 2) Instance Method :- CreateAccount,Display_Account_Info
# 3) Class Variable :- Bank_Name, ROI_ON_FD
# 4) Class Method :-  Display_Bank_Information
# 5) Static Method :- Dislay_KYC_INFO
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
    
    @classmethod
    def Display_Bank_Information(cls):
        print("Welcome to Banking Console")
        print("Name of Our Bank is :",cls.Bank_Name)
        print("Rate of interest we offer on fixed deposit is :",cls.ROI_ON_FD)

    @staticmethod
    def Display_KYC_INFO():
        print("Please Consider below KYC information")
        print("According to the rules of Goverment of India You have to Submit below Documents")
        print("1: Clear and Recent Passport Size Photo")
        print("2: Photo of Aadhar-Card")
        print("3: Photo of PAN-Card")



def main():
    Bank_Account.Display_KYC_INFO()

    print("Name of Bank :-",Bank_Account.Bank_Name)
    print("Rate of Interest on Fixed Deposit :-",Bank_Account.ROI_ON_FD)    
    
    Bank_Account.Display_Bank_Information()
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