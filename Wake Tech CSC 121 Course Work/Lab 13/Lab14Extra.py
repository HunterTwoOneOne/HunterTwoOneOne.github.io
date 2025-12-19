# Nathanael Long
# 12/14/2025
# GUI Programing Lab - Cash Register


'''
Simple cash register. It has only 3 item options. Workbooks @ 8.50, Textbooks @ 24.00,
and Magazines @ 5.95 each. There's a toggle for a 25% Discount that can be selected.
The program takes the items and depending on if the 25% Discount has selected or not
gives the total or takes off 1/4 of the total and gives that.
'''

import tkinter

class cash_register:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('$$$ CASH REGISTER $$$')
        self.frame = tkinter.Frame(self.main_window)
        tkinter.Label(self.frame, text='WORKBOOKS').grid(row=0, column=0)
        self.workbooks = tkinter.Entry(self.frame, width=5)
        self.workbooks.grid(row=0, column=1)
        tkinter.Label(self.frame, text='TEXTBOOKS').grid(row=1, column=0)
        self.textbooks = tkinter.Entry(self.frame, width=5)
        self.textbooks.grid(row=1, column=1)
        tkinter.Label(self.frame, text='MAGAZINES').grid(row=2, column=0)
        self.magazines = tkinter.Entry(self.frame, width=5)
        self.magazines.grid(row=2, column=1)
        self.discount_var = tkinter.IntVar()
        tkinter.Checkbutton(self.frame, text='25% DISCOUNT',
                            variable=self.discount_var).grid(row=3, columnspan=2)
        tkinter.Label(self.frame, text='TOTAL').grid(row=4, column=0)
        self.total_var = tkinter.StringVar()
        tkinter.Label(self.frame, textvariable=self.total_var).grid(row=4, column=1)
        tkinter.Button(self.frame, text='CALCULATE',
                       command=self.calculate).grid(row=5, column=0)
        tkinter.Button(self.frame, text='EXIT',
                       command=self.main_window.destroy).grid(row=5, column=1)
        self.frame.pack()
        tkinter.mainloop()

    def calculate(self):
        try:
            total = (int(self.workbooks.get()) * 8.50 +
                     int(self.textbooks.get()) * 24.00 +
                     int(self.magazines.get()) * 5.95)
            if self.discount_var.get() == 1:
                total *= 0.75
            self.total_var.set(f'${total:.2f}')
        except ValueError:
            self.total_var.set('ERROR!')

if __name__ == '__main__':
    cash_register()