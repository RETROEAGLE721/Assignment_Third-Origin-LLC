from operator import index
import pandas as pd
from datetime import date 


class budget_tracker:
    
    def __init__(self, income : int ,expense_list : dict):
        self.income = income
        self.expense_list = pd.DataFrame(expense_list)

    def calculate_expense(self):
        return self.income - sum(self.expense_list["Amount"])
    
    def view_expense_list(self):
        return self.expense_list
    
    def save_list(self):
        today_date = date.today()
        self.expense_list.to_csv("ExpenseList_"+str(today_date)+".csv")
        
    def analyze_expense(self):
        self.expense_list['Amount used in %'] = (self.expense_list['Amount'] / self.income) * 100
        return self.expense_list
        


income_amount = ""
name= []
amount=[]
expense_list = {}
while True:
    print("1. Enter income\n"+
          "2. Enter expense list\n"+
          "3. View expense list\n"+
          "4. Calculation remaining amount\n"+
          "5. Analysis expense\n"+
          "6. Exit"
          )
    try:
        user_input = int(input("Enter number :- "))
    except:
        print("Note :- Please enter a number")
        
        
    if user_input == 1:
        
        try:
            income_amount = int(input("Please enter income :- "))
        except:
            print("Note :- PLease enter numbers")  
            
              
    elif user_input == 2:
        
        while True:
            print('Please enter "done" when you completed entering expenses ')
            user_input = input("Enter Name :- ")
            if user_input.lower() == "done":
                break
            else:
                name.append(user_input.capitalize())
                amount.append(int(input("Enter Amount :- ")))
        expense_list = {"Name": name, "Amount": amount}
        
    elif user_input == 3:
        
        if name == []:
            print("Please enter Expense List")
        else:
            print(s1.view_expense_list())
        
    elif user_input == 4:
        
        if income_amount == "":
            print("PLease enter income_amount")
        if name == []:
            print("Please enter expense list")
        if income_amount != "" and name != []:
            print("Your expense is",income_amount-s1.calculate_expense())
            print("Remaining Amount is",s1.calculate_expense())
    
    elif user_input == 5:
        
        if income_amount == "":
            print("PLease enter income_amount")
        if name == []:
            print("Please enter expense list")
        if income_amount != "" and name != []:
            print(s1.analyze_expense())
    
    
    elif user_input == 6:
        
        s1.save_list()
        exit()

    s1 = budget_tracker(income_amount, expense_list)
