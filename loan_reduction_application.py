"""
AUTHOR:     Christian Nwachukwu

TITLE:      Loan Reduction Applicationn

Date:       28/02/2019
"""



from tkinter import *

def loan_reduction_payment():
    installment_count=0
    for i in range(9):
        num1=float(number1.get())
        num2=float(number2.get())/100
        num3=int(number3.get())
        installment=(num3 + (num2*num3))
        installment_count = installment_count - 1
        finalresult=Label(root, text="Loan Payable is: N %.2f" % installment + "\nYour Balance is: N %.2f" % (num1-num3) +
                                     "\nInstallments Left is: ").grid(row=8, column=1)
        return

root = Tk()
root.geometry('400x200+100+200')
root.title('Loan Reduction Calculator')

number1=StringVar()
number2=StringVar()
number3=StringVar()

label=Label(root, text="This is a Loan Reduction Calculator").grid(row=0, column=0)
label=Label(root, text=" ").grid(row=1)
label1=Label(root, text="LOAN(N):", fg='red').grid(row=2, column=0)
label2=Label(root, text="RATE in %:", fg='blue').grid(row=3, column=0)
label3=Label(root, text="PAID SUM(N):", fg='green').grid(row=4, column=0)

num1=Entry(root, textvariable=number1, width=20).grid(row=2, column=1)
num2=Entry(root, textvariable=number2, width=20). grid(row=3, column=1)
num3=Entry(root, textvariable=number3, width=20).grid(row=4, column=1)

button1=Button(root, text='Calculate', command=loan_reduction_payment, width=10).grid(row=7, column=0)
button2=Button(root, text='Quit', command=root.quit, width=10).grid(row=7, column=1)

root.mainloop()
