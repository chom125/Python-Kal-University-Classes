import tkinter


class InvestmentCalculator:
    def __init__(self):
        # create main window
        self.main_window = tkinter.Tk()

        # create four frames
        self.frame_1 = tkinter.Frame(self.main_window)
        self.frame_2 = tkinter.Frame(self.main_window)
        self.frame_3 = tkinter.Frame(self.main_window)
        self.frame_4 = tkinter.Frame(self.main_window)
        self.frame_5 = tkinter.Frame(self.main_window)

        # Adding investment amount label and text box
        self.investmentAmt_label = tkinter.Label(self.frame_1, text='Investment Amount: ')
        self.investmentAmt_entry = tkinter.Entry(self.frame_1, width=10)
        self.investmentAmt_label.pack(side='left')
        self.investmentAmt_entry.pack(side='right')

        # Adding years label and text box
        self.years_label = tkinter.Label(self.frame_2, text='Years: ')
        self.years_entry = tkinter.Entry(self.frame_2, width=10)
        self.years_label.pack(side='left')
        self.years_entry.pack(side='right')

        # Adding Annual Interest Rate label and text box
        self.annualInterestRate_label = tkinter.Label(self.frame_3, text='Annual Interest Rate: ')
        self.annualInterestRate_entry = tkinter.Entry(self.frame_3, width=10)
        self.annualInterestRate_label.pack(side='left')
        self.annualInterestRate_entry.pack(side='right')

        # Adding future value labels
        self.futureValue_label = tkinter.Label(self.frame_4, text='Future Value')
        self.fv = tkinter.StringVar()
        self.fvalue_label = tkinter.Label(self.frame_4, textvariable=self.fv)
        self.futureValue_label.pack(side='left')
        self.fvalue_label.pack(side='right')

        # Adding buttons
        self.calc_button = tkinter.Button(self.frame_5, text='Calculate', command=self.calc_investment)

        # Adding button
        self.calc_button.pack(side='left')

        # Adding frames to window
        self.frame_1.pack()
        self.frame_2.pack()
        self.frame_3.pack()
        self.frame_4.pack()
        self.frame_5.pack()

        # Add this line to display
        self.main_window.mainloop()

    # Call this function to calculate future value
    def calc_investment(self):
        # Get invest amount
        self.invAmt = float(self.investmentAmt_entry.get())
        # Get years
        self.years = int(self.years_entry.get())
        # Get annual Int Rate
        self.annualIntRate = float(self.annualInterestRate_entry.get())

        # calculating interest rate
        self.intRate = (self.annualIntRate / 12.0) / 100.0;

        # calculating Future Value
        self.futureValue = self.invAmt * ((1 + self.intRate) ** (self.years * 12));

        # update the future value label
        self.fv.set(str(round(self.futureValue, 2)))


# Calling class
inv = InvestmentCalculator();