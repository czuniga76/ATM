# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 21:27:50 2020

@author: Christian Zuniga
    
"""
class Account():
    def __init__(self,pin,balance):
        self.pin = 123
        self.balance = 1000
        self.selection = 0
        
class ATM():
    def __init__(self):
        self.atmBalance = 10000
        
    def checkId(self,cardInfo,pin):
        account = self.getAccount(cardInfo) # connect to bank to get account info for this card
        if (account.pin != pin):
            print("Incorrect PIN for this account")
            return False,None
        else:
            # display options and store selection
            print(" Enter Action ")
            print(" 1. See Balance ")
            print(" 2. Deposit ")
            print(" 3. Withdraw")
            print(" 4. Exit")
            # TODO get selection
            self.selection = 3 # store selection
            return True,account
            
    def getAccount(self,cardInfo):
        # connect to bank network to get account info
        # impolement local account for testing
        account = Account()
        return account
    
    def checkCardPresent(self):
        # if card detected get card account number
        cardInfo = "cardInfo"
        return False,cardInfo # when card is detected
    
    def processCard(self,cardInfo):
        print("Enter pin") # get pin from user
        pin = 0
        confirm,account = self.checkId(cardInfo,pin)
        if confirm == True:
            account = self.processSelection(account)
            
        return account
            
    def processSelection(self,account):
        if self.selection == 1:
            print("Account balance ", account.balance)
        elif self.selection == 2: 
            # accept money deposit
            # count amount
            depositAmount = 1 # getAmountfrom
            self.balance += depositAmount
            account.balance += depositAmount
        elif self.selection == 3:
            # check account balance
            withdrawAmount = 1
            if withdrawAmount < account.balance:
                account.balance -= withdrawAmount
                self.balance -= withdrawAmount 
                
        return account 
            
        
        
    def updateAccount(self,account):
        # updated account in bank
        return None
            
    def reqService(self):
        #TODO check for errors and request service
        return None
    
 
def main():
    atm = ATM()
    noCard = True
    noErrors = True
    while noErrors:  # stay running unless errors occur
        while noCard == True:
        # wait for card to be inserted
            [noCard,cardInfo] = atm.checkCardPresent()
        account = atm.processCard(cardInfo)
        atm.updateAccount(account)
        noCard = True # ready for next request
        if atm.balance <0:
            noErrors = False # atm needs service
            atm.reqService()
            print("out of service")
        
    
        
if __name__ == "__main__":
    main()
    