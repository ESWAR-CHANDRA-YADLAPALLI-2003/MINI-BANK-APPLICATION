class Bank:
    bank_name='UNION BANK OF INDIA'
    bank_ifsc='UBIN0807320'
    bank_roi='5'
    bank_address='Badvel'
    bank_branch='M.V.Palli'
    def __init__(self,n,a,ac,b,ad,pin):
        self.name=n
        self.age=a
        self.account=ac
        self.balance=b
        self.address=ad
        self.pin=pin
    def customer_details(self):
        print(f'Customer Name : {self.name}')
        print(f'Customer Age : {self.age}')
        print(f'Customer Account Number : {self.account}')
        print(f'Customer Account Balance : {self.balance}')
        print(f'Customer Address : {self.address}')
    @classmethod
    def bank_details(cls):
        print(f'Bank Name : {cls.bank_name}')
        print(f'Bank Ifsc : {cls.bank_ifsc}')
        print(f'Bank Rate of Interest : {cls.bank_roi}')
        print(f'Bank Address : {cls.bank_address}')
        print(f'Bank Branch : {cls.bank_branch}')
    @staticmethod
    def get_int_value():
        value=int(input('Enter amount : '))
        return value
    def withdraw(self):
        pin=int(input("Enter your PIN : "))
        if pin==self.pin:
            amount=self.get_int_value()
            if self.balance>=amount:
                self.balance-=amount
                print(f'Withdraw Successfully \nAvailable Balance is : {self.balance}')
            else:
                print(f'Insufficient Balance \nAvailable Balance is : {self.balance}')
        else:
            print("INCORRECT PIN \nPlease Enter Correct PIN")
    def deposite(self):
        pin=int(input("Enter your PIN : "))
        if pin==self.pin:
            amount=self.get_int_value()
            if amount>0:
                self.balance+=amount
                print(f'Deposited Successfully \nAvailable Balance is : {self.balance}')
            else:
                print('Amount Should be more than ZERO [0]')
        else:
            print("INCORRECT PIN \nPlease Enter Correct PIN")
            

            
eswar=Bank('ESWAR CHANDRA YADLAPALLI',21,12345,100000,'GVM',12345)
operation=int(input("Choose one Option From this(1 or 2 or 3) : \n 1.DEPOSITE \n 2.WITHDRAW \n 3.CHECKBALANCE : "))
if operation==1:
    eswar.deposite()
elif operation==2:
    eswar.withdraw()
else:
    pin=int(input("Enter your PIN : "))
    if pin==eswar.pin:
            print(f'Available Balance is : {eswar.balance}')
    else:
            print("INCORRECT PIN \nPlease Enter Correct PIN")




        





















