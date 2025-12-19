
#
# Nathanael Long
# 12/14/2025
# GUI Programing Lab - Grade Calculator

'''
Simple Grade Calculator. Generates a GUI for users to input the numbers.
Tests, Labs, and Exams. Each of these has a 'weight' and is factored in.
The program then assigns the letter grade associated.(e.x. A is a 90 or higher)
'''


import tkinter
import tkinter.messagebox

class grade_calculator:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('GRADE CALCULATOR')
        self.main_window.geometry('260x125')

        self.test_frame = tkinter.Frame(self.main_window)
        self.lab_frame = tkinter.Frame(self.main_window)
        self.exam_frame = tkinter.Frame(self.main_window)
        self.avg_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        tkinter.Label(self.test_frame, text='TESTS GRADE').pack(side='left')
        self.test_entry = tkinter.Entry(self.test_frame, width=10)
        self.test_entry.pack(side='left')
        tkinter.Label(self.lab_frame, text='LABS GRADE').pack(side='left')
        self.lab_entry = tkinter.Entry(self.lab_frame, width=10)
        self.lab_entry.pack(side='left')
        tkinter.Label(self.exam_frame, text='EXAMS GRADE').pack(side='left')
        self.exam_entry = tkinter.Entry(self.exam_frame, width=10)
        self.exam_entry.pack(side='left')
        tkinter.Label(self.avg_frame, text='GRADE AVERAGE').pack(side='left')
        self.avg_var = tkinter.StringVar()
        self.avg_var.set('---')
        tkinter.Label(self.avg_frame, textvariable=self.avg_var).pack(side='left')
        tkinter.Button(self.button_frame, text='CALCULATE',
                       command=self.calculate).pack(side='left')
        tkinter.Button(self.button_frame, text='EXIT',
                       command=self.main_window.destroy).pack(side='left')

        self.test_frame.pack()
        self.lab_frame.pack()
        self.exam_frame.pack()
        self.avg_frame.pack()
        self.button_frame.pack()
        tkinter.mainloop()

    def calculate(self):
        try:
            tests = float(self.test_entry.get())
            labs = float(self.lab_entry.get())
            exams = float(self.exam_entry.get())
            average=tests*0.2+labs*0.3+exams*0.5
            if average >= 90:
                letter_grade = 'A'
            elif average >= 80:
                letter_grade = 'B'
            elif average >= 70:
                letter_grade = 'C'
            elif average >= 60:
                letter_grade = 'D'
            else:
                letter_grade = 'F'
            self.avg_var.set(f'{average:.1f} ({letter_grade})')
        except ValueError:
            self.avg_var.set('ERROR!')

if __name__ == '__main__':
    grade_calculator()