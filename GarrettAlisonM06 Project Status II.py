"""
Program:GarrettAlison_FinalProject
Author: Alison Garrett
Last Date Modified: 3/1/2022

The purpose of this program is to allow a user to plan a visit to
Ivy Tech for one of their visit days.

"""

from breezypythongui import EasyFrame

import tkinter as tk

class Page1(EasyFrame):
    """sets up window and widgets"""
    def __init__(self):
        
        EasyFrame.__init__(self, width = 350, height = 300, title = "Ivy Visit Planner")
        
        self["background"] = "green"
        self.addLabel(text = "Welcome to Ivy Visit Planner!", row = 0, column =0, columnspan = 2, sticky = "NSEW")
        self.addLabel(text = "Please start customizing your visit", row = 1, column = 0, columnspan =2, sticky = "NSEW")
        #Enter First and Last Name
        self.addLabel(text = "First Name", row = 2, column = 0)
        self.inputField = self.addTextField(text = "", row = 2, column = 1)

        self.addLabel(text = "Last Name", row = 3, column = 0)
        self.inputField = self.addTextField(text = "", row = 3, column = 1)
        
        #Date of Birth
        self.addLabel(text = "Date of Birth (MM/DD/YY)", row = 4, column = 0)
        self.inputField = self.addTextField(text = "", row = 4, column = 1)
        
        #Phone Number
        self.addLabel(text = "Phone Number (111-222-3333)", row = 5, column = 0)
        self.inputField = self.addTextField(text = "", row = 5, column = 1)
        
        #Email
        self.addLabel(text = "Email", row = 6, column = 0)
        self.inputField = self.addTextField(text = "", row = 6, column = 1)

        #NextButton
        self.nextBtn = self.addButton(text = "Next Page", row = 7, column = 0, columnspan = 2, command = self.close)

    def close(self):
        self.master.destroy()

class Page2(EasyFrame):
    """sets up window and widgets"""
    def __init__(self):
        
        EasyFrame.__init__(self, width = 350, height = 200, title = "Ivy Visit Planner")
        self["background"] = "green"
        self.addLabel(text = "When would you like to visit?", row = 0, column =0, columnspan = 2, sticky = "NSEW")
        
        #Date Radiobuttons
        self.addLabel(text = "Date", row = 1, column = 0)
        self.dateGroup = self.addRadiobuttonGroup(row = 2, column = 0)
        defaultRB = self.dateGroup.addRadiobutton(text = "April 1, 2022")
        self.dateGroup.addRadiobutton(text = "May 6, 2022")
        self.dateGroup.addRadiobutton(text = "June 3, 2022")
        #Time Radiobuttons
        self.addLabel(text = "Time", row = 1, column = 1)
        self.timeGroup = self.addRadiobuttonGroup(row = 2, column = 1)
        defaultRB = self.timeGroup.addRadiobutton(text = "10am-12pm")
        self.timeGroup.addRadiobutton(text = "12pm-2pm")
        self.timeGroup.addRadiobutton(text = "2pm-4pm")
    
def main():
    Page1().mainloop()
    Page2().mainloop()

if __name__ == "__main__":
    main()


