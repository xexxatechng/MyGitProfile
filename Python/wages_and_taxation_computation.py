#Code written by:       Christian Nwachukwu
#Date:                  25/05/2019
#Application puppose:   Application calculates groos pay, net pay and withholding Tax by collecting certain inputs from user.

class Pay:
    def __init__(self, hours, rate):
        #declare instance variables
        self.hourly_pay_rate = hours
        self.hours_worked = rate


#function computes gross pay
    def gross_payment(self):
        #calculates gross pay
        gross_pay = self.hourly_pay_rate * self.hours_worked
        return gross_pay


#function computes withholding tax
    def withholding_tax(self):
        #calculate withholding tax
        gross_pay = self.hourly_pay_rate * self.hours_worked
        if(gross_pay >= 0 and gross_pay < 300):
            tax = (10/100) * gross_pay
        elif(gross_pay >= 300 and gross_pay < 400):
            tax = (12/100) * gross_pay
        elif (gross_pay >= 400 and gross_pay < 500):
            tax = (15 / 100) * gross_pay
        elif (gross_pay >= 500):
            tax = (20/100) * gross_pay
        else:
            tax = print("Invalid")
            return tax

#function computes net pay
    def net_payment(self):
        #calculate Net Pay
        gross_pay = self.hourly_pay_rate * self.hours_worked
        net_pay = gross_pay - self.withholding_tax()
        return net_pay


while True:
    hourly_pay_rate = eval(input("Input Hourly Pay Rate: "))
    hours_worked = eval(input("Input Hours Worked: "))
    
    #An object "clerk" is created to compute his wages & taxation
    clerk = Pay(hourly_pay_rate, hours_worked)
    print()
    print("My Gross pay is: " + str(clerk.gross_payment()))
    print()
    clerk = Pay(hourly_pay_rate, hours_worked)
    print("My Withholding Tax is: " + str(clerk.withholding_tax()))
    print()
    clerk = Pay(hourly_pay_rate, hours_worked)
    print("My Net pay is: " + str(clerk.net_payment()))
    print("------------------------------------------")
    print("Press 'y' to re-enter")
    selection = input()
    if selection != 'y':
        break
    else:
        continue
