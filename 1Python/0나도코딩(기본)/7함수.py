#함수 공부1(개념)
#일종의 박스라고 생각하면 됨.
#5라는 값을 박스에 넣으면, 20을 더한 값을 줌.
def open_account() :
    print("new account is opened")

open_account()

#함수 공부2(전달값과 반환값)
def deposit(balance, money) :
    print("Deposit is completed. now balance is {0}".format(balance + money))
    return balance + money

account1 = 0
account1 = deposit(account1, 1000)

def withdraw(balance, money) :
    if balance >- money :
        print("Withdraw is completed. now balance is {0}".format(balance - money))
        return balance - money
    else :
        print("Withdraw is failed. now balance is {0}.".format(balance))    
        return balance

account2 = 0
account2 = deposit(account2, 1000)
account2 = withdraw(account2, 500)

def withdraw_night(balance, money) : 
    commission = 100
    print("Commission is {0}, now balance is {1}".format(commission, balance - money - commission))
    return commission, balance - money - commission

account3 = 2000
account3 = withdraw_night(account3, 1000)
















